import streamlit as st
from streamlit_molstar import st_molstar
import os
import pandas as pd

st.title("RBN - Pembrolizumab")

#Global Variable
LIST_DOCKING = ["Diffdock", "Dynamic Bind"]
LIST_RBN = ["RBN3143","RBN012759"]
st.session_state.PATH_FILE_RBN = st.session_state.DOCKING_FILE + "RBN - Pembro\\"
st.session_state.PATH_RESULT_RBN = st.session_state.RESULT_FILE + "RBN - Pembro\\"

#Input docking
rbn = st.sidebar.selectbox("Which RBN do you prefer ?",LIST_RBN)
docking_method = st.sidebar.selectbox("Which Docking method do you prefer ?",LIST_DOCKING)
st.session_state.path_result_display = st.session_state.PATH_FILE_RBN + rbn + "\\" + docking_method + "\\"
list_files = [f.split(".")[0] for f in os.listdir(st.session_state.path_result_display) if os.path.isfile(st.session_state.path_result_display+f)]

file = st.sidebar.selectbox("Which file do you prefer ?",list_files)

#get rank
r = file.find("rank")
rank = file[r+4]
#print("Debug : "+str(rank))

#Display mol
st_molstar(st.session_state.path_result_display + file+".pdb")

#RMSD
st.subheader("DockRMSD")
with st.expander("DockRmsd"):
    st.session_state.result_dockrmsd = st.session_state.PATH_RESULT_RBN + "DockRMSD\\"
    df_rmsd = pd.read_csv(st.session_state.result_dockrmsd + rbn + "\\" + "Summary.csv", sep=";",header=0)
    st.write(df_rmsd)
    st.subheader("Moyenne du RMSD")
    #st.write(df_rmsd.mean())

#Prodigy
st.subheader("Prodigy")
with st.expander("Prodigy"):
    st.session_state.result_prodigy = st.session_state.PATH_RESULT_RBN + "Prodigy\\"
    file_prodigy = st.session_state.result_prodigy + "Result.csv"
    df_prodigy = pd.read_csv(file_prodigy, sep=";", header=0)
    df_prodigy = df_prodigy.loc[(df_prodigy["RBN"] == rbn) & (df_prodigy["Docking method"]==docking_method)]
    st.bar_chart(df_prodigy, x="Rank", y="Dgprediction (low refinement) (Kcal/mol)")
    st.bar_chart(df_prodigy, x="Rank",
                 y=["CC", "CN", "CO", "CX", "NN", "NO", "NX", "OO", "OX",
                    "XX"])

#Liaison Biovia
st.subheader("Biovia result")
with st.expander("Liaison Biovia"):
    st.session_state.result_biovia = st.session_state.PATH_RESULT_RBN + "Liaison_Biovia\\" + rbn + "\\" + docking_method + "\\"
    file_biovia = [f for f in os.listdir(st.session_state.result_biovia) if f == file+".svg"]
    if not file_biovia:
        st.write("No file corresponding")
    else:
        with open(st.session_state.result_biovia+file_biovia[0], "r") as f:
            svg_code = f.read()
        st.markdown(f"""<div>{svg_code}</div>""", unsafe_allow_html=True)


#PDBSum
st.subheader("PDBSum")
with st.expander("PDBSum"):
    st.session_state.result_pdbsum = st.session_state.PATH_RESULT_RBN + "PDBSum\\"
    file_pdbsum = st.session_state.result_pdbsum + "Result_PDBSum.csv"
    df_pdbsum = pd.read_csv(file_pdbsum, sep=";", header=0)
    st.write(rbn + " / "+docking_method + " / " + rank)
    df_link = df_pdbsum.loc[(df_pdbsum["rbn"] == rbn) & (df_pdbsum["Docking_method"]==docking_method) & (df_pdbsum["Rank"]==int(rank))]
    df_link.index = [0]
    link = df_link.at[0,'Link']
    st.write("Voir lien : "+link)