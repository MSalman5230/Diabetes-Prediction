<h1>Predicting Diabetes: A Machine Learning Approach</h1>

Live Demo:https://PredictDiabetes.msalman.de
# Information
1. Exploratory Data Analysis (EDA) with Seaborn, and UMAP for (Uniform Manifold Approximation and Projection)for visualizing high-dimensional data in a lower-dimensional space
2. XGboost Tuned Hyperparamertes Tuned with Optuna and ML-Flow 
3. Streamlit for webapp


<h1 style="font-size:20px;">About the dataset:</h1>
<ul>
    <li>
        <code>gender</code>: Gender refers to the biological sex of the individual, which can have an impact on their susceptibility to diabetes. There are three categories in it male ,female and other.
    </li>
    <br>
    <li>
        <code>age</code>: Age is an important factor as diabetes is more commonly diagnosed in older adults.Age ranges from 0-80 in our dataset.
    </li>
    <br>
    <li>
        <code>hypertension</code>: Hypertension is a medical condition in which the blood pressure in the arteries is persistently elevated. It has values a 0 or 1 where 0 indicates they don’t have hypertension and for 1 it means they have hypertension.
    </li>
    <br>
    <li>
        <code>heart_disease</code>: Heart disease is another medical condition that is associated with an increased risk of developing diabetes. It has values a 0 or 1 where 0 indicates they don’t have heart disease and for 1 it means they have heart disease.
    </li>
    <br>
    <li>
        <code>smoking_history</code>: Smoking history is also considered a risk factor for diabetes and can exacerbate the complications associated with diabetes.In our dataset we have 5 categories i.e not current,former,No Info,current,never and ever.
    </li>
    <br>
    <li>
        <code>bmi</code>: BMI (Body Mass Index) is a measure of body fat based on weight and height. Higher BMI values are linked to a higher risk of diabetes. The range of BMI in the dataset is from 10.16 to 71.55. BMI less than 18.5 is underweight, 18.5-24.9 is normal, 25-29.9 is overweight, and 30 or more is obese.
    </li>
    <br>
    <li>
        <code>HbA1c_level</code>: HbA1c (Hemoglobin A1c) level is a measure of a person's average blood sugar level over the past 2-3 months. Higher levels indicate a greater risk of developing diabetes. Mostly more than 6.5% of HbA1c Level indicates diabetes.
    </li>
    <br>
    <li>
        <code>blood_glucose_level</code>: Blood glucose level refers to the amount of glucose in the bloodstream at a given time. High blood glucose levels are a key indicator of diabetes.
    </li>
    <br>
    <li>
        <code>diabetes</code>: Diabetes is the target variable being predicted, with values of 1 indicating the presence of diabetes and 0 indicating the absence of diabetes.
    </li>
</ul>
<p>The dataset can be found at <a href='https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset'>https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset</a></p>
<hr>