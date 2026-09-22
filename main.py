from src.parser import create_parser
from src.handler import add_expense,list_expenses,delete_expense,summary
def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    if args.command == "add":
        expense_id = add_expense(description=args.description,amount=args.amount)
        if expense_id:
            print(f"Expense added successfully (ID: {expense_id})")
        else:
            print(f"Expense add failure")

    elif args.command == "list":
        list_expenses()

    elif args.command == "delete":
        success  = delete_expense(args.id)
        if(success):
            print(f"Expense id:{args.id} deleted successfully")
        else:
            print(f"Expense with id:{args.id} not found")

    elif args.command == "summary":
        total_amount, month = summary(args.month)
        if args.month is None:
            print(f"Total expenses: ${total_amount:.2f}")
        else:
            print(f"Total expenses for {month}: ${total_amount:.2f}")


if __name__ == "__main__":
    main()
