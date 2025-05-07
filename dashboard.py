import streamlit as st
import os

#Global Variable
st.session_state.RESULT_FILE = "C:\\Users\\corp.revillon\\OneDrive - HUBEBI\\Bureau\\Result_docking\\"
st.session_state.DOCKING_FILE = "C:\\Users\\corp.revillon\\OneDrive - HUBEBI\\Bureau\\Fichier docking\\"

st.title("Docking Analyzing")

pages = {
    "Interaction":[
        st.Page("RBN_pembro.py", title="RBN - Pembro"),
        st.Page("PD1_complex.py", title="PD1 - Complex")
    ],
    "Protein":[
        st.Page("Pembrolizumab.py", title="Pembrolizumab")
    ]
}

pg = st.navigation(pages)
pg.run()