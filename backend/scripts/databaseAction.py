import psycopg2
from psycopg2.extras import RealDictCursor
class querySQL:
    def __init__(self):
        self.conn = psycopg2.connect(database = "okc",
                            host = "localhost",
                            user = "okcapplicant",
                            password = "thunder",
                            port = "5432")
        self.cursor = self.conn.cursor()


    def insert_From_Py(self, game_values, query):
        self.cursor.execute(query, game_values)
        self.conn.commit()


    def truncate_From_Py(self, query):
        self.cursor.execute(query)
        self.conn.commit()


    def retrieve_From_Py(self, playerId):
        try:
            cur = self.conn.cursor(cursor_factory=RealDictCursor)
            select_statement = "SELECT * FROM player where playerId = %s"
            cur.execute(select_statement, (playerId,))
            return cur.fetchall()
        except psycopg2.DatabaseError as db_err:
            print("A database error occurred:", db_err)
        except psycopg2.InterfaceError as intf_err:
            print("An interface error occurred:", intf_err)
        except Exception as err:
            print("An exception has occurred:", err)
            print("Exception type:", type(err))

    def retrieve_Shot_From_Py(self, playerId):
        try:
            cur = self.conn.cursor(cursor_factory=RealDictCursor)
            select_statement = "SELECT * FROM shot where playerId = %s"
            cur.execute(select_statement, (playerId,))
            return cur.fetchall()
        except psycopg2.DatabaseError as db_err:
            print("A database error occurred:", db_err)
        except psycopg2.InterfaceError as intf_err:
            print("An interface error occurred:", intf_err)
        except Exception as err:
            print("An exception has occurred:", err)
            print("Exception type:", type(err))


    def retrieve_Game_From_Py(self,gameId):
        try:
            cur = self.conn.cursor(cursor_factory=RealDictCursor)

            select_statement = "SELECT * FROM game where gameId = %s"

            cur.execute(select_statement, (gameId,))
            return cur.fetchall()
        except psycopg2.DatabaseError as db_err:
            print("A database error occurred:", db_err)
        except psycopg2.InterfaceError as intf_err:
            print("An interface error occurred:", intf_err)
        except Exception as err:
            print("An exception has occurred:", err)
            print("Exception type:", type(err))
