import os
from flask import Flask
from flask_script import Manager
from settings import settings

# configure your app
app =settings() 


if __name__ == '__main__':
    app.run(debug=True)

