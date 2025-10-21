# app.py
import streamlit as st
import pandas as pd
import joblib
import os
import plotly as plt

st.title("Previsão de APGAR5")

# -----------------
# Carregar modelo treinado
# -----------------
model_path = os.path.join("models", "lgbm_apgar5_model_001.pkl")
model = joblib.load(model_path)
# -----------------
# Inputs do usuário
# -----------------
features = ['PESO', 'CONSPRENAT', 'SEMAGESTAC', 'APGAR1', 'TPROBSON', 'KOTELCHUCK']
categorical_cols = ['TPROBSON', 'KOTELCHUCK']

# Valores válidos para as categorias
tp_values = [1,2,3,4,5,6,7,8,10,11]      
kotel_values = [1,2,3,4,5]              

inputs = {}
for f in features:
    if f == 'TPROBSON':
        inputs[f] = st.selectbox(f"Selecione {f}", tp_values, index=4)
    elif f == 'KOTELCHUCK':
        inputs[f] = st.selectbox(f"Selecione {f}", kotel_values, index=4)
    else:
        # Limites baseados no dataset original
        if f == 'PESO':
            min_val, max_val, default_val = 500, 5000, 3000
        elif f == 'CONSPRENAT':
            min_val, max_val, default_val = 1, 12, 8
        elif f == 'SEMAGESTAC':
            min_val, max_val, default_val = 20, 45, 39
        elif f == 'APGAR1':
            min_val, max_val, default_val = 0, 10, 8
        inputs[f] = st.number_input(f"Digite {f}", min_value=min_val, max_value=max_val, value=default_val)

# -----------------
# Criar DataFrame
# -----------------
input_df = pd.DataFrame([list(inputs.values())], columns=features)

# -----------------
# Corrigir tipos categóricos
# -----------------
for col in categorical_cols:
    input_df[col] = input_df[col].astype('category')

# -----------------
# Previsão
# -----------------
pred = model.predict(input_df)

st.subheader(f"Previsão de APGAR5: {pred[0]:.2f}")