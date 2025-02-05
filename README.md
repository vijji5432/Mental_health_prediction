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
├── 📄 mental_health_analysis.ipynb <- Google Colab notebook for model training
├── 📄 streamlit_ui.py          <- Streamlit-based web UI
├── 📄 predict_mental_health.py <- Command-line script for model inference
├── 📄 mental_health_model.pkl  <- Saved trained model
├── 📄 LLM_experimentation.pdf  <- (Optional) Report on LLM explanations
└── 🎥 demo.mp4                 <- Video walkthrough
```

## 🛠 Installation
To set up the project, follow these steps:

1️⃣ **Clone the repository:**
```bash
git clone https://github.com/yourusername/mental_health_project.git
cd mental_health_project
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
streamlit run streamlit_ui.py
```

### 🔹 **Run Inference via CLI**
Use the command-line script for predictions:
```bash
python predict_mental_health.py
```
Follow the prompts to enter your details and receive predictions.

## 📊 Model Evaluation
- Model: **Random Forest Classifier**
- Metrics: **Accuracy, Precision, Recall, F1-score**
- Feature importance analyzed using **SHAP**

## 🎥 Video Demonstration
Watch the walkthrough of the project: [`demo.mp4`]

## 🏗 Future Improvements
- Experiment with other models (XGBoost, Neural Networks)
- Improve UI with more interactivity
- Integrate LLM for better explanations

---
📧 **For inquiries:** Contact vijjialekhya@gmail.com or visit vijji5432 .


