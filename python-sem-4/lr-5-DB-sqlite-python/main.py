'''# CRUD - Create, Read, Update, Delete
Задание:
1) отрефакторить код:
для каждой функции создать свою python функцию
1.1 параметризация 
1.2 обработка исключений (можно отлавливать SQlite3Error общее или какие-то специфические исключения)
- при выборке данных отсутствие таблицы
- при добавлении
- при обновлении и удалении
'''

from sqlite3 import OperationalError
import sqlite3


# CREATE
def create_query(table_name: str):
    conn = sqlite3.connect('zhukov.db')
    c = conn.cursor()
    c.execute(f'''CREATE TABLE {table_name}
              (id int, height real, name text, deleted bool, created_at DATETIME)'''
              )
    conn.commit()
    print(f'Table "{table_name}" is created')
    conn.close()


# READ (SELECT)
def read_query(tbl_name: str):
    conn = sqlite3.connect('zhukov.db')
    c = conn.cursor()
    try:
        crud_res = c.execute(f'SELECT * FROM {tbl_name}')
        for r in crud_res:
            print(r)

    except OperationalError as e:
        print('Table does not exist:', e)
        try:
            c.execute(f'''CREATE TABLE {tbl_name}
                (id int, height real, name text, deleted bool, created_at DATETIME)'''
                      )
        except:
            print('Error. Table was not created')
    conn.close()


# INSERT
def insert_query(tbl_name: str):
    conn = sqlite3.connect('zhukov.db')
    c = conn.cursor()
    try:
        c.execute(
            f'''INSERT INTO {tbl_name} values ('1', 1.65, 'user', 1, '2022-05-10 13:31:00')'''
        )
        conn.commit()
        crud_res = c.execute(f'SELECT * FROM {tbl_name}')
        for r in crud_res:
            print(r)
    except OperationalError as e:
        print('No such table exists', e)
    conn.close()


# UPDATE
def update_query(tbl_name):
    conn = sqlite3.connect('zhukov.db')
    c = conn.cursor()
    c.execute(f'UPDATE {tbl_name} SET deleted = 1 WHERE id == 1')
    conn.commit()
    crud_res = c.execute(f'SELECT * FROM {tbl_name}')
    for r in crud_res:
        print(r)
    conn.close()


# DELETE
def delete_query(tbl_name: str):
    conn = sqlite3.connect('zhukov.db')
    c = conn.cursor()
    print('DELETE query')
    c.execute(f"DELETE FROM {tbl_name} WHERE name == 'user'")
    conn.commit()
    crud_res = c.execute(f'SELECT * FROM {tbl_name}')
    for r in crud_res:
        print(r)
    conn.close()


while True:
    operation_name = str(
        input(
            "Choose one of the operations: CREATE (table), SELECT, UPDATE, DELETE: "
        ))
    if (operation_name == 'CREATE'):
        table_name = str(input('Enter table name: '))
        create_query(table_name)

    elif (operation_name == 'SELECT'):
        select_table_name = str(input('(select)Enter table name:'))
        read_query(select_table_name)

    elif (operation_name == 'INSERT'):
        insert_table_name = str(input('(insert)Enter table name: '))
        insert_query(insert_table_name)

    elif (operation_name == 'UPDATE'):
        update_table_name = str(input('(update)Enter table name: '))
        update_query(update_table_name)

    elif (operation_name == 'DELETE'):
        delete_table_name = str(input('(delete)Enter table name: '))
        delete_query(delete_table_name)

    if (operation_name == ''):
        break
