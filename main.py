from connect import (
    get_cassandra_session,
    get_mongo_connection,
    get_dgraph_connection,
    close_connections,
)


def menu_cassandra(session):
    while True:
        print("\nCassandra")
        print("1. Últimas 15 interacciones de un usuario")
        print("2. Eventos de una sede en un rango de fechas")
        print("3. Historial de cambios de un evento (filtro opcional por tipo de cambio)")
        print("4. Interacciones de un usuario por rango de fechas y tipo de interacción")
        print("5. Visitas y asistencias de un usuario en una sede por rango de fechas")
        print("6. Historial de eventos a los que asistió un usuario")
        print("7. Actividad de una categoría de eventos en un rango de fechas")
        print("8. Eventos por disponibilidad (disponible / lleno)")
        print("9. Regresar al menú principal")

        option = int(input("\nSelecciona una de las consultas: "))

        if option == 1:
            print("Consulta 1 Cassandra")
        elif option == 2:
            print("Consulta 2 Cassandra")
        elif option == 3:
            print("Consulta 3 Cassandra")
        elif option == 4:
            print("Consulta 4 Cassandra")
        elif option == 5:
            print("Consulta 5 Cassandra")
        elif option == 6:
            print("Consulta 6 Cassandra")
        elif option == 7:
            print("Consulta 7 Cassandra")
        elif option == 8:
            print("Consulta 8 Cassandra")
        elif option == 9:
            break
        else:
            print("No se puede eso. Intenta otra vez")


def menu_mongo(db):
    while True:
        print("\nMongoDB")
        print("1. Detalles de un evento (nombre exacto o parcial)")
        print("2. Eventos por categoría (rango de fechas opcional)")
        print("3. Eventos de un organizador (filtro opcional por estado)")
        print("4. Cartelera de una sede (próximos eventos)")
        print("5. Próximos eventos en una ciudad")
        print("6. Búsqueda libre por palabras clave")
        print("7. Agenda de un evento")
        print("8. Opciones de boletaje de un evento")
        print("9. Regresar al menú principal")

        option = int(input("\nSelecciona una de las consultas: "))

        if option == 1:
            print("Consulta 1 MongoDB")
        elif option == 2:
            print("Consulta 2 MongoDB")
        elif option == 3:
            print("Consulta 3 MongoDB")
        elif option == 4:
            print("Consulta 4 MongoDB")
        elif option == 5:
            print("Consulta 5 MongoDB")
        elif option == 6:
            print("Consulta 6 MongoDB")
        elif option == 7:
            print("Consulta 7 MongoDB")
        elif option == 8:
            print("Consulta 8 MongoDB")
        elif option == 9:
            break
        else:
            print("No se puede eso. Intenta otra vez")


def menu_dgraph(client):
    while True:
        print("\nDgraph")
        print("1. Recomendar eventos de una categoría según la red de amigos")
        print("2. Patrones de co-asistencia (posibles amigos)")
        print("3. Eventos recomendados por intereses y amigos")
        print("4. Fidelización de un organizador y propagación entre amigos")
        print("5. Usuarios similares por temas y categorías")
        print("6. Amigos inactivos en una categoría (últimos 3 meses)")
        print("7. Usuarios nodo clave que recomendaron un evento")
        print("8. Interacciones directas e indirectas usuario-evento")
        print("9. Regresar al menú principal")

        option = int(input("\nSelecciona una de las consultas: "))

        if option == 1:
            print("Consulta 1 Dgraph")
        elif option == 2:
            print("Consulta 2 Dgraph")
        elif option == 3:
            print("Consulta 3 Dgraph")
        elif option == 4:
            print("Consulta 4 Dgraph")
        elif option == 5:
            print("Consulta 5 Dgraph")
        elif option == 6:
            print("Consulta 6 Dgraph")
        elif option == 7:
            print("Consulta 7 Dgraph")
        elif option == 8:
            print("Consulta 8 Dgraph")
        elif option == 9:
            break
        else:
            print("No se puede eso. Intenta otra vez")


def main():
    print("Conectando\n")
    cassandra_session = get_cassandra_session()
    mongo_db = get_mongo_connection()
    dgraph_client = get_dgraph_connection()

    while True:
        print("\nMenu principal")
        print("1. Cassandra")
        print("2. MongoDB")
        print("3. Dgraph")
        print("4. Salir")

        main_option = int(input("\nSelecciona una base de datos: "))

        if main_option == 1:
            menu_cassandra(cassandra_session)
        elif main_option == 2:
            menu_mongo(mongo_db)
        elif main_option == 3:
            menu_dgraph(dgraph_client)
        elif main_option == 4:
            print("Saliendo de Gestión de Eventos")
            close_connections()
            break
        else:
            print("No se puede eso. Intenta otra vez.")


if __name__ == "__main__":
    main()