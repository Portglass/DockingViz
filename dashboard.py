import streamlit as st
import path
import sys

#Global Variable
dir = path.Path(__file__).absolute()
sys.path.append(dir.parent.parent)

st.session_state.RESULT_FILE = "Result_docking\\"
st.session_state.DOCKING_FILE = "Fichier docking\\"

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