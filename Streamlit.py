import streamlit as st
import pandas as pd
from joblib import dump
from joblib import load
import pickle


# Title
st.title("🌾 Crop Production Prediction")



# Load encoders
encoders = load("model/encoder.joblib")

# Load random_Forest_regressor_model
rfr = load("C:/Users/dhars/Downloads/Dhass/codeing/GUVI/2. MainBoot/4.Project_Code/Project3/Crop_Production_Prediction/model/random_Forest_regressor_model.joblib")

# Load linear_regression_model
lrr = load("C:/Users/dhars/Downloads/Dhass/codeing/GUVI/2. MainBoot/4.Project_Code/Project3/Crop_Production_Prediction/model/linear_model.joblib")



# Set default values
default_country = sorted(encoders['Country'].classes_)[0]
default_item = sorted(encoders['Item'].classes_)[0]
default_year = 2023
default_area = 37000.0
default_yield = 1810.8

# Initialize session state for reset
if 'reset' not in st.session_state:
    st.session_state.reset = False

# Reset 
def reset_form_rfr():
    st.session_state.Country_rfr = default_country
    st.session_state.Item_rfr = default_item
    st.session_state.Year_rfr = default_year
    st.session_state.Area_harvested_rfr = default_area
    st.session_state.Yield_rfr = default_yield

def reset_form_lr():
    st.session_state.Country_lr = default_country
    st.session_state.Item_lr = default_item
    st.session_state.Year_lr = default_year
    st.session_state.Area_harvested_lr = default_area
    st.session_state.Yield_lr = default_yield




#MAIN TABS
tab1,tab2 = st.tabs(['Random Forest Regressor','Linear Regression'])


with tab1:
  try:
    #Form
    with st.form("prediction_form"):
    # Form fields
      Country = st.selectbox("Select Country", sorted(encoders['Country'].classes_), key="Country_rfr")
      Item = st.selectbox("Select Crop Item", sorted(encoders['Item'].classes_), key="Item_rfr")
      Year = st.selectbox("Select Year", list(range(2019, 2030)), key="Year_rfr")
      Area_harvested = st.number_input("Area Harvested (ha)", min_value=0.0, step=100.0, key="Area_harvested_rfr")
      Yield = st.number_input("Yield (kg/ha)", min_value=0.0, step=100.0, key="Yield_rfr")

      # Buttons
      predict_btn = st.form_submit_button("Predict Production")
      reset_btn = st.form_submit_button("Reset Button", on_click=reset_form_rfr)





    # Display selected inputs in a table
    st.subheader("📋 Selected Input Data")
    input_data = {
        'Country': [Country],
        'Item': [Item],
        'Year': [Year],
        'Area harvested (ha)': [Area_harvested],
        'Yield (kg/ha)': [Yield]
    }
    input_df = pd.DataFrame(input_data)
    st.table(input_df)



    # After form submit
    if predict_btn:
        new_data = {
            'Country': Country,
            'Item': Item,
            'Year': Year,
            'Area harvested (ha)': Area_harvested,
            'Yield (kg/ha)': Yield
        }
        new_df = pd.DataFrame([new_data])

        for col in new_df.columns:
            if col in encoders:
                new_df[col] = encoders[col].transform(new_df[col])

        prediction = rfr.predict(new_df)
        st.success(f"✅ Predicted production is: **{prediction[0]:,.2f} tons - by using random forest regressor model**")

  except Exception as e:
        st.error(f"Failed to fetch data: {e}")




with tab2:
  try:
    #Form
    with st.form("prediction_form2"):
    # Form fields
      Country = st.selectbox("Select Country", sorted(encoders['Country'].classes_), key="Country_lr")
      Item = st.selectbox("Select Crop Item", sorted(encoders['Item'].classes_), key="Item_lr")
      Year = st.selectbox("Select Year", list(range(2019, 2030)), key="Year_lr")
      Area_harvested = st.number_input("Area Harvested (ha)", min_value=0.0, step=100.0, key="Area_harvested_lr")
      Yield = st.number_input("Yield (kg/ha)", min_value=0.0, step=100.0, key="Yield_lr")


      # Buttons
      predict_btn = st.form_submit_button("Predict Production")
      reset_btn = st.form_submit_button("Reset Button", on_click=reset_form_lr)





    # Display selected inputs in a table
    st.subheader("📋 Selected Input Data")
    input_data = {
        'Country': [Country],
        'Item': [Item],
        'Year': [Year],
        'Area harvested (ha)': [Area_harvested],
        'Yield (kg/ha)': [Yield]
    }
    input_df = pd.DataFrame(input_data)
    st.table(input_df)



    # After form submit
    if predict_btn:
        new_data = {
            'Country': Country,
            'Item': Item,
            'Year': Year,
            'Area harvested (ha)': Area_harvested,
            'Yield (kg/ha)': Yield
        }
        new_df = pd.DataFrame([new_data])

        for col in new_df.columns:
            if col in encoders:
                new_df[col] = encoders[col].transform(new_df[col])

        prediction = lrr.predict(new_df)
        st.success(f"✅ Predicted production is: **{prediction[0]:,.2f} tons - by using Linear Regression model**")

  except Exception as e:
        st.error(f"Failed to fetch data: {e}")
