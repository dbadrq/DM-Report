# Predicting Heart Disease Using Data Mining Techniques

## Project Overview
This project aims to predict heart disease using data mining techniques, specifically employing the Random Forest algorithm. The dataset used is a composite of five well-known heart disease datasets from Kaggle, consisting of 1190 individual records and 11 essential variables for prognostic assessments. The study assesses the influence of various factors, including age and gender, on the likelihood of acquiring heart disease and evaluates the comparative significance of these characteristics in forecasting cardiac disease.

## Table of Contents
- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Methodology](#methodology)
- [Results](#results)
- [Files and Scripts](#files-and-scripts)
- [Usage Instructions](#usage-instructions)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Objectives
1. To assess the influence of different factors, including age, gender, and other clinical attributes, on the likelihood of acquiring heart disease.
2. To build a precise predictive model using the Random Forest algorithm to evaluate heart disease risk.
3. To provide practical insights directly implementable in clinical environments through data-driven healthcare approaches.

## Methodology
The project follows the CRISP-DM methodology, consisting of the following phases:
1. **Business Understanding**: Define research goals and objectives, assess the feasibility of using the Random Forest algorithm.
2. **Data Understanding**: Collect and explore the dataset, perform initial data analysis using tools like Weka and SketchEngine.
3. **Data Preparation**: Select, clean, construct, integrate, and format the data for modeling.
4. **Modeling**: Build and optimize predictive models using Weka and scikit-learn, refine hypotheses with ChatGPT, and analyze models with R.
5. **Evaluation**: Assess model results, review the process, determine next steps, and verify model performance using various tools.
6. **Deployment**: Plan deployment, monitor and maintain the system, document the project, and develop deployment scripts.

## Results
- The Random Forest model achieved an accuracy of approximately 93% in predicting heart disease.
- Feature importance analysis indicated that factors such as ST slope, type of chest pain, and cholesterol level were significant predictors of heart disease.
- The model's predictive performance and feature importance insights provide valuable information for clinical decision-making and public health policy.

## Files and Scripts
- `forecast.py`: Script for training and evaluating the Random Forest model on the heart disease dataset.
- `Gantt.py`: Script for generating a detailed Gantt chart for the project timeline.
- `Overview_Gantt.py`: Script for generating a Gantt chart for an overview of the project schedule.
- `WBS.py`: Script for creating a Work Breakdown Structure (WBS) of the project phases and tasks.

## Usage Instructions
### Prerequisites
- Python 3.x
- Required Python libraries: pandas, scikit-learn, matplotlib, seaborn, pygraphviz

### Setup
1. Clone the repository:

2. Install the required libraries:
    ```bash
    pip install pandas scikit-learn matplotlib seaborn pygraphviz
    ```

### Running the Scripts
1. **Train and Evaluate the Model**:
    ```bash
    python forecast.py
    ```
    This script will train the Random Forest model, evaluate its performance, and generate visualizations for the confusion matrix and feature importance.

2. **Generate the Gantt Chart**:
    ```bash
    python Gantt.py
    ```
    This script will create a detailed Gantt chart illustrating the project timeline.

3. **Generate the Gantt Chart**:
    ```bash
    python Overview_Gantt.py
    ```
    This script will create an overview Gantt chart illustrating the project timeline.

4. **Create the Work Breakdown Structure (WBS)**:
    ```bash
    python WBS.py
    ```
    This script will generate visual representations of the project phases and tasks.

## Project Structure
./
├── README.md
├── forecast.py
├── Gantt.py
├── Overview_Gantt.py
├── WBS.py

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or additions.
