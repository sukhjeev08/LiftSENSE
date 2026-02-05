# LiftSENSE
A data-driven platform that estimates fat percentage and provides workout and calorie recommendations using physiological inputs.

## 🚀 Features
- Body fat percentage prediction using ML regression
- Workout focus recommendation (Cardio / Strength / Balanced)
- Calorie goal recommendation (Deficit / Maintenance / Bulk)
- Interactive Streamlit UI

## 🧠 Tech Stack
- Python
- scikit-learn
- pandas
- Streamlit

## 📊 Machine Learning Details
- Models evaluated: Linear Regression, Random Forest, Gradient Boosting
- Final model: Random Forest Regressor
- Evaluation metrics: MAE, R²
- Feature engineering: BMI, workout frequency, experience level
- Pipeline used to avoid data leakage

## 📊 Model Accuracy Summary

| Model               |R^2 Score | Mean Average Error|
|--------------------|-------------------|------------|
| Linear Regression   | 0.624           |3.200|
| Gradient Boosting   | 0.795        |2.391|
| Random Forest       | 0.804           |2.323|

## 💬 Feedback

I’m still learning, and feedback is always welcome!  
Feel free to open an issue or share suggestions to help improve this project.

---

## ⭐ Credits

Dataset source: Kaggle  
Notebook created with ❤️ as part of my Data Science learning journey.
