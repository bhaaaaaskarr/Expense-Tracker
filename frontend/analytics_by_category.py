import pandas as pd
import streamlit as st
from datetime import datetime
import requests

APP_URL = "http://localhost:8000"


def analytics_by_category_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input(label='Start Date', value=datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input(label='End Date', value=datetime(2024, 8, 3))

    if st.button('Get Analytics'):
        payload = {
            "start_date": str(start_date),
            "end_date": str(end_date),
        }
        response = requests.post(f"{APP_URL}/analytics", json=payload)
        response=response.json()
        data = {
            'Category': list(response.keys()),
            'Total': [v['total'] for v in response.values()],
            'Percentage': [round(v['percentage'],2) for v in response.values()]
        }
        df = pd.DataFrame(data)
        # df["Total"] = df["Total"].map(lambda x: f"{x:.2f}")
        # df["Percentage"] = df["Percentage"].map(lambda x: f"{x:.2f}")

        st.bar_chart(data=df.set_index('Category')['Percentage'])
        st.table(df)
        # st.table(data)
        # st.write(data['Total'], data['Percentage'])
