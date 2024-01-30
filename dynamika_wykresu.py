import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

x = np.linspace(-10, 10, 100)


def rozklad_normalny(x, mean, sd):
    prawdopodobienstwo = np.exp(-0.5 * ((x - mean) / sd) ** 2) / np.sqrt(np.pi * sd ** 2)
    return prawdopodobienstwo


mean = st.slider(label='średnia', min_value=0., max_value=100., value=4.)
sd = st.slider(label='odchylenie standardowe', min_value=0.1, max_value=100., value=4.)

pdf = rozklad_normalny(x, mean, sd)

fig, ax = plt.subplots()
plt.plot(x, pdf, color='blue')
plt.xlabel('Punkty danych')
plt.ylabel('Gęstość prawdopodobieństwa')
plt.grid()
st.pyplot(fig)