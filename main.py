from src.parser import create_parser
from src.handler import add_expense,list_expenses,delete_expense,summary
def main():
    try:
        parser = create_parser()
        args = parser.parse_args()

        if args.command == "add":
            expense_id = add_expense(description=args.description,amount=args.amount)
            if expense_id:
                print(f"Expense added successfully (ID: {expense_id})")
            else:
                print(f"Expense add failure")

        elif args.command == "list":
            print(f"list_expense")

        elif args.command == "delete":
            print(f"delete id {args.id}")
            flag  = delete_expense(args.id)
            if(flag):
                print(f"Expense id:{args.id} deleted successfully")
            elif(flag is None):
                print(f"Error occured in deletion")
            else:
                print(f"Expense with id:{args.id} not found")

        elif args.command == "summary":
            print(f"summary: {args.month}")
            total_amount, month = summary(args.month)
            if args.month is None:
                print(f"Total expenses: ${total_amount:.2f}")
            else:
                print(f"Total expenses for {month}: ${total_amount:.2f}")
    
    except Exception as e:
        print(f"Error:{e}")

if __name__ == "__main__":
    main()
