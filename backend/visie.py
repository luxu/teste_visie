# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors
from decouple import config


def conexao():
    return (
        pymysql.connect(
            host=config("HOSTNAME_VISIE"),
            user=config("USERNAME_VISIE"),
            password=config("PASSWORD_VISIE"),
            database=config("DATABASE_VISIE"),
            cursorclass=pymysql.cursors.DictCursor,
        )
    )


def list_data_table(connection, tbl=None):
    sql = r"SELECT * FROM pessoas"
    try:
        with connection.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
    except Exception as err:
        print(f'ERROR..: {err}')
    finally:
        connection.close()


def listar(connection):
    sql = 'SELECT * FROM `pessoas`'
    # list_tables = []
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            # list_all_datas = cursor.fetchall()
            # list_tables.extend(table_name["TABLE_NAME"] for table_name in list_all_datas)
            return cursor.fetchall()
    finally:
        connection.close()


def inserir(connection, data):
    campos_db = ['nome', 'rg', 'cpf', 'data_nascimento', 'data_admissao', 'funcao']
    data = [str(r[1]) for r in data.items()]

    sql = "INSERT INTO pessoas"
    sql += f' ({", ".join((campos_db))}) VALUES '
    sql += "(%s, %s, %s, %s, %s, %s)"

    with connection.cursor() as cursor:
        cursor.execute(sql, data)
    connection.commit()


def alterar(connection, data):
    campos_db = ['nome', 'rg', 'cpf', 'data_nascimento', 'data_admissao', 'funcao', 'id_pessoa']
    data = [str(r[1]) for r in data.items()]

    sql = "UPDATE pessoas "
    sql += f'SET {campos_db[0]}="{data[0]}", {campos_db[1]}="{data[1]}", {campos_db[2]}="{data[2]}", '
    sql += f'{campos_db[3]}="{data[3]}", {campos_db[4]}="{data[4]}", {campos_db[5]}="{data[5]}"'
    sql += f" WHERE {campos_db[6]}={data[6]}"

    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
    except pymysql.err.OperationalError as err:
        return err
    connection.commit()


def deletar(connection, id_pessoa):
    sql = f"DELETE FROM pessoas WHERE id_pessoa={id_pessoa}"
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
    except pymysql.err.OperationalError as err:
        return err
    connection.commit()


def consultar_por_id(connection, id_pessoa):
    sql = f"SELECT * FROM `pessoas` WHERE id_pessoa={id_pessoa}"
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchone()
    finally:
        connection.close()


def consultar_por_nome(connection, nome):
    sql = f"SELECT * FROM `pessoas` WHERE nome like '%{nome}%'"
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        connection.close()
