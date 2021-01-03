from app import app 
from app.models import Task
from flask import Flask, request, render_template, redirect, url_for
from neo4j import GraphDatabase
from flask_wtf import FlaskForm

# driver = GraphDatabase.driver(uri="bolt://149.156.109.37:7687", auth=("u7pytel", "297881"))
# session = driver.session()

@app.route('/', methods=('GET', 'POST'))
def index():
    tasks = Task().get_all_tasks()
    return render_template('base.html', tasks=tasks)

@app.route('/add_task', methods=('GET', 'POST'))
def add_task():
    name = request.form['name_of_task']
    category = request.form['category']
    Task().add_task(name, category)

    return redirect(url_for('index'))

@app.route('/delete_tasks', methods=('GET', 'POST'))
def delete_tasks():
    Task().delete_tasks()
    return redirect(url_for('index'))
