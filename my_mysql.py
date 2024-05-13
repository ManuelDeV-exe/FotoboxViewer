import pymysql
import sys

class new_MySql_object():
    def __init__(self, data_myconfig_data):
        self.data = {}
        self.verbunden = False
        self.myconfig_data = data_myconfig_data
        self.my_db = self.connect_to_mysql()

    def connect_to_mysql(self):
        try:
            my_db = pymysql.connect(
                host=self.myconfig_data["mysql_host"],
                user=self.myconfig_data["mysql_username"], 
                password=self.myconfig_data["mysql_password"], 
                database=self.myconfig_data["mysql_database"]
                )
            self.verbunden = True
            return my_db
        except Exception as e:
            print(e) 
            self.verbunden = False

    def create_cursor(self):
        return self.my_db.cursor()
        
    def check_connection(self, count=0):
        try:
            self.close_database()
            self.my_db = self.connect_to_mysql()
            sql_tabel = self.myconfig_data["mysql_sql_tabel"]
            cursor = self.my_db.cursor()
            cursor.execute(f"SELECT * FROM {sql_tabel}")
        except:
            try:
                self.close_database()
            except: print(Exception)
            self.my_db = self.connect_to_mysql()
        finally:
            print('Connection True')

    def update_user_data(self, user, bool):
        sql_tabel = self.myconfig_data["mysql_sql_tabel"]
        self.check_connection()

        cursor = self.my_db.cursor()
        cursor.execute(f"UPDATE {sql_tabel} SET Blockiert = '{bool}' WHERE User = '{user}'")
        self.my_db.commit()

    def read_data(self, user):
        sql_tabel = self.myconfig_data["mysql_sql_tabel"]
        self.check_connection()

        cursor = self.my_db.cursor()
        cursor.execute(f"SELECT * FROM {sql_tabel} WHERE User = '{user}'")
        result = cursor.fetchall()

        return result

    def read_all_data(self):
        sql_tabel = self.myconfig_data["mysql_sql_tabel"]
        self.check_connection()

        cursor = self.my_db.cursor()
        cursor.execute(f"SELECT * FROM {sql_tabel}")
        result = cursor.fetchall()

        self.data = result

    def close_database(self):
        cursor = self.my_db.cursor()

        cursor.close()
        self.my_db.close()

    def remove_all_data(self):
        sql_tabel = self.myconfig_data["mysql_sql_tabel"]
        self.check_connection()
        cursor = self.my_db.cursor()
        cursor.execute(f"DELETE FROM {sql_tabel}")
        self.my_db.commit()

    def delete(self, Spaltenname, Zellenwert):
        sql_tabel = self.myconfig_data["mysql_sql_tabel"]
        database = self.myconfig_data["mysql_database"]

        self.check_connection()
        cursor = self.my_db.cursor()
        cursor.execute(f"DELETE FROM {database}.{sql_tabel} WHERE {sql_tabel}.`{Spaltenname}` = '{Zellenwert}';")
        
        self.my_db.commit()