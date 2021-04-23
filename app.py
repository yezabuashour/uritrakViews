import math
import json
import os
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
	return render_template("test.html")

# ### Can delete this block after JSON is fed in ###
# file = "templates/dj.json"

# with open(file) as f:
# 	data = json.loads(f.read())
# ### Can delete this block after JSON is fed in ###

# def sortFunction(value):
# 	return value.name
# data = sorted(data, key=sortFunction)


def dataManip(data):
	# data = sorted(data, key=sortFunction)
	length = len(data)
	j = []
	for k in range(len(data)):
		j.append(len(data[k]['measurements']))
	return data, length, j


def writeToFile(data):
	f = open("./test.txt", "w")
	f.write(data)
	f.close()
	return
@app.route("/patient")
def home():
	data = request.data
	data = data.decode("utf-8")
	data = json.loads(data)
	data = dataManip(data)
	return render_template("index.html", data=data[0], l=data[1], j=data[2])

@app.route("/patient/<num>")
def id_page(num):
	data = request.data
	data = data.decode("utf-8")
	data = json.loads(data)
	return render_template("patient.html", data=data)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 33507))
	app.run(host="0.0.0.0", port=port)
