import streamlit as st
import pandas as pd
import numpy as np
import webbrowser
import streamlit.components.v1 as components

st.title('Endless Gus')

target_url = 'player.html'
# embed streamlit docs in a streamlit app
components.iframe(target_url)

# target_url = 'https://wfmu.org/archiveplayer/?show=95483&archive=189777&starttime=0:44:0'
# webbrowser.open_new_tab(target_url)



