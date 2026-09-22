import argparse

def create_parser():
    try:
        parser = argparse.ArgumentParser(prog="expense-tracker",
                                        description="Command-line expense tracker"
                                        )

        sub_parsers = parser.add_subparsers(dest="command",required=True)

        # add
        # expense-tracker add --description "Lunch" --amount 20
        add_parser = sub_parsers.add_parser("add")
        add_parser.add_argument("--description",required=True)
        add_parser.add_argument("--amount",type=float,required=True)

        # list
        # expense-tracker list
        sub_parsers.add_parser("list")

        # delete
        # expense-tracker delete --id 2
        delete_parser = sub_parsers.add_parser("delete")
        delete_parser.add_argument("--id",type=int,required=True)

        # summary
        # expense-tracker summary
        # expense-tracker summary --month 8
        summary_parser = sub_parsers.add_parser("summary")
        summary_parser.add_argument("--month",type=int)

        return parser
    except:
        return None


