# 🧠 Abuzzz!!! Depression Detection App

A machine learning-based web application that helps users self-assess their mental health by answering a few lifestyle-related questions. It uses a trained Random Forest model to estimate the likelihood of depression based on factors like sleep, social activity, and energy levels.

---

## 🚀 Features

- Predicts likelihood of depression based on simple lifestyle questions
- Real-time prediction using a trained Random Forest Classifier
- Clean, interactive interface using Streamlit
- Probability score shown for awareness
- Friendly suggestions based on prediction

---

## 🧠 Model Details

- **Algorithm**: Random Forest Classifier  
- **Input Features**:
  - Daily Sleep Hours
  - Sadness Level
  - Social Activity Level
  - Energy Level
- **Output**: Depression likelihood (binary: 0 = No Depression, 1 = Possible Depression)
- **Model File**: `model.pkl`

---

## 📊 Dataset

- **File**: `depression_data.csv`
- **Format**: CSV
- **Target Column**: `depression` (0 or 1)
- **Split**: 80% training / 20% testing

---

## 🛠️ Tech Stack

- Python 3
- pandas, numpy
- scikit-learn
- Streamlit
- pickle

---

## 🖥️ How to Run the App Locally

### 1. Clone the Repo
```bash
git clone https://github.com/abubaker05/Abuzzz_Depression_Detection.git
cd Abuzzz_Depression_Detection.git
