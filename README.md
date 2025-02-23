# Student Performance Prediction
The Student Performance Prediction project aims to predict the academic performance of students based on various features such as study hours, attendance, parental education, and more. This predictive model helps in identifying students who may be at risk of underperforming, allowing educators to take early intervention measures.

The project uses machine learning techniques to analyze historical student data and generate predictions for future academic outcomes. By leveraging models such as Decision Trees, Random Forests, and Linear Regression, this project aims to provide an accurate and reliable tool for forecasting student performance.

The objective is not only to predict scores but also to gain insights into the factors that most influence academic success, ultimately contributing to improving educational strategies and outcomes.

## Implementation
**Dependencies:**
* pandas: For data manipulation and analysis.
* scikit-learn: For building machine learning models and performing model evaluation.
* matplotlib: For creating visualizations and charts.
* seaborn: For statistical data visualization.
* numpy: For numerical computing and working with arrays
* catboost
* xgboost
* dill
* flask

**Environ Setup**
1. Create a virtual Environment: conda create -p venv python==2.11 -y || python -m venv environ_name
2. Activate the virtual environment: environ_name\Scripts\Activate
3. Use this command to install the libraries: pip install -r requiements.txt
4. If you'r using your device, install ipykernel and run then run the notebook files.
5. Then have a look at modular coding used for data ingestion, transformation, model training and prediction pipelines
6. Then run python src/components/data_ingestion.py, it will create files such model.pkl, preprocessor.pkl, train and test-csv
7. In the terminal navigate to your project directory and hit the command to run the app: python app.py
8. Open the browser and search for 127.0.0.1:5000/predictdata
9. 
## Project Directories
Here is an overview of the project's directory structure
```
student-performance-prediction/
├── notebooks/                  # Jupyter notebooks for data exploration and analysis
│   └── EDA Student performance.ipynb  # Jupyter notebook for initial data exploration
|   └── Model Training.ipynb 
├── data/                      # Directory containing the dataset(s)
│   └── student_data.csv        # Example CSV file with student data
│
├── src/                        # Source code for the project
│    └──components
|           ├── __init__.py             # Initialize the source code module
│           ├── data_ingestion.py   
│           ├── data_transformation.py  
│           ├── model_trainer.py               # Code for training the machine learning models
│     └──pipeline
|           ├── __init__.py             
│           ├── prediction_pipeline.py
│    └──__init__.py
│    └──exception.py
│    └──logger.py
│    └──utils.py
├── templates/                        
│    └──home.html
├── requirements.txt            # List of required Python dependencies
├── README.md                   # Project documentation (this file)
└── app.py.py           

```
## Usage Instructions
## Features
## Model details
## Tech Stack used
## Credits and Acknowledgements

This project would not have been possible without the guidance, tools, and resources provided by the following:

- **Guidance and Support:**
  - Krish Naik: for project guidance and support.
  - ----------- Name for providing a platform and resources for development.

- **Tools and Libraries:**
  - [Scikit-learn](https://scikit-learn.org/) for data preprocessing, linear regression model and  evaluation.
  - [Pandas](https://pandas.pydata.org/) and [NumPy](https://numpy.org/) for data manipulation and analysis.
  - [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/) for visualization.

- **Dataset:**  
  - The dataset used in this project, `student.csv`, was sourced from [Kaggle](https://www.kaggle.com/).

- **Community and Tutorials:**  
  - Special thanks to the Python and data science community for sharing valuable tutorials and insights.
  - [GitHub](https://github.com/) for version control and collaboration.

---

**Acknowledgement:**  
This project is a result of collaborative learning and the application of knowledge from various online resources, courses, and tutorials. Thank you to everyone who contributed directly or indirectly to its success.
## dataset
## Future Improvements
## Contact Information

If you have any questions, feedback, or collaboration ideas, feel free to reach out:

- **Author:** Allaudin Ansari  
- **Email:** allu456654ansari@gmail.com  
- **GitHub Profile:** [Allaudin Ansari](https://github.com/allu0786ansari)  

For any inquiries related to this project, please don't hesitate to contact me!
## output
![App Screenshot](https://github.com/allu0786ansari/Student_Performance_Prediction/blob/main/output/predicted_output.png)
## Demo
