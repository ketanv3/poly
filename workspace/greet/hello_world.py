import click


@click.command()
@click.option('--name', required=True)
@click.option('--count', default=1)
def command(name, count):
    for i in range(count):
        print(f'Hi, {name}!')
