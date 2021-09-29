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


def sign_in(login, password):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM `users` WHERE userLogin=\'" + str(login) + "\'AND userPassword=\'" + str(password) + "\'")
    cnx.disconnect_db()
    return cursor.fetchall()


def if_login_exists(login):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM `users` WHERE userLogin=\'" + str(login) + "\'")
    cnx.disconnect_db()
    if len(cursor.fetchall()) != 0:
        return True
    else:
        return False
