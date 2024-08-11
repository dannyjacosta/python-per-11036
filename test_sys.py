import sys
import os
import os.path
import time

# SYS Module
for arg in sys.argv:
    print(arg)

print('The executable path is ' + sys.executable)
print('The Python version is ' + sys.version)
print('The executing platform is ' + sys.platform)
print('The default encoding is ' + sys.getdefaultencoding())


# OS module

print('The Current Working Directory is ' + os.getcwd())

if not os.path.exists('delete-me'):
    os.mkdir('delete-me')

if not os.path.exists('delete-me-later.txt'):
    with open('delete-me-later.txt', 'w') as file:
        pass

time.sleep(3)
os.rename('delete-me-later.txt', 'delete-me.txt')
os.rmdir('delete-me')
os.remove('delete-me.txt')


print(os.path.abspath('./constantes.py'))
print(os.path.basename('./constantes.py'))
print('File constantes.py exists? ' + str(os.path.exists('./constantes.py')))
print('constantes.txt is a file? ' + str(os.path.isfile('./constantes.txt')))
print('.venv is a directory? ' + str(os.path.isdir('.venv')))
