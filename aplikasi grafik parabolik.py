import streamlit as st
import numpy as np
import mathplotlib.pyplot as plt

st.title("Pengaruh koefisien a,b,c pada grafik parabolic")

a=st.slider("a",-2,2,1)
b=st.slider("b",-2,2,1)
c=st.slider("c",-2,2,1)

x=np.linspace(-5, 5,200)

y=a*x**+b*x+c

fig,ax=plt.subplots()

ax.plot(x,y,"f(x)")

ax.grid(True)
ax.legend()

style.pyplot(fig)