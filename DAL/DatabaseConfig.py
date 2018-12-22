import mysql.connector


class DatabaseConfig:
    dbName = "f"
    dbUserName = ""
    dbPassword = ""
    dbServer = ""
    dbPort = ""

    def __init__(self, Server, Name, UserName, Password, Port):
        self.dbName = Name
        self.dbPassword = Password
        self.dbPort = Port
        self.dbServer = Server
        self.dbUserName = UserName

    def getDBConnection(self):
        return mysql.connector.connect(
            host=self.dbServer,
            user=self.dbUserName,
            passwd=self.dbPassword,
            database = self.dbName,
            port=self.dbPort
        )
