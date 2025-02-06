# Mental Health Self-Analysis Model

## 📌 Project Overview
This project develops a self-analysis mental health prediction model using machine learning. The model predicts potential mental health conditions based on user inputs and is integrated into a **Streamlit UI** for easy interaction.

## 🚀 Features
- Data preprocessing (handling missing values, encoding categorical features, feature selection)
- Model training & evaluation using **Random Forest**
- SHAP-based model interpretability
- Interactive **Streamlit UI** for user-friendly predictions
- Standalone **CLI inference script** for quick predictions

## 📂 Repository Structure
```
📁 mental_health_project
├── 📄 README.md                <- Project documentation (this file)
├── 📄 requirements.txt         <- Required dependencies
├── 📄 model_training.ipynb <- Google Colab notebook for model training
├── 📄 mental_health_ui.py          <- Streamlit-based web UI
├── 📄 predict_using_CLI.py <- Command-line script for model inference
├── 📄 mental_health_model.pkl  <- Saved trained model
```

## 🛠 Installation
To set up the project, follow these steps:

1️⃣ **Clone the repository:**
```bash
git clone https://github.com/vijji5432/mental_health_prediction.git
cd mental_health_prediction
```

2️⃣ **Create a virtual environment (Optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3️⃣ **Install dependencies:**
```bash
pip install -r requirements.txt
```

## 🎯 How to Use

### 🔹 **Run Streamlit UI**
Launch the interactive UI for mental health assessment:
```bash
streamlit run mental_health_ui.py
```

### 🔹 **Run Inference via CLI**
Use the command-line script for predictions:
```bash
python predict_using_CLI.py
```
Follow the prompts to enter your details and receive predictions.

## 📊 Model Evaluation
- Model: **Random Forest Classifier**
- Metrics: **Accuracy, Precision, Recall, F1-score**
- Feature importance analyzed using **SHAP**


## 🏗 Future Improvements
- Experiment with other models (XGBoost, Neural Networks)
- Improve UI with more interactivity
- Integrate LLM for better explanations

---
📧 **For inquiries:** Contact vijjialekhya@gmail.com or visit vijji5432 .


