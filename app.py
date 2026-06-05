import pandas as pd
import scipy.stats
import streamlit as st
import time

# Variables de estado que se conservan entre ejecuciones
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iteraciones', 'media'])

st.header('Lanzar una moneda')

def toss_coin(n):
    # Simula n lanzamientos de moneda usando una distribución de Bernoulli
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    means = []
    outcome_1_count = 0

    # Creamos un contenedor vacío en la interfaz para ir actualizando el gráfico
    chart_placeholder = st.empty()

    for outcome_no, r in enumerate(trial_outcomes, 1):
        if r == 1:
            outcome_1_count += 1
        current_mean = outcome_1_count / outcome_no
        means.append(current_mean)
        
        # Animación dinámica: Solo duerme si son pocos intentos para no congelar la app
        if n <= 100:
            chart_placeholder.line_chart(means)
            time.sleep(0.02)
            
    # Si son demasiados intentos, muestra el gráfico final de golpe para optimizar rendimiento
    if n > 100:
        chart_placeholder.line_chart(means)

    # Retorna la última media calculada
    return means[-1]

number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    st.session_state['experiment_no'] += 1
    
    # Ejecuta la simulación y obtiene la media final
    mean = toss_coin(number_of_trials)
    
    # Agrega el resultado al historial del estado de la sesión usando concat
    nuevo_registro = pd.DataFrame(data=[[st.session_state['experiment_no'], number_of_trials, mean]],
                                columns=['no', 'iteraciones', 'media'])
    
    st.session_state['df_experiment_results'] = pd.concat([st.session_state['df_experiment_results'], nuevo_registro], axis=0)
    st.session_state['df_experiment_results'] = st.session_state['df_experiment_results'].reset_index(drop=True)

# Muestra siempre la tabla con el historial acumulado
st.write(st.session_state['df_experiment_results'])