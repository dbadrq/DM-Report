import matplotlib.pyplot as plt
import pygraphviz as pgv

# Define the phases and tasks with colors
phases = {
    "Business Understanding": {
        "tasks": [
            "Define research goals",
            "Assess influence of factors",
            "Evaluate random forest feasibility",
            "Formulate problem statement",
            "Set research objectives"
        ],
        "color": "lightblue"
    },
    "Data Understanding": {
        "tasks": [
            "Collect initial data",
            "Describe data",
            "Explore data with Weka",
            "Analyze text data with SketchEngine",
            "Clean data with pandas"
        ],
        "color": "lightgreen"
    },
    "Data Preparation": {
        "tasks": [
            "Select data",
            "Clean data",
            "Construct data",
            "Integrate data",
            "Format data",
            "Visualize data with R"
        ],
        "color": "lightyellow"
    },
    "Modeling": {
        "tasks": [
            "Select modeling techniques",
            "Design tests",
            "Build models with Weka",
            "Optimize parameters",
            "Train models with scikit-learn",
            "Refine hypotheses with ChatGPT",
            "Analyze models with R"
        ],
        "color": "lightcoral"
    },
    "Evaluation": {
        "tasks": [
            "Evaluate model results",
            "Review process",
            "Determine next steps",
            "Evaluate metrics with Weka",
            "Verify model performance with SketchEngine",
            "Analyze results with R"
        ],
        "color": "lightskyblue"
    },
    "Deployment": {
        "tasks": [
            "Plan deployment",
            "Monitor system",
            "Maintain system",
            "Document project",
            "Develop deployment scripts",
            "Compile final report"
        ],
        "color": "lightpink"
    }
}

# Function to draw each phase
def draw_phase(phase, data):
    G = pgv.AGraph(directed=True)
    G.add_node(phase, shape='box', style='filled', fillcolor=data['color'])
    for task in data['tasks']:
        G.add_node(task, shape='ellipse', style='filled', fillcolor=data['color'])
        G.add_edge(phase, task)

    # Draw the graph
    G.layout(prog='dot')
    filename = f"{phase.replace(' ', '_')}.png"
    G.draw(filename)

    # Display the graph
    img = plt.imread(filename)
    plt.figure(figsize=(10, 6))
    plt.imshow(img)
    plt.axis('off')
    plt.title(phase, fontsize=15)
    plt.show()

# Draw each phase
for phase, data in phases.items():
    draw_phase(phase, data)
