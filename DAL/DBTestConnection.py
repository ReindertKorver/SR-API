from DAL.DatabaseConfig import DatabaseConfig
import json

class DBTestConnection:
    @staticmethod
    def connectAsTest():
        db = DatabaseConfig("localhost", "sr-api", "root", "", "3306")
        conn = db.getDBConnection()
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM users")

        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        return json.dumps(myresult)
