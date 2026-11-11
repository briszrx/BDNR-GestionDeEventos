


def populate_cassandra():
    # 1. Se abre cada CSV de data/Cassandra/ con csv.DictReader, que entrega cada fila como diccionario.
    # 2. Se convierten los tipos antes de insertar (int(), float(), fechas con datetime).
    # 3. Se prepara una sentencia INSERT por tabla con session.prepare(), como en el laboratorio.
    # 4. Cassandra modela una tabla por consulta: el mismo dato se inserta en todas las tablas que lo necesiten.
    # 5. Se recorren las filas y se insertan en lotes pequeños con BatchStatement (como execute_batch de la tarea de logística).
    # 6. Las tablas de resumen (actividad por categoría, eventos por disponibilidad) se calculan a partir de
    #    los eventos, asistencias, cancelaciones e interacciones ya generados.
    # 7. Se valida con un SELECT / conteo por tabla.
    pass
 
 
def populate_mongodb():
    # 1. Se abre el CSV/JSON de data/Mongo/ (csv.DictReader o json.load).
    # 2. Se convierten los tipos (precio a float, cupos a int, fechas a datetime) y se arma un documento por evento.
    # 3. Los arreglos anidados de agenda y de boletaje se generan con Faker dentro de cada documento.
    # 4. Se mantiene consistencia entre cupos disponibles, asistentes registrados y capacidad de la sede.
    # 5. Se insertan las colecciones con insert_many(), como en el laboratorio de PyMongo.
    # 6. Se crean los índices pensados para las consultas del proyecto.
    # 7. Se valida con count_documents().
    pass
 
 
def populate_dgraph():
    # 1. Se aplica el schema (predicados, tipos e índices) con client.alter(pydgraph.Operation(schema=schema)).
    #    alter() se usa directo sobre client, sin txn().
    # 2. Se leen los CSV de data/Dgraph/ con csv.DictReader. Los valores llegan como texto: se convierten con
    #    int(), float() o datetime en ISO 8601 antes de enviarlos.
    # 3. Se arma una lista de diccionarios por tipo de nodo (usuarios, eventos, temas, organizadores),
    #    cada uno con "uid": "_:etiqueta" (blank node) y "dgraph.type".
    # 4. Se insertan los nodos con txn.mutate(set_obj=lista), txn.commit() y txn.discard() en finally.
    #    Se guarda res.uids, que relaciona cada etiqueta con el UID real asignado por Dgraph.
    # 5. Se leen los CSV de relaciones (amistades, asistencias, intereses, recomendaciones, temas, organizador).
    # 6. Se crean las aristas con esos UID: {"uid": uids[origen], "relacion": [{"uid": uids[destino]}]},
    #    en una mutación por tipo de relación.
    # 7. La red de amigos se genera con amigos de amigos, usuarios con 2+ eventos en común,
    #    usuarios inactivos y usuarios recurrentes de un mismo organizador, para que las 8 consultas tengan datos.
    # 8. Para volver a poblar sin duplicar, se limpia antes con drop_all (pidiendo confirmación, como en la actividad).
    # 9. Se valida con una consulta type(...) usando client.txn(read_only=True).query().
    pass
 
 
if __name__ == "__main__":
    populate_cassandra()
 
    populate_mongodb()
 
    populate_dgraph()
 