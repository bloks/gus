import streamlit as st
import pandas as pd
import numpy as np
import webbrowser
import streamlit.components.v1 as components

st.title('Endless Gus')


html_string = "<span style=""white-space:nowrap""><a href=""https://wfmu.org/flashplayer.php?version=3&amp;show=140083&amp;archive=253112&amp;starttime=0:30:21"" onclick=""return kdbarchivelink(this.href, 3)"">Pop-up</a></span>"

st.html(html_string)





# target_url = 'https://wfmu.org/archiveplayer/?show=95483&archive=189777&starttime=0:44:0'
# webbrowser.open_new_tab(target_url)



