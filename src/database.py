import json
import os
from typing import TypedDict

DATABASE_FILE = "expenses.json"


class Expense(TypedDict):
    id:int
    description:str
    amount:float
    date:str


def load_expense() -> list[Expense]:
    # if file not exists create
    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE,"w") as file:
            json.dump([],file)
        return []

    with open(DATABASE_FILE,"r") as file:
        return json.load(file)

def save_expense(expenses:list[Expense])->None:
    with open(DATABASE_FILE,"w") as file:
        json.dump(expenses,file,indent=4)