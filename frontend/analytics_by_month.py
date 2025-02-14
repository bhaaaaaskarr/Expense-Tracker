import pandas as pd
import streamlit as st
from datetime import datetime
import requests

APP_URL = "http://localhost:8000"

def analytics_by_month_tab():
    response = requests.get(f"{APP_URL}/monthly_analytics")
    response=response.json()
    df=pd.DataFrame(response)
    df['month'] = pd.to_datetime(df['month'], format='%Y-%m').dt.strftime('%b \'%y')

    st.bar_chart(df.set_index('month'))
    st.table(df)