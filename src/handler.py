from src.database import load_expense, save_expense,Expense
from datetime import date

def add_expense(description:str,amount:float)->int|None:
    try:
        expenses = load_expense()
        # create expense
        new_id = max((expense["id"] for expense in expenses),default=0) + 1

        new_expense:Expense = {
            "id":new_id,
            "description":description,
            "amount":amount,
            "date":date.today().isoformat()
        }
        # append to expense
        expenses.append(new_expense)
        # save_expense(expense)
        save_expense(expenses)
        return new_id
    except Exception as e:
        print(f"Error {e}")
        return None

def list_expenses()->None:
    expenses = load_expense()
    if not expenses:
        print("No expenses found")
        return 
    #display expenses
    print(f"{'ID':<5}{'Date':<15}{'Description':<20}{'Amount':>10}")
    print("-"*50)
    for expense in expenses:
        amount = f"${expense["amount"]:.2f}"
        print(
            f"{expense['id']:<5}"
            f"{expense['date']:<15}"
            f"{expense['description']:<20}"
            f"{amount:>10}"
        )


def delete_expense(expense_id:int)->bool:
    try:
        expenses = load_expense()
        new_expenses  = [expense 
                         for expense in expenses 
                         if expense["id"]!=expense_id
                        ]
        # Nothing was deleted
        if len(new_expenses) == len(expenses):
            return False
        save_expense(new_expenses)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def summary(month:int|None = None)->tuple[float,str|None]:
    months = [
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"
    ]

    try:
        expenses = load_expense()
        #calculate total
        if month is not None:
            if month <1 or month>12:
                raise ValueError("Month must be between 1 and 12")
            expenses = [expense for expense in expenses if int(expense["date"][5:7])==month]
        total_amount = sum(expense["amount"] for expense in expenses)
        month_name = months[month-1] if month is not None else None
        return total_amount,month_name
    
    except Exception as e:
        print(f"Error: {e}")
        return 0.0,None