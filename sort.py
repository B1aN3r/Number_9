import os
from numpy import sort
from pathlib import Path


dir = os.listdir('directory')

for i in dir:
    per = i.split('-')
    god='directory/'
    for j in per[0: len(per)-1]:
        god = god + j 
        if not os.path.exists(god):
            os.mkdir(god)
        god+='/'
    Path(f'{god+per[len(per)-1]}.txt').touch()
