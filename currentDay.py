import os
from random import randint

# for i in range(0,randint(5,161)):
#     d = '0 days ago'
#     with open('file.txt', 'a') as file:
#         file.write(d + "\n")
#     os.system('git add .')
#     os.system('git commit --date="' + d + '" -m "commit"')
# os.system('git push origin master')

# cd existing_repo
# git remote add origin https://gitlab.com/To-Rex/python-test.git
# git branch -M main
# git push -uf origin main
#pushing gitlab

for i in range(0,randint(5,161)):
    d = '0 days ago'
    with open('file.txt', 'a') as file:
        file.write(d + "\n")
    os.system('git add .')
    os.system('git commit --date="' + d + '" -m "commit"')
os.system('git push origin master')
os.system('git push -uf origin master')
