import os
from random import randint

date = '2021-6-20'
for i in range(0,7):
    for j in range(0,randint(5,11)):
        d = date + ' ' + str(i) + ' hours ago'
        with open('file.txt', 'a') as file:
            file.write(d + "\n")
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "commit"')

os.system('git push origin master')
