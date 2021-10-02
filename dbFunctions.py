import sys
from classes.Bdd import *

sys.path.append("../../usersManagementPY")
import functions


def get_all_users():
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "SELECT * FROM users"
    cursor.execute(query)
    cnx.connection.close()
    return cursor.fetchall()


def get_user_with_id(id):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE userId=%s"
    values = (id,)
    cursor.execute(query, values)
    cnx.connection.close()
    return cursor.fetchall()


def get_user_with_login_password(login, password):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE userLogin=%s AND userPassword=%s"
    values = (login, functions.create_hash(password))
    cursor.execute(query, values)
    cnx.connection.close()
    return cursor.fetchall()


def if_login_exists(login):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE userLogin= %s"
    values = (login,)
    cursor.execute(query, values)
    cnx.connection.close()
    if len(cursor.fetchall()) != 0:
        return True
    else:
        return False


def if_email_exists(email):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE userEmail= %s"
    values = (email,)
    cursor.execute(query, values)
    cnx.connection.close()
    if len(cursor.fetchall()) != 0:
        return True
    else:
        return False


def insert_user(login, lastname, firstname, email, password, dob, cob):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "INSERT INTO users (" \
            "userLogin, " \
            "userLastName, " \
            "userFirstName, " \
            "userEmail, " \
            "userPassword, " \
            "userDoB, " \
            "userCoB, " \
            "userDepartement) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (
        login,
        lastname,
        firstname,
        email,
        password,
        dob,
        cob,
        "worker"
    )
    cursor.execute(query, values)
    cnx.connection.commit()
    cnx.connection.close()


def delete_user_with_id(id):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "DELETE  FROM users WHERE userId=%s"
    values = (id,)
    cursor.execute(query, values)
    cnx.connection.commit()
    cnx.connection.close()


def update_pwd(pwd, id):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "UPDATE users SET userPassword=%s, userPasswordExpiry=%s WHERE userId=%s"
    values = (pwd, functions.set_pwd_expiry(), id)
    cursor.execute(query, values)
    cnx.connection.commit()
    cnx.connection.close()


def update_departement(dep, id):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "UPDATE users SET userDepartement=%s WHERE userId=%s"
    values = (dep, id)
    cursor.execute(query, values)
    cnx.connection.commit()
    cnx.connection.close()

# recherche
