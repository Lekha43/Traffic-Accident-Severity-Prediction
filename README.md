 Traffic Accident Severity Prediction Dashboard

 1. Project Overview

The Traffic Accident Severity Prediction Dashboard is a Python-based desktop application that analyzes traffic accident data and predicts accident severity based on weather conditions, road type, time of accident, and accident history.

The project uses Machine Learning to classify accidents into three categories:

- Minor
- Moderate
- Severe

The dashboard provides accident statistics, graphical analysis, and a prediction feature through a simple graphical user interface.

 2. Objectives

- Analyze traffic accident data.
- Identify accident severity patterns.
- Study the relationship between weather and accident severity.
- Analyze accidents based on road type.
- Predict accident severity using a Decision Tree Classifier.
- Display accident information using graphs and dashboard summary cards.

 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data handling and analysis |
| Matplotlib | Graph visualization |
| Scikit-learn | Machine Learning model |
| Tkinter | Desktop dashboard interface |

 4. Features

Accident Summary: Displays total, minor, moderate, and severe accidents.
Severity Prediction: Predicts accident severity using selected input conditions.
Weather Analysis:Visualizes accident severity across different weather conditions.
Road Type Analysis: Compares accidents on urban, highway, and rural roads.
Severity Graph: Displays the distribution of accident severity.
Dataset Viewer: Displays the accident dataset in a table.

 5. Project Structure

Traffic-Accident-Severity-Prediction/
│
├── accident_dashboard.py
├── README.md
└── requirements.txt

 6. Installation

Step 1: Install Python

Install Python 3 from the official website:

https://www.python.org/

Step 2: Install Required Libraries

Open the VS Code terminal and execute:

pip install pandas matplotlib scikit-learn

Tkinter is included with most standard Windows Python installations.

 7. How to Run

1. Open the project folder in Visual Studio Code.
2. Save the Python program as `accident_dashboard.py`.
3. Open the terminal.
4. Execute the following command:

python accident_dashboard.py

5. The Traffic Accident Severity Dashboard will open.

 8. How to Use the Dashboard

1. View the accident summary cards.
2. Select the weather condition.
3. Select the road type.
4. Select the time of accident.
5. Select the accident history level.
6. Click Predict Severity to display the predicted accident severity.
7. Click the graph buttons to analyze accident patterns.
8. Click View Dataset to display the accident records.

 9. Machine Learning Method

The project uses a Decision Tree Classifier.

 Input Features

- Weather
- Road Type
- Time
- Accident History

 Output

Predicted accident severity:

- Minor
- Moderate
- Severe

 10. Graphs

The dashboard includes:

1. Accident Severity Distribution
2. Weather vs Accident Severity
3. Road Type vs Accident Severity

These graphs help visualize accident patterns and compare severity across different conditions.

 11. Sample Prediction

Input:

| Feature          | Value   |
| Weather          | Rainy   |
| Road Type        | Highway |
| Time             | Night   |
| Accident History | High    |

Output:

Predicted Accident Severity: Severe

The output is an illustrative prediction from the sample dataset.

 12. Limitations

- The project currently uses a small, manually created sample dataset.
- Predictions are intended for educational demonstration only.
- Model predictions are not reliable for real-world accident safety decisions.
- The prediction model should be trained and evaluated using a larger, representative real-world accident dataset for practical applications.


