import streamlit as st
from streamlit_molstar import st_molstar
import os
import xml.etree.ElementTree as ET
import pandas as pd
from additional_funtion import parse_struct

st.title("Parp14 - RBN")

#Global Variable
LIST_DOCKING = ["Diffdock", "Dynamic Bind"]
LIST_RBN = ["RBN3143","RBN012759"]
st.session_state.PATH_FILE_PARP = st.session_state.DOCKING_FILE + "PARP - RBN/"
st.session_state.PATH_RESULT_PARP = st.session_state.RESULT_FILE + "Parp14 - RBN/"

#Input docking
rbn = st.sidebar.selectbox("Which RBN do you prefer ?",LIST_RBN)
docking_method = st.sidebar.selectbox("Which Docking method do you prefer ?",LIST_DOCKING)

with st.expander("Affinity - Prodigy"):
    st.session_state.result_prodigy = st.session_state.PATH_RESULT_PARP + "Prodigy/"
    file_prodigy = st.session_state.result_prodigy + "result.csv"
    df_prodigy = pd.read_csv(file_prodigy, sep=";", header=0)
    df_prodigy = df_prodigy.loc[(df_prodigy["RBN"] == rbn) & (df_prodigy["Docking method"] == docking_method)]
    st.bar_chart(df_prodigy, x="Rank", y="Dgprediction (low refinement) (Kcal/mol)")
    st.bar_chart(df_prodigy, x="Rank",
                 y=["CC", "CN", "CO", "CX", "NN", "NO", "NX", "OO", "OX", "XX"])

with st.expander("RMSD"):
    st.write("Not implemented")

with st.expander("Interactions"):
    st.write("Not implemented")
