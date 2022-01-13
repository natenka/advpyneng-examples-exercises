import click


@click.command()
@click.option("--username", "-u", prompt=True)
#@click.option("--password", "-p", prompt=True, hide_input=True, confirmation_prompt=True)
@click.password_option()
def cli(username, password):
    print(username, password)


if __name__ == "__main__":
    cli()
