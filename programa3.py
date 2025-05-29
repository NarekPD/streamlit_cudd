import streamlit as st
from openai import OpenAI

def respuesta_gpt_roles(solicitud):
    prompt = solicitud

    # Inicializar el cliente de OpenAI con tu clave de API
    openai_api_key = st.secrets["api_key"] 
    client = OpenAI(api_key=key)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # O el modelo que prefieras, como "gpt-3.5-turbo-16k"
        messages=[
        {"role": "system", "content": "Eres un profesor de fisiología de la facultad de medicina de la Universidad Autonoma de Chihuahua. Respondes via whatsapp, no usas emojis. Tus respuestas son siempre sarcasticas y despectivas. Si tienen mala redaccion, búrlate de su ortografía"},
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
    )
    respuesta = completion.choices[0].message.content.strip()
    return respuesta

# Show title and description.
st.title("💬 Chatbot despectivo")

prompt = st.chat_input("Escribe algo")
if prompt==None:
   st.stop()

with st.chat_message("user",avatar = "🦖"):
   st.markdown(prompt)

# Generate a response using the OpenAI API.

# stream = client.chat.completions.create(
#         model="gpt-4o-mini",  
#         messages=[
#             {"role": "system", "content": "You are an assistant."},
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens=800,
#         temperature=0.75,
#     )

# respuesta = stream.choices[0].message.content

respuesta = respuesta_gpt_roles(solicitud)

with st.chat_message("assistant"):
   st.write(respuesta)
