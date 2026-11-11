import os
 
from cassandra.cluster import Cluster, NoHostAvailable
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
import pydgraph
 

# CONFIGURACIÓN

CASSANDRA_IPS = os.getenv("CASSANDRA_CLUSTER_IPS", "127.0.0.1")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
MONGO_DB = os.getenv("MONGO_DB", "gestion_eventos")
DGRAPH_HOST = os.getenv("DGRAPH_HOST", "localhost:9080")
 

_cluster = None
_mongo_client = None
_dgraph_stub = None
 
 

# CASSANDRA

def get_cassandra_session():
    global _cluster
    try:
        _cluster = Cluster(CASSANDRA_IPS.split(","))
        session = _cluster.connect()
        print("Cassandra: conectado")
        return session
    except NoHostAvailable:
        print("Cassandra: error de conexión (¿contenedor en el puerto 9042?)")
        raise
 
 

# MONGODB

def get_mongo_connection():
    global _mongo_client
    try:
        _mongo_client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
        _mongo_client.admin.command("ping")
        print("MongoDB: conectado")
        return _mongo_client[MONGO_DB]
    except (ConnectionFailure, ServerSelectionTimeoutError):
        print("MongoDB: error de conexión (¿contenedor en el puerto 27017?)")
        raise
 
 
# DGRAPH

def get_dgraph_connection():
    global _dgraph_stub
    _dgraph_stub = pydgraph.DgraphClientStub(DGRAPH_HOST)
    client = pydgraph.DgraphClient(_dgraph_stub)
    try:
        client.txn(read_only=True).query("{ q(func: type(User), first: 1) { uid } }")
        print("Dgraph: conectado")
        return client
    except Exception:
        print("Dgraph: error de conexión (¿contenedor con el puerto 9080 publicado?)")
        _dgraph_stub.close()
        raise
 

# CERRAR CONEXIONES

def close_connections():
    if _cluster:
        _cluster.shutdown()
    if _mongo_client:
        _mongo_client.close()
    if _dgraph_stub:
        _dgraph_stub.close()
 
 
# PRUEBA 

if __name__ == "__main__":
    get_cassandra_session()
    get_mongo_connection()
    get_dgraph_connection()
    close_connections()
    print("Todas las conexiones funcionan y se cerraron correctamente.")
 