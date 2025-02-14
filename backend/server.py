from selectors import SelectSelector

from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel


class Expense(BaseModel):  # tells fastapi that data should be returned in this format
    # expense_date: date
    amount: float
    category: str
    notes: str


class DateRange(BaseModel):  # tells fastapi that data should be returned in this format
    start_date: date
    end_date: date


app = FastAPI()


@app.get("/expenses/{expense_date}", response_model=List[Expense])  #list of a class
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_by_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve summary from the database.")

    return expenses


@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: List[Expense]):
    db_helper.delete_expenses_by_date(expense_date)
    for expense in expenses:
        expenses = db_helper.update_expenses(expense_date, expense.amount, expense.category, expense.notes)

    return {"message": "Expenses updated successfully."}


@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    expenses = db_helper.fetch_summary(date_range.start_date, date_range.end_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve summary from the database.")

    total = sum([row['total'] for row in expenses])

    breakdown={}

    for row in expenses:
        percentage =(row['total']/total)*100 if total !=0 else 0
        breakdown[row['category']]={'total': row['total'],
                                    'percentage':percentage}

    return breakdown
