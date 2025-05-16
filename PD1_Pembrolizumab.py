import streamlit as st
from streamlit_molstar import st_molstar
import os
import xml.etree.ElementTree as ET
import pandas as pd

st.title("PD1 - Pembrolizumab")

st.subheader("littérature")
st.image("Result_docking/PD1 - Pembrolizumab/litterature/medium.png")
st.image("Result_docking/PD1 - Pembrolizumab/litterature/liaison.png")
st.write("source : https://medium.com/@caseysteffen/comparative-analysis-pembrolizumab-and-pd-1-receptor-binding-properties-de368b55381f")

#Global variable
LIST_DOCKING = ["Haddock_wt_spe", "Cluspro_w_spe"]
LIST_CHAIN = ["Heavy chain","Light chain"]
st.session_state.path_file = "Result_docking/PD1 - Pembrolizumab/"
st.session_state.path_file_prodigy = "Result_docking/PD1 - Pembrolizumab/Prodigy_neurosnap.csv"

#Selection
docking_method = st.sidebar.selectbox("Which Docking method do you prefer ?",LIST_DOCKING)

st.session_state.path_file_docking = st.session_state.path_file + docking_method + "/" + "File/"
list_files = [".".join(f.split(".")[:-1]) for f in os.listdir(st.session_state.path_file_docking) if os.path.isfile(st.session_state.path_file_docking+f)]
file = st.sidebar.selectbox("Which file do you want", list_files)
st.session_state.path_result_file = st.session_state.path_file + docking_method + "/" + file + "/"

Prodigy_chain = st.sidebar.selectbox("Which Chain do you prefer (prodigy) ?",LIST_CHAIN)


#Haddock wt specification
if docking_method =="Haddock_wt_spe":
    st.subheader("Haddock 1er jet without specification")
    st.write("Ce docking a été réalisé via le logiciel Haddock. Il est à l'aveugle et flexible, les modèles présentés actuellement sont seulement ceux se trouvant dans a zone Fab")

if docking_method == "Cluspro_w_spe":
    st.subheader("Cluspro 1er jet with specification")
    st.write("Ce docking a été réalisé via le logiciel Cluspro. Il a ciblé les chaines A,B notamment dans la zone Fab en se basant sur les interactions déja disponible dans la littérature (voir section Littérature). Les modèles présentés actuellement sont seulement ceux se trouvant dans a zone Fab")

#Display mol
st_molstar(st.session_state.path_file_docking + file+".pdb")

#Liaison
with st.expander("Liaisons (PDBPisa)"):
    list_files_liaisons = [f for f in os.listdir(st.session_state.path_result_file) if os.path.isfile(st.session_state.path_result_file+f) and f.startswith("liaison")]
    if list_files_liaisons == []:
        st.write("No file detected")
    else:
        for file_liaison in list_files_liaisons:
            tree = ET.parse(st.session_state.path_result_file + file_liaison)
            root = tree.getroot()

            # Stockage des données
            data = []
            for struct in root.findall("STRUCTURE"):
                struct1 = struct.find("STRUCTURE1").text.strip()
                distance = float(struct.find("DISTANCE").text)
                struct2 = struct.find("STRUCTURE2").text.strip()
                data.append({
                    "Structure 1": struct1,
                    "Distance (Å)": round(distance, 3),
                    "Structure 2": struct2
                })

            # Création du DataFrame
            df = pd.DataFrame(data)

            # Affichage
            st.subheader("Tableau " +" ".join(file_liaison.split(".")[0].split("_")[1:]))
            st.dataframe(df)

            # Filtrage (ex: distance max)
            max_dist = st.slider("Distance maximale", 2.0, 5.0, 3.5, key=file_liaison)
            filtered_df = df[df["Distance (Å)"] <= max_dist]
            st.dataframe(filtered_df)

with st.expander("Affinity (Prodigy - Neurosnap)"):
    df_prodigy = pd.read_csv(st.session_state.path_file_prodigy,sep=";", header=0)
    st.dataframe(df_prodigy)
    df_prodigy_chain = df_prodigy.loc[(df_prodigy["Chain"] == Prodigy_chain) & (df_prodigy["Software"] == docking_method)]
    st.bar_chart(df_prodigy_chain, x="File", y=["No. of intermolecular contacts", "No. of charged-charged contacts", "No. of charged-polar contacts", "No. of charged-apolar contacts", "No. of polar-polar contacts", "No. of apolar-polar contacts", "No. of apolar-apolar contacts"])
    st.bar_chart(df_prodigy_chain, x="File", y="Percentage of apolar NIS residues")
    st.bar_chart(df_prodigy_chain, x="File", y="Percentage of charged NIS residues")
    st.bar_chart(df_prodigy_chain, x="File", y="Predicted binding affinity")
    st.bar_chart(df_prodigy_chain, x="File", y="Predicted dissociation constant")
