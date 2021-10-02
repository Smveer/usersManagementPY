import mysql.connector

#connection to the database
class Bdd(object):
    def __init__(self):
        config = {
            'user': 'admin',
            'password': 'Passw0rd2021',
            'host': 'smveer-database.csl30vkvy9k1.eu-west-3.rds.amazonaws.com',
            'port': 3306,
            'database': 'usrMngmntDb',
            'raise_on_warnings': True
        }
        self.connection = mysql.connector.connect(**config)
