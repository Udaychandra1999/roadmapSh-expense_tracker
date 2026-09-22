import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        prog="expense-tracker",
        description="Command-line expense tracker",
        epilog="Use 'expense-tracker <command> --help' for more information."
    )

    sub_parsers = parser.add_subparsers(
        dest="command",
        title="commands",
        description="Available commands"
    )

    # add
    # expense-tracker add --description "Lunch" --amount 20
    add_parser = sub_parsers.add_parser(
        "add",
        help="Add a new expense",
        description="Add a new expense with a description and amount."
    )
    add_parser.add_argument(
        "--description",
        required=True,
        help="Description of the expense"
    )
    add_parser.add_argument(
        "--amount",
        type=float,
        required=True,
        help="Amount of the expense"
    )

    # list
    # expense-tracker list
    sub_parsers.add_parser(
        "list",
        help="List all expenses",
        description="Display all recorded expenses."
    )

    # delete
    # expense-tracker delete --id 2
    delete_parser = sub_parsers.add_parser(
        "delete",
        help="Delete an expense",
        description="Delete an expense using its ID."
    )
    delete_parser.add_argument(
        "--id",
        type=int,
        required=True,
        help="ID of the expense to delete"
    )

    # summary
    # expense-tracker summary
    # expense-tracker summary --month 8
    summary_parser = sub_parsers.add_parser(
        "summary",
        help="Show expense summary",
        description="Show the total amount of expenses."
    )
    summary_parser.add_argument(
        "--month",
        type=int,
        help="Show expenses for a specific month (1-12)"
    )

    return parser