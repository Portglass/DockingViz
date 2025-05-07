import streamlit as st
import json
from stmol import showmol
import py3Dmol

st.title("Pembrolizumab")
st.session_state.PATH_PEMBROLIZUMAB = st.session_state.RESULT_FILE+"Pembrolizumab/"

# 1A2C
# Structure of thrombin inhibited by AERUGINOSIN298-A from a BLUE-GREEN ALGA
xyzview = py3Dmol.view(query='pdb:5DK3')
xyzview.setStyle({'cartoon':{'color':'spectrum'}})
showmol(xyzview, height = 500,width=800)

for i in ["heavy chain","light chain"]:
    file = open(st.session_state.PATH_PEMBROLIZUMAB + i + "_physico_chemical_properties.json", "r")
    json_file = json.load(file)
    file.close()
    st.header(i)
    with st.expander("General information"):
        st.write("Molecular Weight : "+str(json_file["Molecular_weight"]))
        st.write("Theorical pI : " + str(json_file["Theorical_pI"]))
        st.write("Half life hours pI : " + str(json_file["Half_life_hours"]))
        st.write("Instability index : " + str(json_file["Instability_index"]))
        st.write("Aliphatic index : " + str(json_file["Aliphatic_index"]))
        st.write("Aromaticity pourcent : " + str(json_file["Aromaticity_pourcent"]))
        st.write("Grand average hydropathicity : " + str(json_file["Grand_average_hydropathicity"]))

    with st.expander("Composition"):
        st.subheader("Atome")
        st.write("Total atome : " + str(json_file["Total atom"]))
        st.bar_chart(json_file["Atom_composition"])

        st.subheader("Acide aminé")
        st.write("Total ac : "+str(json_file["Number_ac"]))
        st.bar_chart(json_file["Ac_composition"])
        st.write("Total negatively charged residues (Asp+Glu) : " + str(json_file["Total_nb_negatively_charged_residues_Asp_Glu"]))
        st.write("Total positively charged residues (Arg+Lys) : " + str(json_file["Total_nb_positively_charged_residues_Arg_Lys"]))

        st.image(st.session_state.PATH_PEMBROLIZUMAB+"ac_color_scheme "+ i +".png")

    st.image(st.session_state.PATH_PEMBROLIZUMAB+"hydrophobic plot "+ i +".png")
    st.write("Score minimun : "+str(json_file["Hydrophobicity_plot"]["Score_min"]))
    st.write("Score maximum : "+str(json_file["Hydrophobicity_plot"]["Score_max"]))
    #st.json(json_file)
