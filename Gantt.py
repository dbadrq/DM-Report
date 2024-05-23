import pandas as pd
import matplotlib.pyplot as plt

# Define project phases, tasks, and durations in weeks
tasks = [
    {"Task": "Define research goals", "Phase": "Business Understanding", "Start Week": 1, "Duration (weeks)": 1},
    {"Task": "Assess influence of factors", "Phase": "Business Understanding", "Start Week": 1, "Duration (weeks)": 1},
    {"Task": "Evaluate random forest feasibility", "Phase": "Business Understanding", "Start Week": 2, "Duration (weeks)": 1},
    {"Task": "Formulate problem statement", "Phase": "Business Understanding", "Start Week": 2, "Duration (weeks)": 1},
    {"Task": "Set research objectives", "Phase": "Business Understanding", "Start Week": 2, "Duration (weeks)": 1},

    {"Task": "Collect initial data", "Phase": "Data Understanding", "Start Week": 3, "Duration (weeks)": 1},
    {"Task": "Describe data", "Phase": "Data Understanding", "Start Week": 3, "Duration (weeks)": 1},
    {"Task": "Explore data with Weka", "Phase": "Data Understanding", "Start Week": 4, "Duration (weeks)": 1},
    {"Task": "Analyze text data with SketchEngine", "Phase": "Data Understanding", "Start Week": 4, "Duration (weeks)": 1},
    {"Task": "Clean data with pandas", "Phase": "Data Understanding", "Start Week": 4, "Duration (weeks)": 1},

    {"Task": "Select data", "Phase": "Data Preparation", "Start Week": 5, "Duration (weeks)": 1},
    {"Task": "Clean data", "Phase": "Data Preparation", "Start Week": 5, "Duration (weeks)": 4},
    {"Task": "Construct data", "Phase": "Data Preparation", "Start Week": 9, "Duration (weeks)": 1},
    {"Task": "Integrate data", "Phase": "Data Preparation", "Start Week": 9, "Duration (weeks)": 2},
    {"Task": "Format data", "Phase": "Data Preparation", "Start Week": 11, "Duration (weeks)": 1},
    {"Task": "Visualize data with R", "Phase": "Data Preparation", "Start Week": 11, "Duration (weeks)": 2},

    {"Task": "Select modeling techniques", "Phase": "Modeling", "Start Week": 13, "Duration (weeks)": 1},
    {"Task": "Design tests", "Phase": "Modeling", "Start Week": 13, "Duration (weeks)": 2},
    {"Task": "Build models with Weka", "Phase": "Modeling", "Start Week": 15, "Duration (weeks)": 1},
    {"Task": "Optimize parameters", "Phase": "Modeling", "Start Week": 16, "Duration (weeks)": 1},
    {"Task": "Train models with scikit-learn", "Phase": "Modeling", "Start Week": 17, "Duration (weeks)": 1},
    {"Task": "Refine hypotheses with ChatGPT", "Phase": "Modeling", "Start Week": 17, "Duration (weeks)": 1},
    {"Task": "Analyze models with R", "Phase": "Modeling", "Start Week": 18, "Duration (weeks)": 1},

    {"Task": "Evaluate model results", "Phase": "Evaluation", "Start Week": 19, "Duration (weeks)": 1},
    {"Task": "Review process", "Phase": "Evaluation", "Start Week": 19, "Duration (weeks)": 1},
    {"Task": "Determine next steps", "Phase": "Evaluation", "Start Week": 20, "Duration (weeks)": 1},
    {"Task": "Evaluate metrics with Weka", "Phase": "Evaluation", "Start Week": 20, "Duration (weeks)": 1},
    {"Task": "Verify model performance with SketchEngine", "Phase": "Evaluation", "Start Week": 20, "Duration (weeks)": 1},
    {"Task": "Analyze results with R", "Phase": "Evaluation", "Start Week": 20, "Duration (weeks)": 1},

    {"Task": "Plan deployment", "Phase": "Deployment", "Start Week": 21, "Duration (weeks)": 1},
    {"Task": "Monitor system", "Phase": "Deployment", "Start Week": 21, "Duration (weeks)": 1},
    {"Task": "Maintain system", "Phase": "Deployment", "Start Week": 22, "Duration (weeks)": 1},
    {"Task": "Document project", "Phase": "Deployment", "Start Week": 22, "Duration (weeks)": 1},
    {"Task": "Develop deployment scripts", "Phase": "Deployment", "Start Week": 22, "Duration (weeks)": 1},
    {"Task": "Compile final report", "Phase": "Deployment", "Start Week": 23, "Duration (weeks)": 2}
]

# Convert to DataFrame
df = pd.DataFrame(tasks)

# Create figure and axis
fig, ax = plt.subplots(figsize=(16, 10))

# Define colors for each phase
colors = {
    "Business Understanding": "lightblue",
    "Data Understanding": "lightgreen",
    "Data Preparation": "lightyellow",
    "Modeling": "lightcoral",
    "Evaluation": "lightskyblue",
    "Deployment": "lightpink"
}

# Plot tasks
for i, task in df.iterrows():
    ax.barh(task['Task'], task['Duration (weeks)'], left=task['Start Week'] - 0.5, color=colors[task['Phase']], edgecolor='black')

# Format the x-axis to show weeks in the center of each bar
plt.xticks(range(1, 25))
ax.set_xticks([x + 0.5 for x in range(1, 25)])
ax.set_xticklabels(range(1, 25))

plt.xlabel('Weeks')
plt.ylabel('Tasks')
plt.title('Detailed Gantt Chart for Heart Disease Prediction Project')

# Add legend by phases outside the plot
handles = [plt.Rectangle((0,0),1,1, color=colors[phase]) for phase in colors]
labels = colors.keys()
plt.legend(handles, labels, loc='center left', bbox_to_anchor=(1, 0.5))

# Show grid for better readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Add phase labels to the left of the tasks
current_phase = ""
y_position = 0
for i, task in df.iterrows():
    if task['Phase'] != current_phase:
        ax.text(-3, i, task['Phase'], ha='right', va='center', fontsize=12, fontweight='bold', color=colors[task['Phase']])
        current_phase = task['Phase']
    y_position -= 1

# Show plot
plt.tight_layout()
plt.show()
