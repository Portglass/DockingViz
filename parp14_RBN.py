import streamlit as st
from streamlit_molstar import st_molstar
import os
import xml.etree.ElementTree as ET
import pandas as pd
from additional_funtion import parse_struct

st.title("Parp14 - RBN")

with st.expander("RMSD"):
    st.write("Not implemented")

with st.expander("Affinity"):
    st.write("Not implemented")

with st.expander("Interactions"):
    st.write("Not implemented")