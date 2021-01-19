import os
from random import randint

for i in range(0,randint(5,21)):
    d = '2021-1-19'
    with open('file.txt', 'a') as file:
        file.write(d + "\n")
    os.system('git add .')
    os.system('git commit --date="' + d + '" -m "commit"')

os.system('git push origin master')