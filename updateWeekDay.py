import os
from random import randint

date = '2021-6-23'
for i in range(0,7):
    for j in range(0,randint(5,11)):
        d = '2021-6-' + str(i+1) + ' ' + str(j) + ':00:00'
        with open('file.txt', 'a') as file:
            file.write(d + "\n")
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "commit"')

os.system('git push origin master')
