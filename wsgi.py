# wsgi.py
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import server as application  

if __name__ == "__main__":
    application.run()
