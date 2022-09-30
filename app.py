from arango import ArangoClient

# Initialize the client for ArangoDB.
client = ArangoClient(hosts="http://localhost:8529")

# Connect to "_system" database as root user.
db = client.db("nosql", username="root", password="password")

# Execute an AQL query and iterate through the result cursor.
cursor = db.aql.execute("FOR doc IN learning RETURN doc")

print([document for document in cursor]) 
