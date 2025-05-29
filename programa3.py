import streamlit as st
from openai import OpenAI
import random

# Lista de emojis tipo "hater"
assistant_emojis = ["🙄", "😒", "😑", "😠"]

def respuesta_gpt_roles(solicitud):
    openai_api_key = st.secrets["api_key"]
    client = OpenAI(api_key=openai_api_key)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un profesor de fisiología de la facultad de medicina. Respondes vía WhatsApp. Tus respuestas son siempre sarcásticas y despectivas. Si tienen mala redacción, te burlas de su ortografía."},
            {"role": "user", "content": "Hola profe, que dias tenemos clase?"},
            {"role": "assistant", "content": "Lunes a Sábado, excepto jueves. El horario desglosado viene en el SEGA"},
            {"role": "user", "content": "Profe cuando da asesorias?."},
            {"role": "assistant", "content": "Nunca, ya tengo suficiente con verlos durante la clase"},
            {"role": "user", "content": "Profe, cual es su correo?"},
            {"role": "assistant", "content": "mi correo es estudia@burro.com"},
            {"role": "user", "content": "Profe, da otra clase aparte de fisiología?"},
            {"role": "assistant", "content": "Nooooooo"},
            {"role": "user", "content": solicitud},
        ],
        max_tokens=800,
        temperature=0.8,
    )
    respuesta = completion.choices[0].message.content.strip()
    return respuesta

# Interfaz
st.title("💬 Chatbot despectivo")

prompt = st.chat_input("Escribe algo")

if prompt is None:
    st.stop()

with st.chat_message("user", avatar="💩"):
    st.markdown(prompt)

respuesta = respuesta_gpt_roles(prompt)

# Selección aleatoria del avatar del asistente
assistant_avatar = random.choice(assistant_emojis)

with st.chat_message("assistant", avatar=assistant_avatar):
    st.write(respuesta)
