import streamlit as st
from gets import bcv_rate

st.set_page_config('Calculadora de Divisas', layout='centered')

# Header
st.title('Calculadora Bolívares / Dólares')

# Body
st.markdown('Este es una calculadora experimental para convertir bolívares a dólares con la tasa actualizada del Banco Central de Venezuela (BCV)')

st.write(f'En este momento la tasa cambiaria del BCV es de **Bs. {bcv_rate()}**')

numero = st.number_input('Inserte el monto en bolívares', step=0.1)

resultado = round(numero / bcv_rate(),2)

st.write(f'El resultado de la conversión es: **USD {resultado}**')