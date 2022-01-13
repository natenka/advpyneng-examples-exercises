import click


@click.group()
def pomodoro_cli():
    pass


@pomodoro_cli.command()
@click.option("--day", "-d", is_flag=True)
@click.option("--week", "-w", is_flag=True)
@click.option("--month", "-m", is_flag=True)
def stats(day, week, month):
    print("STATS")


@pomodoro_cli.command()
@click.option("--pomodoros_to_run", "-r", default=5, show_default=True, type=int)
@click.option("--work_minutes", "-w", default=25, show_default=True, type=int)
@click.option("--short_break", "-s", default=5, show_default=True, type=int)
@click.option("--long_break", "-l", default=30, show_default=True, type=int)
@click.option("--set_size", "-p", default=4, show_default=True, type=int)
def work(pomodoros_to_run, work_minutes, short_break, long_break, set_size):
    pass


if __name__ == "__main__":
    pomodoro_cli()
