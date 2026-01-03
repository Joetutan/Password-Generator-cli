import argparse


def get_commands():
    
    parser = argparse.ArgumentParser(description="Cli Password manager ")
    subparser = parser.add_subparsers(dest="command")

    #--- Init subcommand ---
    init_cmd = subparser.add_parser("init", help="Initialize password vault")

    #--- add subcommand ---
    add_cmd = subparser.add_parser("add", help="add new password to vault")
    add_cmd.add_argument("len", type= int, default= 16, help="assign password length")
    add_cmd.add_argument("char", type=str, default="base64", help="assign charset")

    #--- get subcommand ---
    get_cmd = subparser.add_parser("get", help="retrieve password from vault")

    #--- rotate subcommand ---
    rotate_cmd = subparser.add_parser("rotate", help="rotate account password")
    rotate_cmd.add_argument("--account", help="provide account name" )

    #--- list subcommand ---
    list_cmd = subparser.add_parser("list", help="list acounts stored in vault")

    return parser.parse_args()