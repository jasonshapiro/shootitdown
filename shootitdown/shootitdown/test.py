import os

print os.getcwd()
print os.path.dirname(__file__)
print os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/')
