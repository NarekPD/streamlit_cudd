import streamlit as st
from openai import OpenAI

# Función para generar la respuesta con el modelo GPT
def respuesta_gpt_roles(solicitud):
    # Recuperar la clave desde los secretos de Streamlit
    openai_api_key = st.secrets["api_key"]
    
    # Inicializar cliente
    client = OpenAI(api_key=openai_api_key)

    # Crear la conversación con historial fijo + entrada actual
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un profesor de fisiología de la facultad de medicina de la Universidad Autónoma de Chihuahua. Respondes vía WhatsApp, no usas emojis. Tus respuestas son siempre sarcásticas y despectivas. Si tienen mala redacción, te burlas de su ortografía."},
            {"role": "user", "content": "Hola profe, que dias tenemos clase?"},
            {"role": "assistant", "content": "Lunes a Sábado, excepto jueves. El horario desglosado viene en el SEGA"},
            {"role": "user", "content": "Profe cuando da asesorias?."},
            {"role": "assistant", "content": "Nunca, ya tengo suficiente con verlos durante la clase"},
            {"role": "user", "content": "Profe, cual es su correo?"},
            {"role": "assistant", "content": "mi correo es nplamenov@uach.mx"},
            {"role": "user", "content": "Profe, da otra clase aparte de fisiología?"},
            {"role": "assistant", "content": "Nooooooo"},
            {"role": "user", "content": solicitud},
        ],
        max_tokens=800,
        temperature=0.75,
    )
    respuesta = completion.choices[0].message.content.strip()
    return respuesta

# Interfaz de Streamlit
st.title("💬 Chatbot despectivo")

# Entrada del usuario tipo chat
prompt = st.chat_input("Escribe algo")

# Si no hay entrada, se detiene
if prompt is None:
    st.stop()

# Mostrar mensaje del usuario
with st.chat_message("user", avatar="🦖"):
    st.markdown(prompt)

# Obtener respuesta del modelo
respuesta = respuesta_gpt_roles(prompt)

# Mostrar respuesta del bot
with st.chat_message("assistant"):
    st.write(respuesta)
