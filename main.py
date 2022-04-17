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

class Colour(enum.Enum):
    rd = 'Red'
    gr = 'green'
    ye = 'yellow'
    bl = 'blue'
    pr = 'purple'

class Toys(enum.Enum):
    st = 'star'
    bl = 'ball'
    an = 'angel'
    sn = 'snowflake'

rand_color = list(Colour._value2member_map_)
rand_toy = list(Toys._value2member_map_)


@cli.command()
def toy():
    click.echo(f'{random.choice(rand_color)} {random.choice(rand_toy)}')
    

if __name__ == "__main__":
    cli()
