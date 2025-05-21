import streamlit as st
import path
import sys

#Global Variable
dir = path.Path(__file__).absolute()
sys.path.append(dir.parent)

st.session_state.RESULT_FILE = dir.parent+"/Result_docking/"
st.session_state.DOCKING_FILE = dir.parent+"/Fichier docking/"

st.title("Docking Analyzing")

pages = {
    "Interaction":[
        st.Page("RBN_pembro_RIAB.py", title="RBN - Pembro RIAB"),
        st.Page("PD1_Pembrolizumab.py", title="PD1 - Pembrolizumab")
    ],
    "Protein":[
        st.Page("Pembrolizumab.py", title="Pembrolizumab")
    ]
}

pg = st.navigation(pages)
pg.run()