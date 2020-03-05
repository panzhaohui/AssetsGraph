import py2neo 
from py2neo import Graph,Node,Relationship,Rev

py2neo.authenticate("localhost:7474", "neo4j", "638085") 
graph = Graph("http://localhost:7474/db/data/")   

