import streamlit as st
import pandas as pd
import numpy as np
import webbrowser
import streamlit.components.v1 as components
from selenium.webdriver.common.by import By
import time


#driver.find_elements(By.XPATH, '//button')


#%pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()

st.title('Endless Gus')

player_url = "https://wfmu.org/archiveplayer/?show=95483&archive=189777&starttime=0:44:0"
driver.get(player_url)

play_button = driver.find_element(By.XPATH, '//button')


#play_button.click() #start



time.sleep(10)


play_button.click() #stop




# target_url = 'https://wfmu.org/archiveplayer/?show=95483&archive=189777&starttime=0:44:0'
# webbrowser.open_new_tab(target_url)







