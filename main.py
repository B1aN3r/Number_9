import click
from datetime import datetime
import enum
import random
from loguru import logger
from functools import wraps

### я не знаю  как запушить в гит библиотеку клик(я ее чуть-чуть модифицировал) для отлова ошибок неправильного ввода команды
# а так у меня все работает
logger.add('logs.log', format = '{time} {level} {message}',
level = "INFO", rotation= '50 KB', compression= 'zip')
# отлавливает команды, введенные в консоль
def click_log(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        context = click.get_current_context()
        logger.info(f"{context.command.name} {context.params}")
        return fn(*args, **kwargs)
    return wrapper
###

#создает группу вызывающихся функций

@click.group()
def cli():
    pass


@cli.command()
@click.option('--hour', is_flag=True, default=False)
@click_log
def newyear(hour):
    today = datetime.today()
    nyd = datetime(today.year + 1, 1, 1, 0, 0, 0)
    nydd = nyd - today
    if hour:
        logger.info(f'Вывод функции: До Нового года {nydd.days} д. и {int(nydd.seconds/3600)} ч.')
        click.echo(f'До Нового года {nydd.days} д. и {int(nydd.seconds/3600)} ч.')
    else:
        logger.info(f'Вывод функции: До нового года {nydd.days} дней')
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
@click_log
def toy():
    chipapu = random.choice(rand_color)
    munyanya = random.choice(rand_toy)
    logger.info(f'Вывод функции: {chipapu} {munyanya}')
    click.echo(f'Вывод функции: {chipapu} {munyanya}')

    

if __name__ == "__main__":
    cli()
