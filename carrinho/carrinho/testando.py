import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print BASE_DIR
print (BASE_DIR + '/Templates').replace('\\','/')