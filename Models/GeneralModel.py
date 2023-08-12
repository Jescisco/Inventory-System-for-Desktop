import mariadb as mdb

class GeneralModel:

    def open_conn(self):
        try:
            conn=mdb.connect(host="127.0.0.1",user="root",password="",database="inventory")
            return conn
        except mdb.Error as e:
            message=f"Ocurrió un error: {e}!"
            return message

    def run_set_query(self, query, parameters:tuple):
        conn=self.open_conn()
        cursor=conn.cursor()
        try:
            cursor.execute(query, parameters)
            conn.commit()
            rows=cursor.rowcount
            return rows
        except mdb.Error as e:
            message=f"Ocurrió un error: {e}!"
            return message
        finally:
            cursor.close()
            self.close_conn(conn)

    def run_get_query(self, query, parameters:tuple=()):
        conn=self.open_conn()
        cursor=conn.cursor()
        try:
            cursor.execute(query,parameters)
            conn.commit()
            fetch=cursor.fetchall()
            return fetch
        except mdb.Error as e:
            message=f"Ocurrió un error: {e}!"
            return message
        finally:
            self.close_conn(conn)

    def close_conn(self, conn):
        conn.close()
