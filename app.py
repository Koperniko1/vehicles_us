import pandas as pd
import streamlit
import plotly.express as px
import numpy as np

df = pd.read_csv('vehicles_us.csv')
print(df.head())