import streamlit as st
from datetime import datetime
import requests

APP_URL = "http://localhost:8000"


def add_update_tab():
    selected_date = st.date_input('Enter Date', datetime(2024, 8, 1), label_visibility="collapsed")
    response = requests.get(f"{APP_URL}/expenses/{selected_date}")
    if response.status_code == 200:
        existing_expenses = response.json()
        st.success('Expenses loaded successfully')
    else:
        st.error('Failed to retrieve expenses')
        existing_expenses = []

    categories = ['Rent', 'Food', 'Shopping', 'Entertainment', 'Other']

    with st.form(key='expense_form'):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("Amount")  # Column header
        with col2:
            st.write("Category")  # Column header
        with col3:
            st.write("Notes")  # Column header

        expenses = []
        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i]['amount']
                category = existing_expenses[i]['category']
                notes = existing_expenses[i]['notes']

            else:
                amount = 0.0
                category = 'Other'
                notes = ''

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(label='Amount', value=amount, min_value=0.0, step=10.0,
                                               key=f"amount_{i}", label_visibility='collapsed')

            with col2:
                category_input = st.selectbox(label='Category', index=categories.index(category), options=categories,
                                              key=f'category_{i}', label_visibility='collapsed')

            with col3:
                notes_input = st.text_input(label='Notes', value=notes, key=f'notes_{i}', label_visibility="collapsed")

            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })

        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            filtered_expenses = [expense for expense in expenses if
                                 expense['amount'] > 0]  # won't upload the default rows(rows with amount=0)

            response = requests.post(f"{APP_URL}/expenses/{selected_date}", json=filtered_expenses)
            if response.status_code == 200:
                st.success('Expenses updated successfully')
            else:
                st.error('Failed to update expenses')
