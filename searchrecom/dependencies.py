from nameko.extensions import DependencyProvider

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
from mysql.connector.pooling import MySQLConnectionPool


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
    
    def get_service_by_type(self, type_id):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM services WHERE id_service_type = %s", (type_id,))
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def get_service_by_type_lokasi(self, type_id, lokasi_id):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM services WHERE id_service_type = %s and id_lokasi = %s", (type_id, lokasi_id))
        result = cursor.fetchall()
        cursor.close()
        return result

    def add_service(self, nama, id_lokasi, url, id_service_type):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("INSERT INTO services (nama, id_lokasi, url, id_service_type) VALUES (%s, %s, %s, %s)", (nama, id_lokasi, url, id_service_type))
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
                'url' : url,
                'id_service_type' : id_service_type
            }
        }
    
    def add_service_type(self, nama):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("INSERT INTO service_type (nama) VALUES (%s)", (nama,))
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
        cursor.execute("INSERT INTO lokasi (nama) VALUES (%s)", (nama,))
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
    
    def get_service_by_name(self, name):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM services WHERE lower(nama) = lower(%s)", (name,))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def get_service_type_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM service_type WHERE id = %s", (id,))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def add_request_error(self, path, error_message, service_id=None, service_type_id=None):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("INSERT INTO requests_error (id_service, path, error_message, id_service_type ) VALUES (%s, %s, %s, %s)", (service_id, path, error_message, service_type_id))
        self.connection.commit()
        id = cursor.lastrowid
        cursor.close()
        return {
            'code' : 200,
            'message' : "Success",
            'data' : {
                'id' : id,
                'service_id' : service_id,
                'error_message' : error_message
            }
        }
    
class Database(DependencyProvider):

    connection_pool = None

    def __init__(self):
        try:
            self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="database_pool",
                pool_size=10,
                pool_reset_session=True,
                host='nameko-example-mysql',
                port='3306',
                # host='localhost',
                database='soa_searchrecom',# nama database nya diganti sesuai dengan services
                user='root',
                password='password'
                # password=''
            )
        except Error as e :
                    self.log.error(f"Error while connecting to MySQL using Connection pool: {e}")
                    raise
        
    def stop(self):
        # Called when the container is stopped
        if self.connection_pool:
            self.connection_pool.close()
            print("MySQL Connection Pool closed")
    
    def get_dependency(self, worker_ctx):
        if self.connection_pool is None:
            raise Exception("Connection pool is not initialized")
        return DatabaseWrapper(self.connection_pool.get_connection())
