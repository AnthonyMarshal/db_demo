import streamlit as st
import pandas as pd
import numpy as np
# Set the title of the dashboard
st.title("Simple Streamlit Dashboard")
# Sidebar with options
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Home", "Data Overview", "Visualizations", "Settings"])
# Home section
if options == "Home":
  st.header("Welcome to the Dashboard!")
  st.write("This is a simple dashboard created with Streamlit.")
# Data Overview section
elif options == "Data Overview":
  st.header("Data Overview")
  # Generate some sample data
  data = pd.DataFrame({'A': np.random.rand(100),'B': np.random.rand(100),'C': np.random.rand(100)})
  st.subheader("Sample Data")
  st.write(data.head())
  st.subheader("Statistics")
  st.write(data.describe())
# Visualizations section
elif options == "Visualizations":
  st.header("Visualizations")
  st.subheader("Line Chart")
  st.line_chart(data)
  st.subheader("Area Chart")
  st.area_chart(data)
  st.subheader("Bar Chart")
  st.bar_chart(data)
# Settings section
elif options == "Settings":
  st.header("Settings")
  st.subheader("Dashboard Settings")
  theme = st.selectbox("Select Theme", ["Light", "Dark", "Custom"])
  st.subheader("User Settings")
  user_name = st.text_input("Enter your name")
  st.write("Hello, ", user_name)
  st.subheader("Other Settings")
  st.slider("Select value", 0, 100, 50)
# Footer
st.sidebar.write("Demo Test")
