import streamlit as st
import pandas as pd

def load_txt_file():
    uploaded_files = st.file_uploader(
        "Textdateien auswählen",
        type=["txt"],
        accept_multiple_files=True
    )

    data_list = []

    if uploaded_files:
        for uploaded_file in uploaded_files:
            file_content = uploaded_file.read().decode("utf-8")
            
            data_list.append({
                "Titel": uploaded_file.name,
                "Text": file_content
            })
            
        df = pd.DataFrame(data_list)
        return df  
    
    return None
      