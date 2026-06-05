import streamlit as st

st.header('Lanzar una moneda')

# Widget 1: El control deslizante para elegir los intentos
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)

# Widget 2: El botón para iniciar el experimento
start_button = st.button('Ejecutar')

# Acción que ocurre solo cuando se presiona el botón
if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')

st.write('Esta aplicación aún no es funcional. En construcción.')