import os
from random import randint

# for i in range(1,365):
#     for j in range(0,randint(5,11)):
#         d = str(i) + ' days ago'
#         with open('file.txt', 'a') as file:
#             file.write(d + "\n")
#         os.system('git add .')
#         os.system('git commit --date="' + d + '" -m "commit"')

# current day commit

# for i in range(0,randint(5,161)):
#     d = '0 days ago'
#     with open('file.txt', 'a') as file:
#         file.write(d + "\n")
#     os.system('git add .')
#     os.system('git commit --date="' + d + '" -m "commit"')

# os.system('git push origin master')

#2022-6-11 day commit 
for i in range(0,randint(5,11)):
    d = '2022-6-2'
    with open('file.txt', 'a') as file:
        file.write(d + "\n")
    os.system('git add .')
    os.system('git commit --date="' + d + '" -m "commit"')

os.system('git push origin master')