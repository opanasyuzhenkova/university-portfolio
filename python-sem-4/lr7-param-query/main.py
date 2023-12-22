import sqlite3
import functools
import logging
import pendulum
from User import User


def log_time():
    '''
  Time function. Used for logging
  '''
    return pendulum.now('Europe/Moscow').to_datetime_string()


def deco(func=None, *, level=logging.INFO):
    """
  Decorator that logs CRUD operations

  Keyword arguments:
  func -- the name of the function to be decorated
  * -- all parameters must be passed by name (f.e. key = value)
  level -- logger with the specified importance level set (f.e. DEBUG,
  INFO, WARNING, ERROR, CRITICAL )

  """
    if func is None:
        return lambda func: deco(
            func, level=level
        )  # привязывание декоратора к декорируемой функции

    @functools.wraps(func)
    def inner(*args, **kwargs):
        logging.basicConfig(level=level, filename='logs.log')
        logging.info(f'|{log_time()}|-({func.__name__})')
        result = func(*args, **kwargs)
        return result

    return inner


def connect_to_db(db_name: str) -> sqlite3.Connection:
    """Database connection function.

    Keyword arguments:
    db_name -- name of database

  """
    print('Database connection...')
    try:
        conn = sqlite3.connect(db_name)
        print('DB connection established successfully')
    except sqlite3.DatabaseError:
        print(f'Not connect to DB: {db_name}')
    return conn


# read query (select * from table)
@deco(level=logging.ERROR)
def read_query(conn: sqlite3.Connection, table_name, col_name="*"):
    try:
        res = conn.execute(f"SELECT {col_name} FROM {table_name}")
        print('*' * 25)
        for i in res:
            print(i)
        print('*' * 25)
        conn.commit()
    except sqlite3.OperationalError as e:
        print('Error:', e)
        logging.error(f'|{log_time()}|:{e}')
    else:
        logging.info(f'[{log_time()}|:Done')


# update query (update table_name SET column1 = value 1, column2 = value 2,..) where _condition_
@deco(level=logging.INFO)
def update_query(conn: sqlite3.Connection,
                 table_name: str,
                 values,
                 condition: str = None):
    try:
        print('Update table:')
        if condition:
            conn.execute(f'UPDATE {table_name} SET {values} WHERE {condition}')
        else:
            conn.execute(f'UPDATE {table_name} SET {values}')
        conn.commit()
        read_query(conn, table_name)
    except sqlite3.OperationalError as e:
        print('Error:', e)
        logging.error(f'|{log_time}|:{e}')


# create query (create table table_name (column1 datatype, column2 datatype, column3 datatype ...)
@deco(level=logging.INFO)
def create_query(conn: sqlite3.Connection, queries=None):
    try:
        read_str = "SELECT * FROM user"  # попытка вывести таблицу
        crud_res = conn.execute(read_str)
        for r in crud_res:
            print(r)

    except sqlite3.OperationalError:  # если таблицы нет - создаём
        print('No such table. Table creation:')
        try:
            values = []
            columns = ['id', 'height', 'name', 'del', 'created']
            insert_str = f"INSERT INTO user VALUES ("
            for i in columns:
                insert_str += ':' + i + ','
            insert_str = insert_str[:-1] + ');'

            #print(insert_str)

            p = 0
            for q in queries:
                if ("CREATE TABLE" in q):  # выполняем создание
                    conn.execute(q)
                else:
                    values.append({})  # собираем словарь значений
                    for i in range(len(columns)):
                        try:
                            values[p].update({columns[i]: q[i]})
                        except:
                            values[p].update({columns[i]: None})
                    p += 1

            #print(*values, sep='\n')

            conn.executemany(insert_str, values)  # выполняем запрос
            conn.commit()
            try:
                read_str = "SELECT * FROM user"  # пытаемся вывести снова
                crud_res = conn.execute(read_str)
                for r in crud_res:
                    print(r)
            except sqlite3.OperationalError:  # если не получатся поднимаем ошибку
                print('Failed to create table')

        except Exception as e:
            print('Error! Table not created', e)


# insert query (INSERT INTO table_name (column1, column2, column3...) VALUES (v1, v2..);
@deco(level=logging.INFO)
def insert_query(conn: sqlite3.Connection, table_name: str, *values):
    try:
        print('Adding data to a table:')
        vals = []
        columns = [str(i) for i in range(len(values[0]))]
        insert_str = f"INSERT INTO {table_name} VALUES ("
        for i in columns:
            insert_str += ':' + i + ','
        insert_str = insert_str[:-1] + ');'

        #print(insert_str)

        for q in range(len(values)):
            vals.append({})
            for i in range(len(columns)):
                try:
                    vals[q].update({columns[i]: values[q][i]})
                except:
                    vals[q].update({clmns[i]: None})

        conn.executemany(insert_str, vals)
        conn.commit()
        read_query(conn, table_name)

    except Exception as e:
        print('Error. Insert failed', e)
        logging.error(f'|{log_time}|:{e}')


# delete query (DELETE FROM table_name WHERE condition)
@deco(level=logging.INFO)
def delete_query(conn: sqlite3.Connection,
                 table_name: str,
                 condition: str = None):
    try:
        print('Deleting data from table:')
        if condition:
            conn.execute(f'DELETE FROM {table_name} WHERE {condition}')
        else:
            conn.execute(f'DELETE FROM {table_name}'
                         )  # если нет условия удаляем всё из таблицы
        conn.commit()
        read_query(conn, table_name)
    except sqlite3.OperationalError as e:
        print('Error:', e)
        logging.error(f'[{log_time}]:{e}')


def main():
    # db_name = input('Enter database name: ')
    db_name = ':memory:'
    db_handler = connect_to_db(db_name)

    create_query(db_handler,
                 queries=[
                     '''CREATE TABLE user
                 (id int, height real, name text, deleted bool, created DATETIME)''',
                     ('1', 1.81, 'user1', 0),
                     ('2', 1.82, 'user2', 0, '2022-03-02 14:03:22'),
                     ('3', 1.83, 'user3', 0, '2022-03-02 14:03:24'),
                     ('4', 1.84, 'user4', 0, '2022-03-02 14:03:25'),
                     ('5', 1.85, 'user5', 1, '2022-03-02 14:03:28'),
                     ('100', 1.90, 'Nick', 0, '2022-03-02 14:03:28')
                 ])

    update_query(db_handler, "user", "deleted = 1, created = NULL", "id == 3")

    insert_query(db_handler, "user",
                 ('6', 1.62, 'userS', 0, '2022-05-24 10:47:29'),
                 ('7', 1.92, 'user6', 0, '2022-05-20 11:47:29'))

    delete_query(db_handler, "user", "deleted == 1")


main()
