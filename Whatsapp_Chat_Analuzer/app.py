import streamlit as st 
import preprocessor
st.sidebar.title("Whatsapp Chat Analyzer")
upload_file = st.sidebar.file_uploader("Choose a file")
if upload_file is not None:
    bytes_data = upload_file.getvalue()
    data = bytes_data.decode('utf-8')
    df = preprocessor.preprocess(data)
    st.dataframe(df)