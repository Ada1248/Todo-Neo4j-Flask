from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, SubmitField
from wtforms.validators import InputRequired, Length
from py2neo import Graph, Node, Relationship
from py2neo.matching import NodeMatcher
from config import database_uri, database_user, database_password
import os

graph = Graph(database_uri, auth=(database_user, database_password))

# graph = Graph(database_uri, auth=(os.environ.get("NEO4J_USERNAME"), os.environ.get("NEO4J_PASSWORD")))
matcher = NodeMatcher(graph)

class Task:
    def add_task(self, name, category):
        task = Node('TodoTask', name=name)
        cat = Node('TodoCategory', category=category)
        rel = Relationship(task, 'CONCERN', cat)
        graph.create(rel)
        print(rel)

    def get_all_tasks(self):
         query = '''
            MATCH (task:TodoTask)-[:CONCERN]->(cat:TodoCategory)
            RETURN task.name as name, cat.category as category
            '''
         return graph.run(query)

    def delete_tasks(self):
        query = '''
        MATCH (task:TodoTask)-[rel:CONCERN]->(cat:TodoCategory)
        DELETE task, rel, cat
        '''
        return graph.run(query)
