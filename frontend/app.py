import streamlit as st
from add_update import add_update_tab
from analytics import analytics_tab

st.title("Expense Management System")

tab1, tab2 = st.tabs(['Add/Update', 'Analytics'])

with tab1:
    add_update_tab()
with tab2:
    analytics_tab()