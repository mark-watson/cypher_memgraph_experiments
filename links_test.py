from gqlalchemy import Memgraph, models
models.IGNORE_SUBCLASSNOTFOUNDWARNING = True
from pprint import pprint

# Make a connection to the database
memgraph = Memgraph(host='127.0.0.1', port=7687)

def execute_and_fetch(query):
    print(f"Query: {query}")
    results = memgraph.execute_and_fetch(query)
    pprint(list(results))
    return list(results)


execute_and_fetch("MATCH (n) DETACH DELETE n")
execute_and_fetch("CREATE (n:Person {name: 'Andy', title: 'Developer', age: 30})")
execute_and_fetch("CREATE (n:Company {name: 'Amazon', location: 'USA'})")
execute_and_fetch("CREATE p = (:Person {name:'Andy'})-[:ORDERS_AT]->(:Company {name: 'Amazon'})")

execute_and_fetch("CREATE p = (:Person {name:'Andy'})-[:WORKS_AT]->(:Company {name: 'Neo4j'})<-[:WORKS_AT]-(:Person {name: 'Michael'}) RETURN p")

execute_and_fetch("MATCH (n) RETURN n")
execute_and_fetch("MATCH (n:Person) RETURN n")
execute_and_fetch("MATCH (:Person {name: 'Andy'})-[r]-() RETURN r")