import streamlit as st
import pandas as pd
import openpyxl

st.title("Analyse your Data .Quickly!")
st.subheader("Easy CSV and Excel file analysis")
st.markdown("<br> <br>",unsafe_allow_html=True)
# Upload a CSV or Excel file
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])


# If a file was uploaded
if uploaded_file:
    # Get the file extension
    file_ext = uploaded_file.name.split(".")[-1]

    # If the file is a CSV
    if file_ext == "csv":
        # Read the file as a pandas DataFrame
        data = pd.read_csv(uploaded_file)

        column_name = st.selectbox("Select a column", data.columns)
        column_data = data[column_name]
        # Display the selected column data
        st.write(column_data)

    # If the file is an Excel file
    elif file_ext == "xlsx":
        # Load the Excel file using openpyxl
        workbook = openpyxl.load_workbook(uploaded_file)

        # Get the active worksheet
        worksheet = workbook.active

        # Create an empty list to store the rows
        rows = []

        # Iterate over the rows and append them to the list
        for row in worksheet.iter_rows(values_only=True):
            rows.append(row)

        # Create a pandas DataFrame from the rows
        data = pd.DataFrame(rows, columns=worksheet[1])

        # Print the column names
        st.write("Column names:", data.columns)

        

    def my_button_function(data):
         st.write(data)
button_clicked = st.button("View all data")
# If the button is clicked
if button_clicked:
    # Try to read the file as a pandas DataFrame
     if uploaded_file is not None:
        if uploaded_file:
            st.write(data)
        
     else :
        
      st.markdown("<p style='color: red;'>Please upload a valid file.</p>", unsafe_allow_html=True)








# import streamlit as st

# binary_contents = b'example content'
# # Defaults to 'application/octet-stream'
# st.download_button('Download binary file', binary_contents)

# import streamlit as st

# with open("flower.png", "rb") as file:
#     btn = st.download_button(
#             label="Download image",
#             data=file,
#             file_name="flower.png",
#             mime="image/png"
#           )