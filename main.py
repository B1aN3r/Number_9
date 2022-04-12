import click
from datetime import datetime
import enum
import random


@click.group()
def cli():
    pass

@cli.command()
@click.option('--hour', is_flag=True, default=False)
def newyear(hour):
    today = datetime.today()
    nyd = datetime(today.year + 1, 1, 1, 0, 0, 0)
    nydd = nyd - today
    if hour:
        click.echo(f'До Нового года {nydd.days} д. и {int(nydd.seconds/3600)} ч.')
    else:
        click.echo(f'До нового года {nydd.days} дней')

@cli.command()
def toy():
    colour = ['red', 'green', 'yellow', 'blue', 'purple']
    toys = ['star', 'ball', 'angel', 'snowflake']
    click.echo(f'{random.choice(colour)} {random.choice(toys)}')
    

if __name__ == "__main__":
    cli()
