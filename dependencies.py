from nameko.extensions import DependencyProvider

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        self.connection = connection

# SERVICES
    def get_all_service_type(self):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM service_type")
        result = cursor.fetchall()
        cursor.close()
        return result

    def get_all_service(self):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM services")
        result = cursor.fetchall()
        cursor.close()
        return result 
    
    def get_all_lokasi(self): 
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM lokasi")
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def add_service(self, nama, id_lokasi, api_get_all, id_service_type):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("INSERT INTO services (nama, id_lokasi, api_get_all, id_service_type) VALUES (%s, %s, %s, %s)", (nama, id_lokasi, api_get_all, id_service_type))
        self.connection.commit()
        id = cursor.lastrowid
        cursor.close()
        return {
            'code' : 200,
            'message' : "Success",
            'data' : {
                'id' : id,
                'nama' : nama,
                'id_lokasi' : id_lokasi,
                'api_get_all' : api_get_all,
                'id_service_type' : id_service_type
            }
        }
    
    def add_service_type(self, nama):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("INSERT INTO service_type (nama) VALUES (%s)", (nama))
        self.connection.commit()
        id = cursor.lastrowid
        cursor.close()
        return {
            'code' : 200,
            'message' : "Success",
            'data' : {
                'id' : id,
                'nama' : nama
            }
        }
    
    def add_lokasi(self, nama):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("INSERT INTO lokasi (nama) VALUES (%s)", (nama))
        self.connection.commit()
        id = cursor.lastrowid
        cursor.close()
        return {
            'code' : 200,
            'message' : "Success",
            'data' : {
                'id' : id,
                'nama' : nama
            }
        }
    
    def get_lokasi_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM lokasi WHERE id = %s", (id,))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def get_service_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM services WHERE id = %s", (id,))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def get_service_type_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM service_type WHERE id = %s", (id,))
        result = cursor.fetchone()
        cursor.close()
        return result

class Database(DependencyProvider):

    connection_pool = None

    def __init__(self):
        try:
            self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="database_pool",
                pool_size=10,
                pool_reset_session=True,
                host='localhost',
                database='soa_searchrecom',# nama database nya diganti sesuai dengan services
                user='root',
                password=''
            )
        except Error as e :
            print ("Error while connecting to MySQL using Connection pool ", e)

    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
