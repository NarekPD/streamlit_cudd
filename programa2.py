# imc_calculadora.py
import streamlit as st

st.set_page_config(page_title="Calculadora de IMC", layout="centered")
st.title("🧮 Calculadora de IMC")

st.write("Introduce tus datos para calcular tu Índice de Masa Corporal (IMC):")

# Entradas del usuario con valores por defecto
peso = st.number_input("Peso (kg):", min_value=0.0, step=0.1, value=70.0)
estatura = st.number_input("Estatura (m):", min_value=0.0, step=0.01, value=1.70)

# Cálculo del IMC
if peso > 0 and estatura > 0:
    imc = peso / (estatura ** 2)
    st.success(f"✅ Tu IMC es: {imc:.2f}")

    # Clasificación según la OMS
    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 24.9:
        categoria = "Peso normal"
    elif imc < 29.9:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"

    st.info(f"📊 Clasificación: **{categoria}**")
else:
    st.warning("Pedazo de animal, lograste confundir a una inteligencia artificial con tu 'inteligencia' personal")
