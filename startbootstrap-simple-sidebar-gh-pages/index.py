# import libraries
import flask
from flask import render_template
from flask import Flask, request




app = Flask(__name__)

@app.route('/')
def index():
   #return render_template('index.html')  # this line only displays files in the templates sub directory.  To display from other directories, see below
   return flask.send_from_directory(".", path="index.html")


if __name__ == '__main__':
   app.run()
