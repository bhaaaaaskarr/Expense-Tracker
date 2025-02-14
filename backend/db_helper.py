import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger('db_helper')


@contextmanager
def fetch_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='expense_manager'
    )
    if connection.is_connected():
        print('--------------------------------------')
        print('* * * Connected to the database * * *')
        print('--------------------------------------')
    else:
        print("Connection unsuccessful!")

    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()


def fetch_all_expenses():
    logger.info(f"'fetch_all_expenses' was called")
    with fetch_db_cursor as cursor:
        cursor.execute('select * from expenses')
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)


def fetch_expenses_by_date(expense_date):
    logger.info(f"'fetch_expenses_by_date' was called with date:{expense_date}")
    with fetch_db_cursor() as cursor:
        cursor.execute('select * from expenses where expense_date=%s', (expense_date,))
        expenses = cursor.fetchall()
        return expenses


def update_expenses(expense_date, amount, category, notes):
    logger.info(
        f"'update_expenses' was called with date:{expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with fetch_db_cursor(commit=True) as cursor:
        cursor.execute('insert into expenses (expense_date,amount, category, notes) values (%s,%s,%s,%s)',
                       (expense_date, amount, category, notes)
                       )


def delete_expenses_by_date(expense_date):
    logger.info(f"'delete_expenses_by_date' was called with {expense_date}")
    with fetch_db_cursor(commit=True) as cursor:
        cursor.execute('delete from expenses where expense_date=%s', (expense_date,))


def fetch_expenses_between_dates(start_date, end_date):
    logger.info(f"'fetch_expenses_between_dates' was called with start date: {start_date} and end date: {end_date}")
    with fetch_db_cursor() as cursor:
        cursor.execute('''select * from expenses 
                        where expense_date
                        between %s and %s
                        order by expense_date
                       ''',
                       (start_date, end_date,)
                       )
        expenses = cursor.fetchall()
        return expenses


def fetch_summary(start_date, end_date):
    logger.info(f"'fetch_summary was called with start_date: {start_date} and end_date: {end_date}")
    with fetch_db_cursor() as cursor:
        cursor.execute('''select category, sum(amount) as total from expenses
        where expense_date between %s and %s
        group by category
        order by total desc''',(start_date,end_date))
        expenses=cursor.fetchall()
        return expenses

if __name__ == '__main__':
    # update_expenses('2020-04-14', 14, 'food', 'cake')
    # delete_expenses_by_date('2020-04-14')
    # print(fetch_expenses_by_date('2024-08-15'))
    # print(fetch_expenses_between_dates('2024-08-01', '2024-08-05'))
    print(fetch_summary('2024-08-01','2024-08-08'))