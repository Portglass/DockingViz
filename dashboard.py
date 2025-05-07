import streamlit as st
import path
import sys
import os

#Global Variable
dir = path.Path(__file__).absolute()
sys.path.append(dir.parent)

print(dir.parent)
print(os.listdir())

st.session_state.RESULT_FILE = dir.parent+"\\Result_docking\\"
st.session_state.DOCKING_FILE = dir.parent+"\\Fichier docking\\"

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