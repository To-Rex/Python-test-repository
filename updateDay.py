import os
from random import randint

for i in range(0,randint(1,3)):
    d = '2020-6-26'
    with open('file.txt', 'a') as file:
        file.write(d + "\n")
    os.system('git add .')
    os.system('git commit --date="' + d + '" -m "commit"')

os.system('git push origin master')