import streamlit as st
import pandas as pd
from streamlit_aggrid import AgGrid

df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
AgGrid(df)