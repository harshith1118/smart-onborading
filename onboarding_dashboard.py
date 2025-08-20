"""
Streamlit App: Onboarding Training Compliance Tracker
"""

import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Onboarding Compliance Dashboard", layout="wide")
st.title("Onboarding Training Compliance Tracker")

# 1. Load Data
csv_path = "onboarding_training_dataset.csv"
df = pd.read_csv(csv_path)

# 2. Data Cleaning
binary_cols = ['Security_Training', 'Tool_Access', 'Role_Training', 'Compliance', 'Orientation']
for col in binary_cols:
    df[col + '_bin'] = df[col].map({'Completed': 1, 'Pending': 0})
df['Start_Date'] = pd.to_datetime(df['Start_Date'], errors='coerce')

# 3. Save Cleaned Data to SQLite
db_path = "onboarding_compliance.db"
conn = sqlite3.connect(db_path)
df.to_sql('onboarding', conn, if_exists='replace', index=False)

st.sidebar.header("Filters")
departments = st.sidebar.multiselect(
    "Select Departments", options=df['Department'].unique(), default=[])
locations = st.sidebar.multiselect(
    "Select Locations", options=df['Location'].unique(), default=[])

if departments and locations:
    filtered_df = df[df['Department'].isin(departments) & df['Location'].isin(locations)]
elif departments:
    filtered_df = df[df['Department'].isin(departments)]
elif locations:
    filtered_df = df[df['Location'].isin(locations)]
else:
    filtered_df = df.copy()



# 4. Completion Rates by Department (Interactive Plotly Bar Chart with Filtering)
st.header("Completion Rates by Department")
if not filtered_df.empty:
    department_completion = filtered_df.groupby('Department')[['Security_Training_bin', 'Tool_Access_bin', 'Role_Training_bin', 'Compliance_bin', 'Orientation_bin']].mean().reset_index()
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(x=department_completion['Department'], y=department_completion['Security_Training_bin'], name='Security'))
    fig1.add_trace(go.Bar(x=department_completion['Department'], y=department_completion['Tool_Access_bin'], name='Tool'))
    fig1.add_trace(go.Bar(x=department_completion['Department'], y=department_completion['Role_Training_bin'], name='Role'))
    fig1.update_layout(barmode='group', title='Training Module Completion Rates by Department', yaxis_title='Completion Rate')
    st.plotly_chart(fig1, use_container_width=True)


# 5. Manager Feedback vs. Modules Completed (Interactive Plotly Scatter)
st.header("Manager Feedback vs. Modules Completed")
filtered_df['Modules_Completed'] = filtered_df[[col + '_bin' for col in binary_cols]].sum(axis=1)
if not filtered_df.empty:
    fig2 = px.scatter(
        filtered_df,
        x='Modules_Completed',
        y='Manager_Feedback_Score',
        color='Department',
        title='Manager Feedback vs. Modules Completed',
        labels={"Modules_Completed": "Modules Completed", "Manager_Feedback_Score": "Manager Feedback Score"}
    )
    st.plotly_chart(fig2, use_container_width=True)


# 6. Compliance vs. Satisfaction by Location (Interactive Plotly Heatmap)
st.header("Compliance vs. Satisfaction by Location")
heatmap_data = filtered_df.groupby('Location')[['Compliance_bin', 'Employee_Satisfaction_Score']].mean().reset_index()
if not heatmap_data.empty:
    fig3 = go.Figure(data=go.Heatmap(
        z=heatmap_data['Compliance_bin'],
        x=heatmap_data['Location'],
        y=heatmap_data['Employee_Satisfaction_Score'],
        colorscale='YlGnBu',
        colorbar=dict(title='Compliance Rate')
    ))
    fig3.update_layout(title='Compliance vs. Satisfaction by Location', xaxis_title='Location', yaxis_title='Avg Satisfaction Score')
    st.plotly_chart(fig3, use_container_width=True)


# 7. Buddy Assignment Impact (Interactive Table)
st.header("Buddy Assignment Impact")
buddy_impact = filtered_df.groupby('Buddy_Assigned')[['Manager_Feedback_Score', 'Employee_Satisfaction_Score']].mean().reset_index()
st.dataframe(buddy_impact, use_container_width=True)




# 8. Module Completion by Department and Location (Grouped Bar Chart)
st.header("Module Completion by Department and Location")
if not filtered_df.empty:
    completion_grouped = filtered_df.groupby(['Department', 'Location'])[['Security_Training_bin', 'Tool_Access_bin', 'Role_Training_bin', 'Compliance_bin', 'Orientation_bin']].mean().reset_index()
    melted = completion_grouped.melt(id_vars=['Department', 'Location'], value_vars=['Security_Training_bin', 'Tool_Access_bin', 'Role_Training_bin', 'Compliance_bin', 'Orientation_bin'], var_name='Module', value_name='Completion Rate')
    fig_bar = px.bar(melted, x='Department', y='Completion Rate', color='Module', barmode='group', facet_col='Location', title='Module Completion Rates by Department and Location')
    st.plotly_chart(fig_bar, use_container_width=True)

# 9. Module Completion Trend by Start Date (Line Chart)
st.header("Module Completion Trend by Start Date")
if not filtered_df.empty:
    trend_df = filtered_df.copy()
    trend_df['Month'] = trend_df['Start_Date'].dt.to_period('M').astype(str)
    trend_grouped = trend_df.groupby('Month')[['Security_Training_bin', 'Tool_Access_bin', 'Role_Training_bin', 'Compliance_bin', 'Orientation_bin']].mean().reset_index()
    fig_line = px.line(trend_grouped, x='Month', y=['Security_Training_bin', 'Tool_Access_bin', 'Role_Training_bin', 'Compliance_bin', 'Orientation_bin'], title='Module Completion Trend Over Time')
    st.plotly_chart(fig_line, use_container_width=True)
