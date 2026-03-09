# 📞 Telco Customer Churn Prediction (End-to-End)

## 📌 Project Overview
Customer retention is crucial for telecommunication companies. This end-to-end Machine Learning project predicts customer churn based on their demographic data, account information, and service usage. It includes an interactive Web App built with Streamlit.

## 🛠️ Tech Stack
- **Data Manipulation:** Python (Pandas, NumPy)
- **Machine Learning:** Scikit-learn (Random Forest Classifier)
- **Web App / Deployment:** Streamlit
- **Visualization:** Matplotlib, Seaborn

## 📊 Key Insights (EDA)
1. **Tenure & Churn:** Customers with less than 6 months of tenure have the highest churn rate. Retention strategies should focus on onboarding.
2. **Contract Type:** Month-to-month contracts are highly correlated with churn compared to 1-year or 2-year contracts.
3. **Monthly Charges:** High monthly charges (especially with Fiber Optic service) show a higher probability of churning.

## 💻 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/Telco-Churn-Prediction.git](https://github.com/your-username/Telco-Churn-Prediction.git)# TelcoCustomerChurn

2. Install the required packages:
   ```bash
   pip install -r requirements.txt

3. Run the Streamlit app:
   ```bash
   streamlit run app.py

## 📈 Model Performance
Algorithm Used: Random Forest Classifier

Accuracy: ~79%

Actionable Output: The model outputs a Churn Probability Score, allowing the business team to prioritize high-risk customers for targeted marketing campaigns.
