#!/usr/bin/env python
from flask import Flask, request, render_template
import json
import random

# create app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("input.html")

    elif request.method == 'POST':
        yourname = request.form.get('yourname')
        with open('/home/16c7x/mysite/data.json') as data_file:
          data = json.load(data_file)
        x = random.randint(0,6)
        line = data["insults"][x]["line"]

        return render_template("answer.html", yourname = yourname, line = line)

# run app
if __name__ == '__main__':
    app.run()
