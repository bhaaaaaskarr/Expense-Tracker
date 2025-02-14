# Expense Tracking System

The **Expense Tracking System** is a web application designed to help users manage and track their personal or business expenses. The project consists of two main components: a **Streamlit** frontend and a **FastAPI** backend server. The frontend allows users to interact with the application, input their expenses, and visualize data, while the backend handles API requests and processes data.

This system also includes testing for both frontend and backend functionality.

## Project Structure

- `frontend/`: Contains the code for the **Streamlit** application, which serves as the user interface.
- `backend/`: Contains the code for the **FastAPI** backend server, which provides the necessary API endpoints for interacting with the expense data.
- `tests/`: Contains the test cases for both the frontend and backend, ensuring the system operates correctly.
- `requirements.txt`: A list of all the required Python packages for both the frontend and backend components.
- `README.md`: Provides an overview and instructions for setting up and running the project.

## Features

- **Expense Tracking**: Users can add, update, or delete expenses in various categories.
- **Expense Visualization**: The system provides visualizations (e.g., pie charts, bar charts) of the user's expenses.
- **User-friendly Interface**: The frontend is built with **Streamlit**, making it easy to use and interact with.
- **RESTful API**: The backend is built with **FastAPI**, providing fast and efficient handling of requests.

## Installation Instructions

To set up the project on your local machine, follow these steps:

### 1. Clone the Repository

Start by cloning the project to your local machine:
```bash
git clone https://github.com/yourusername/expense-management-system.git
cd expense-management-system
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-management-system.git
   cd expense-management-system
   ```
2. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
3. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server.server:app --reload
   ```
4. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```