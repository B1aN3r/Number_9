import click
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

#@click.command()
#@click.option('--hour')

def newyear():
    today = date.today()
    nyd = date(today.year + 1, 1, 1)
    print((nyd - today).days)

if __name__ == '__main__':
    newyear()

