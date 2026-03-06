import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Visualisasi Fungsi Kuadrat dan Turunannya")

a = st.slider("a", -5.0, 5.0, 1.0)
b = st.slider("b", -10.0, 10.0, 0.0)
c = st.slider("c", -10.0, 10.0, 0.0)

x = np.linspace(-10,10,200)

y = a*x**2 + b*x + c
dy = 2*a*x + b

fig, ax = plt.subplots()

ax.plot(x,y,label="f(x)")
ax.plot(x,dy,label="f'(x)")

ax.legend()
ax.grid(True)

st.pyplot(fig)