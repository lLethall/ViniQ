import sqlite3

def connect_database():
    connection = sqlite3.connect('database/viniq.db')
    cursor = connection.cursor()
    return connection, cursor

def register_data(table, data):
    connection, cursor = connect_database()
    try:
        cursor.execute("BEGIN")
        placeholders = ', '.join(['?'] * len(data))
        columns = ', '.join(data.keys())
        values = tuple(data.values())
        # Sentencia SQL de inserción
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        # Inserta los valores en la base de datos
        cursor.execute(sql, values)

        # Confirma la transacción
        connection.commit()
        result = True

    except sqlite3.Error as error:
        # Maneja los errores de la base de datos aquí
        result = error
        connection.rollback()

    finally:
        # Cierra la conexión a la base de datos
        connection.close()
    print(result)
    return result

def load_data(table):
    connection, cursor = connect_database()
    try:
        cursor.execute(f"SELECT * FROM {table};")
        result = []
        for row in cursor.fetchall():
            result.append({cursor.description[idx][0]: value for idx, value in enumerate(row)})
    except sqlite3.Error as error:
        result = error
    finally:
        connection.close()
    return result