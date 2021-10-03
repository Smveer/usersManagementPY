# The mysql queries
import sys
from classes.Bdd import *

sys.path.append("../../usersManagementPY")
import functions


# Show all user
def get_all_users():
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "SELECT * FROM users"
    cursor.execute(query)
    cnx.connection.close()
    return cursor.fetchall()


# Show all user with ID
def get_user_with_id(id):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE userId=%s"
    values = (id,)
    cursor.execute(query, values)
    cnx.connection.close()
    return cursor.fetchall()


# Connection user in login step
def get_user_with_login_password(login, password):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE userLogin=%s AND userPassword=%s"
    values = (login, functions.create_hash(password))
    cursor.execute(query, values)
    cnx.connection.close()
    return cursor.fetchall()


# verification login exist in login step
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


# verification email exist in login step
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


# insert user information to the DataBase
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


# delete user in the DataBase
def delete_user_with_id(id):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "DELETE  FROM users WHERE userId=%s"
    values = (id,)
    cursor.execute(query, values)
    cnx.connection.commit()
    cnx.connection.close()


# change the password if it's expired
def update_pwd(pwd, id):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "UPDATE users SET userPassword=%s, userPasswordExpiry=%s WHERE userId=%s"
    values = (pwd, functions.set_pwd_expiry(), id)
    cursor.execute(query, values)
    cnx.connection.commit()
    cnx.connection.close()


# change department
def update_departement(dep, id):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "UPDATE users SET userDepartement=%s WHERE userId=%s"
    values = (dep, id)
    cursor.execute(query, values)
    cnx.connection.commit()
    cnx.connection.close()


# search user by lastname
def search_by_lastname(lastname):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE userLastName LIKE %s"
    values = (lastname + "%",)
    cursor.execute(query, values)
    cnx.connection.close()
    return cursor.fetchall()


# search user by firstname
def search_by_firstname(firstname):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE userFirstName LIKE %s"
    values = (firstname + "%",)
    cursor.execute(query, values)
    cnx.connection.close()
    return cursor.fetchall()


# search user by email
def search_by_email(email):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE userEmail LIKE %s"
    values = (email + "%",)
    cursor.execute(query, values)
    cnx.connection.close()
    return cursor.fetchall()


# search user by date of birth
def search_by_dob(dob):
    splited_dob = dob.split('-')
    if len(splited_dob) == 3:
        dob = str(splited_dob[2]) + "-" + str(splited_dob[1]) + "-" + str(splited_dob[0])
    else:
        return []
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE userDoB LIKE %s"
    values = (dob + "%",)
    cursor.execute(query, values)
    cnx.connection.close()
    return cursor.fetchall()


# search user by place/country
def search_by_cob(cob):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE userCoB LIKE %s"
    values = (cob + "%",)
    cursor.execute(query, values)
    cnx.connection.close()
    return cursor.fetchall()


# update user information
def update_user(login, lastname, firstname, email, dob, cob, id):
    cnx = Bdd()
    cursor = cnx.connection.cursor(dictionary=True)
    query = "UPDATE users SET " \
            "userLogin=%s, " \
            "userLastName=%s, " \
            "userFirstName=%s, " \
            "userEmail=%s, " \
            "userDoB=%s, " \
            "userCoB=%s " \
            "WHERE userId=%s"
    values = (login, lastname, firstname, email, dob, cob, id)
    cursor.execute(query, values)
    cnx.connection.commit()
    cnx.connection.close()
