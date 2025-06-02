# 🌾 Predicting Crop Production Based on Agricultural Data

## 📌 Project Overview

This project aims to predict **crop production (in tons)** using regression models based on features like **area harvested (in hectares)**, **yield (in kg/ha)**, and **year**. Accurate predictions can assist in planning, policy-making, and optimizing agricultural operations.

## 🌍 Domain

**Agriculture**

## 🎯 Problem Statement

Agriculture is vital to the economy. Accurate crop production forecasts are essential for food security, planning, and policy-making. This project builds a regression-based predictive model using agricultural data.

## 💼 Business Use Cases

* **Food Security & Planning**: Help governments and NGOs prepare for demand.  
* **Policy Development**: Inform agricultural subsidies, insurance, and relief efforts.  
* **Supply Chain Optimization**: Improve logistics for agribusinesses.  
* **Market Price Forecasting**: Assist farmers and traders in market planning.  
* **Precision Farming**: Guide crop selection and resource usage.  
* **Agri-Tech Tools**: Support development of smart farming solutions.

## 🤉 Project Approach

### 1️⃣ Data Preprocessing

* Handle missing values  
* Standardize metrics and filter relevant features

### 2️⃣ Exploratory Data Analysis (EDA)

* Analyze crop and region distributions  
* Identify trends over time  
* Study correlations between yield, area, and production  
* Detect outliers and anomalies

### 🔍📊 Types of Analysis – Key Highlights

- 🌾 Analyzed crop types and regional distribution to identify major crops and agricultural hotspots.  
- 📅 Examined yearly trends and growth patterns in area harvested, yield, and production.  
- 🌱 Explored relationships between area harvested and yield to infer resource utilization impact.  
- 🔗 Studied correlations between area, yield, and production to understand productivity.  
- 📊 Compared yields and production across crops and regions to identify high-performing ones.  
- 🚨 Detected outliers and anomalies to highlight unusual production or yield values.

### 3️⃣ Predictive Modeling

* Train regression models (e.g., Linear Regression, Random Forest)  
* Predict total **crop production** based on input features  
* Evaluate model performance using metrics like R², MAE, RMSE  

### 4️⃣ Streamlit Web App

* Interactive app for real-time crop production prediction  
* User inputs: crop, region, area, yield, year  
* Output: predicted production value
  
## 📊 4️⃣ Visualization

- 📍 Create interactive visuals using **Plotly**, **Streamlit**, or **Power BI**.
- 📉 Dynamic scatter plots and bar charts for species distribution.

## ✅ Outcomes

* Discover trends in crop yield and productivity  
* Build accurate models for production forecasting  
* Provide actionable insights for agriculture planning  
* Deliver a user-friendly interface via Streamlit  

---

## 🧰 Skills & Technologies

### 🖥️ Programming & Tools
- **Languages:** Python  
- **Libraries:** `pandas`, `matplotlib`, `plotly` ,  
- **Databases:** PostgreSQL, MySQL  
- **BI Tools:** Power BI

### 🔧 Data Science Skills
- 🧹 **Data Cleaning**
- 🔄 **Data Preprocessing**
- 📊 **Exploratory Data Analysis (EDA)**
- 📈 **Data Visualization** (Matplotlib, Plotly, Power BI)
- **Machine Learning (Regression)**
- **Streamlit App Development**

---


## ✨ Demo & Usage

    1. Fetch the uncleaned dataset (in `.xlsx` format) and perform data cleaning.  
    2. Execute `Data_Transformation_Cleaning_Preprocessing_Handling.ipynb` and `Crop_Production_EDA.ipynb`.  
    3. Execute `Crop_Production_Model.ipynb` containing two models:  
       - Linear Regression  
       - Random Forest Regressor  
    4. Run `Streamlit.py` to check live predictions.


##  PowerBi Report: 
[https://app.powerbi.com/view?r=eyJrIjoiNDJmYjk2MTAtNWE2Yi00N2EwLWIzYTItNzJjOGUyY2UyNzZlIiwidCI6IjczY2UwZTg5LWRjMzUtNGExMC04NTMxLTFjYzJmMTgxNTUyZCJ9&embedImagePlaceholder=true](https://app.powerbi.com/view?r=eyJrIjoiNDJmYjk2MTAtNWE2Yi00N2EwLWIzYTItNzJjOGUyY2UyNzZlIiwidCI6IjczY2UwZTg5LWRjMzUtNGExMC04NTMxLTFjYzJmMTgxNTUyZCJ9&embedImagePlaceholder=true)

**Streamlit Web App:** [https://predicting-crop-given-based-on-agricultural-data.streamlit.app/](https://predicting-crop-given-based-on-agricultural-data.streamlit.app/)
