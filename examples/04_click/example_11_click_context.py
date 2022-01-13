import click


@click.group()
@click.option("--db-filename", "-n", help="db filename")
@click.pass_context
def dhcp_db(context, db_filename):
    context.obj = {"db_filename": db_filename}


@dhcp_db.command()
@click.option("--db-schema", "-s", help="db schema filename")
@click.pass_context
def create(context, db_schema):
    """
    create DB
    """


@dhcp_db.command()
@click.argument("filename", nargs=-1, required=True)
@click.option("--switch-data", "-s", default=False, is_flag=True)
@click.pass_context
def add(context, filename, switch_data):
    """
    add data to db from FILENAME
    """


@dhcp_db.command()
@click.option("--key", "-k", type=click.Choice(["mac", "ip", "vlan"]))
@click.option("--value", "-v", help="value of key")
@click.option("--show-all", "-a", is_flag=True, help="show db content")
@click.pass_context
def get(context, key, value, show_all):
    """
    get data from db
    """


if __name__ == "__dhcp_db__":
    dhcp_db()
