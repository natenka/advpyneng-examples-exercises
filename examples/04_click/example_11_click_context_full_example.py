import click


# Default values:
DFLT_DB_NAME = "dhcp_snooping.db"
DFLT_DB_SCHEMA = "dhcp_snooping_schema.sql"


@click.group()
@click.option("--db-filename", "-n", default=DFLT_DB_NAME, help="db filename")
@click.pass_context
def main(context, db_filename):
    context.obj = {"db_filename": db_filename}


@main.command()
@click.option("--db-schema", "-s", default=DFLT_DB_SCHEMA, help="db schema filename")
@click.pass_context
def create(context, db_schema):
    """
    create DB
    """
    print("Creating DB {} with DB schema {}".format(context.obj["db_filename"], db_schema))


@main.command()
@click.argument("filename", nargs=-1, required=True)
@click.option(
    "--switch-data",
    "-s",
    default=False,
    is_flag=True,
    help="add switch data if set, else add normal data",
)
@click.pass_context
def add(context, filename, switch_data):
    """
    add data to db from FILENAME
    """
    if switch_data:
        print("Adding switch data to database")
    else:
        print("Reading info from file(s) {}".format(", ".join(filename)))
        print("Adding data to db {}".format(context.obj["db_filename"]))


@main.command()
@click.option(
    "--key",
    "-k",
    type=click.Choice(["mac", "ip", "vlan", "interface", "switch"]),
    help="host key (parameter) to search",
)
@click.option("--value", "-v", help="value of key")
@click.option("--show-all", "-a", is_flag=True, help="show db content")
@click.pass_context
def get(context, key, value, show_all):
    """
    get data from db
    """
    if key and value:
        print("Geting data from DB: {}".format(context.obj["db_filename"]))
        print("Request data for host(s) with {} {}".format(key, value))
    elif key or value:
        print("Please give two or zero args\n")
        # print(get.help)
    else:
        print("Showing {} content...".format(context.obj["db_filename"]))


if __name__ == "__main__":
    main()
