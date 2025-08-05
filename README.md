# Onboarding Training Compliance Tracker

This project is a Streamlit dashboard for analyzing onboarding training compliance, feedback, buddy assignment, and satisfaction.

## Overview

This project is a Streamlit-based interactive dashboard for analyzing onboarding training compliance, feedback, buddy assignment, and employee satisfaction. It uses Python, SQL (SQLite), and Plotly for data processing and visualization.

## Features

- **Filterable Dashboard:** Select departments and locations to view targeted insights.
- **Completion Rates by Department:** Interactive bar chart showing training module completion rates by department.
- **Manager Feedback vs. Modules Completed:** Interactive scatter plot visualizing feedback scores against modules completed.
- **Compliance vs. Satisfaction by Location:** Interactive heatmap showing compliance rates and satisfaction scores by location.
- **Buddy Assignment Impact:** Table showing average feedback and satisfaction scores for employees with and without buddies.
- **Module Completion by Department and Location:** Grouped bar chart showing completion rates for all modules by department and location.
- **Module Completion Trend by Start Date:** Line chart showing completion trends for all modules over time.

## How to Run

1. **Install dependencies:**
   ```bash
   pip install streamlit pandas numpy matplotlib seaborn plotly pillow
   ```
2. **Start the dashboard:**
   ```bash
   streamlit run onboarding_dashboard.py
   ```
3. **Interact with the dashboard:**
   - Use the sidebar to filter by department and location.
   - Explore all interactive charts and tables.

## Data

- The dashboard uses `onboarding_training_dataset.csv` as the source data.
- Data is cleaned and stored in a local SQLite database for analysis.

## File Structure

- `onboarding_dashboard.py`: Main Streamlit dashboard app.
- `onboarding_training_dataset.csv`: Onboarding data file.
- `onboarding_compliance.db`: SQLite database (auto-generated).
- `README.md`: Project documentation.

## Screenshots

To display PNG images in your README:

1. Run the dashboard and use your OS screenshot tool to capture each chart/table.
2. Save images in the `screenshots/` folder in your project directory.
3. Use the following links to display images:

```
### Completion Rates by Department (Bar Chart)
[Department Completion](screenshots/department_completion.png)

### Manager Feedback vs. Modules Completed (Scatter Plot)
![Feedback vs Modules](screenshots/feedback_vs_modules.png)

### Compliance vs. Satisfaction by Location (Heatmap)
![Compliance vs Satisfaction](screenshots/compliance_vs_satisfaction.png)

### Buddy Assignment Impact (Table)
![Buddy Impact](screenshots/buddy_impact.png)

### Module Completion by Department and Location (Grouped Bar Chart)
![Module Completion Grouped Bar](screenshots/module_completion_grouped_bar.png)

### Module Completion Trend by Start Date (Line Chart)
![Module Completion Trend](screenshots/module_completion_trend.png)
```

> **Note:** PNG images will only display if they exist in the specified folder and are not empty. If viewing on GitHub, ensure you commit the images to your repository.

## License

This project is for educational and internal use. Modify and extend as needed.
