from flask import Flask
from neo4j import GraphDatabase

app = Flask(__name__)

from app import routes
