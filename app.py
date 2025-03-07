import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to perform calculations
def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)

# Function to plot the graph
def plot_graph(function, x_range):
    x = np.linspace(x_range[0], x_range[1], 400)
    try:
        y = eval(function)
        plt.figure(figsize=(10, 5))
        plt.plot(x, y, label=function)
        plt.title('Graph of ' + function)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.axhline(0, color='black', lw=0.5, ls='--')
        plt.axvline(0, color='black', lw=0.5, ls='--')
        plt.grid()
        plt.legend()
        plt.show()
    except Exception as e:
        st.error(f"Error in plotting: {str(e)}")

# Streamlit app
st.title("Scientific Calculator with Graphing")

# Input for calculation
st.header("Calculator")
expression = st.text_input("Enter a mathematical expression (e.g., 2 * (3 + 4) / 2):")
if st.button("Calculate"):
    result = calculate(expression)
    st.write("Result:", result)

# Input for graphing
st.header("Graphing")
function = st.text_input("Enter a function of x (e.g., np.sin(x), x**2, np.exp(x)):")
x_start = st.number_input("Start of x range:", value=-10.0)
x_end = st.number_input("End of x range:", value=10.0)

if st.button("Plot Graph"):
    if x_start < x_end:
        plot_graph(function, (x_start, x_end))
        st.pyplot(plt)
    else:
        st.error("Start of x range must be less than end of x range.")
