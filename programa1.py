# mini_chatbot_funcion1.py
import streamlit as st

st.set_page_config(page_title="Chat con análisis básico", layout="centered")

st.title("💬 Mini Chatbot: cuenta palabras y caracteres")
st.write("Escribe algo y te diré cuántas palabras y caracteres tiene.")

# Entrada tipo chat
user_input = st.chat_input("Escribe algo...")

if user_input:
    # Mostrar mensaje del usuario
    st.chat_message("user").write(user_input)

    # Mostrar respuesta del asistente con conteo
    word_count = len(user_input.split())
    char_count = len(user_input)

    st.chat_message("assistant").write(f"📢 Dijiste: {user_input}")
    st.chat_message("assistant").write(f"📝 Tu mensaje tiene {word_count} palabras y {char_count} caracteres.")
