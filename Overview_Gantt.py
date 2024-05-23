import matplotlib.pyplot as plt
import pandas as pd

# Define the tasks and their start/end weeks
tasks = {
    'Business Understanding': [1, 2],
    'Data Understanding': [3, 4],
    'Data Preparation': [5, 12],
    'Modeling': [13, 18],
    'Evaluation': [19, 20],
    'Deployment': [21, 24]
}

# Convert to DataFrame
df = pd.DataFrame(tasks, index=['Start', 'End']).T

# Calculate duration
df['Duration'] = df['End'] - df['Start'] + 1

# Create the Gantt chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars
for i, task in enumerate(df.index):
    ax.barh(task, df.loc[task, 'Duration'], left=df.loc[task, 'Start'], align='center')

# Add labels and grid
ax.set_xlabel('Weeks')
ax.set_ylabel('Tasks')
ax.set_title('Gantt Chart for Research Project')
ax.grid(True)

# Annotate bars with start and end weeks
for i, task in enumerate(df.index):
    ax.text(df.loc[task, 'Start'], i, f'Start: {df.loc[task, "Start"]}', va='center', ha='right', color='white')
    ax.text(df.loc[task, 'End'], i, f'End: {df.loc[task, "End"]}', va='center', ha='left', color='black')

# Display the chart
plt.tight_layout()
plt.show()
