import sys
sys.path.append("../../usersManagementPY")
from classes.Bdd import *


def get_all_users():
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    cursor.execute('SELECT `userId`, `userLogin`, `userEmail`, `userDepartement` FROM `users`')
    results = cursor.fetchall()
    for row in results:
        id = row['userId']
        title = row['userLogin']
        email = row['userEmail']
        departement = row['userDepartement']

        print('%s | %s -> %s --- %s' % (id, title, email, departement))
    cnx.disconnect_db()


def get_user_with_id(id):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    cursor.execute('SELECT `userId`, `userLogin`, `userEmail`, `userDepartement` FROM `users` WHERE userId=' + str(id))
    results = cursor.fetchall()
    for row in results:
        id = row['userId']
        title = row['userLogin']
        email = row['userEmail']
        departement = row['userDepartement']

        print('%s | %s -> %s --- %s' % (id, title, email, departement))
    cnx.disconnect_db()
