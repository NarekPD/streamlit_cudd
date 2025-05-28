# mini_chatbot_sentimiento.py
import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Chat con análisis", layout="centered")

st.title("🧠 Mini Chatbot con funciones de análisis")
st.write("Este bot repite tu mensaje, cuenta palabras y caracteres, y evalúa el sentimiento.")

# Entrada tipo chat
user_input = st.chat_input("Escribe algo...")

if user_input:
    # Mostrar el mensaje del usuario
    st.chat_message("user").write(user_input)

    # Repetir mensaje
    st.chat_message("assistant").write(f"📢 Dijiste: {user_input}")

    # Función 1: Contar palabras y caracteres
    word_count = len(user_input.split())
    char_count = len(user_input)
    st.chat_message("assistant").write(f"📝 Palabras: {word_count}, Caracteres: {char_count}")

    # Función 3: Análisis de sentimiento
    analysis = TextBlob(user_input)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "positivo 😊"
    elif polarity < 0:
        sentiment = "negativo 😟"
    else:
        sentiment = "neutral 😐"

    st.chat_message("assistant").write(f"🔍 Sentimiento detectado: **{sentiment}**")
