import py2neo 
from py2neo import Graph,Node,Relationship

# py2neo.authenticate("localhost:7474", "neo4j", "638085") 
# graph = Graph("http://localhost:7474/db/data/") 
graph = Graph("http://localhost:7474",auth=("neo4j","638095"))

def creatNodeWithLabelProperties(): 
    print("Start - Creating Node with Label and Properties")
     
    #tx = graph.begin()
    #node1 = Node("用户", name="李白") #Below is a Node with 2 Label and 2 properties node2 = Node("FirstLabel", "SecondLabel",name="MyPythonNode2", neo4j_version="2.2")   
    #node2 = Node("用户", "SecondLabel",name="杜甫")
    node3 = Node("用户", "SecondLabel",name="王维")
    #resultNode1 = tx.create(node1)
    #resultNode2 = tx.create(node2)
    #tx.commit()
    graph.create(node3)
    #
    # for index in range(len(resultNodes)): 
    #    print("Created Node - ", index, ", ", resultNodes[index]) 
    # print("Created Node - ", index, ", ", resultNode1)
    # print("Created Node - ", index, ", ", resultNode2)
    
    print("End - Creating Node with Label and Properties")

if __name__ == '__main__':
    print("Start Creating Nodes") 
    creatNodeWithLabelProperties()
    print("End Creating Nodes")