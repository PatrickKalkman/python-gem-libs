import streamlit as st
import matplotlib.pyplot as plt

# Application title
st.title("Streamlit Bar Chart Example")

# User input form
st.sidebar.header("User Input")
num_bars = st.sidebar.slider(
    "Number of bars", min_value=1, max_value=10, value=5, step=1
)
bar_values = [
    st.sidebar.number_input(f"Value for bar {i+1}", value=i + 1)
    for i in range(num_bars)
]


# Create a bar chart
def create_bar_chart(values):
    fig, ax = plt.subplots()
    ax.bar(range(len(values)), values)
    ax.set_xlabel("Bar index")
    ax.set_ylabel("Bar value")
    ax.set_title("Bar chart")
    return fig


# Display the bar chart
if st.button("Generate Bar Chart"):
    chart = create_bar_chart(bar_values)
    st.pyplot(chart)
