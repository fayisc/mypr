import streamlit as st #module for easy web-app
import pandas as pd
import matplotlib.pyplot as plt

# Upload a CSV file
uploaded_file = st.file_uploader("Choose a file", type=["csv"])

# If a file was uploaded
if uploaded_file:
    # Read the file as a pandas DataFrame
    data = pd.read_csv(uploaded_file)

    # Group the data by country and sex
    grouped_data = data.groupby(["country", "sex"]).size().reset_index(name="count")

    # Create the plot
    fig, ax = plt.subplots()
    colors = {"Female": "blue", "Male": "red"} # set colors for each sex
    for sex in colors.keys():
        data_subset = grouped_data[grouped_data["sex"] == sex]
        ax.bar(data_subset["country"], data_subset["count"], color=colors[sex], label=sex)
    ax.legend()

    # Set labels and title
    ax.set_xlabel("Country")
    ax.set_ylabel("Count")
    ax.set_title("Count of People by Country and Sex")

    # Display the plot in Streamlit
    st.pyplot(fig)
