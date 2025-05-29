def respuesta_gpt_roles(solicitud):
    prompt = solicitud

    # Inicializar el cliente de OpenAI con tu clave de API
    client = OpenAI(api_key=key)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # O el modelo que prefieras, como "gpt-3.5-turbo-16k"
        messages=[
        {"role": "system", "content": "Eres un profesor de fisiología de la facultad de medicina de la Universidad Autonoma de Chihuahua. Respondes via whatsapp, no usas emojis. Tus respuestas son despectivas. Si tienen mala redaccion, búrlate sarcasticamente de su ortografía"},
        {"role": "user", "content": "Hola profe, que dias tenemos clase?"},
        {"role": "assistant", "content": "Lunes a Sábado, excepto jueves. El horario desglosado viene en el SEGA"},
        {"role": "user", "content": "Profe cuando da asesorias?."},
        {"role": "assistant", "content": "Nunca, ya tengo suficiente con verlos durante la clase"},
        {"role": "user", "content": "Profe, cual es su correo?"},
        {"role": "assistant", "content": "mi correo es nplamenov@uach.mx"},
        {"role": "user", "content": "Profe, da otra clase aparte de fisiología?"},
        {"role": "assistant", "content": "Nooooooo"},
        {"role": "user", "content": prompt},
        ],
        max_tokens=800,
        temperature=0.75
    )
    respuesta = completion.choices[0].message.content.strip()
    return respuesta

import streamlit as st
from openai import OpenAI

# Función que genera la respuesta del chatbot
def respuesta_gpt_roles(prompt):
    # Aquí podrías usar OpenAI, HuggingFace, o cualquier modelo local
    # Por ahora, es un placeholder que simula una respuesta
    return f"Simulación de respuesta para: '{prompt}'"

# Título de la app
st.title("💬 Chatbot despectivo")

# Entrada del usuario en forma de chat
user_input = st.chat_input("Escribe algo...")

# Si hay entrada del usuario
if user_input:
    # Mostrar el mensaje del usuario
    st.chat_message("user", avatar="🦖").write(user_input)

    # Obtener respuesta usando la función personalizada
    respuesta = respuesta_gpt_roles(user_input)

    # Mostrar la respuesta del asistente
    st.chat_message("assistant").write(respuesta)
