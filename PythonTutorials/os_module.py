import os
from datetime import datetime

# os.chdir() changes cwd
# os.getcwd returns cwd
# os.listdir returns contents of a directory
# os.mkdir() and os.makedirs makes directories

# os.makedirs('test/testing')

# os.rmdir to remove directories
# os.rename('original.txt', 'new.txt')

# print(os.stat('testdata.txt').st_size)
#
# mod_time = os.stat('testdata.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))
#
# for dirpath, dirnames, filenames in os.walk('/Users/dcarson.PATRIOT-TECH/Desktop'):
#     print('Current Path:', dirpath)
#     print('--------------')
#     print('Directories:', dirnames)
#     print('--------------')
#     print('Files', filenames)
#     print(' ')

os.chdir('/Users/dcarson.PATRIOT-TECH/Documents')

cwd = os.getcwd()

print(os.path.exists('{}/{}'.format(cwd, 'Documents')))
