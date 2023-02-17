from gqlalchemy import Memgraph

# Make a connection to the database
memgraph = Memgraph(host='127.0.0.1', port=7687)

# Delete all nodes and relationships
query = "MATCH (n) DETACH DELETE n"

# Execute the query
memgraph.execute(query)

# Create a node with the label FirstNode and message property with the value "Hello, World!"
query = """CREATE (n:FirstNode)
           SET n.message = '{message}'
           RETURN 'Node '  + id(n) + ': ' + n.message AS result""".format(message="Hello, World!")

# Execute the query
results = memgraph.execute_and_fetch(query)

# Print the first member
print(list(results)[0]['result'])

