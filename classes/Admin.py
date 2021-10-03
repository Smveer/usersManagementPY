import sys

import functions

sys.path.append("../../usersManagementPY")

from classes.User import *
from functions import *
from dbFunctions import *


class Admin(User):
    def __init__(self, lastname, firstname, dateBirth, pob, email):
        super().__init__(lastname, firstname, dateBirth, pob, email)

    def list_all_user(self):
        users = get_all_users()
        functions.show_user(users)

    def remove_user(self, id):
        delete_user_with_id(id)

    def change_rights(self, id):
        functions.change_departement(id)

    def add_user(self, lastname, firstname, dateBirth, pob, email):
        user = User(lastname, firstname, dateBirth, pob, email)
        functions.create_user(user)

    def generate_user_pwd(self, id):
        update_pwd(functions.generate_pwd_hash(), id)

    def modify_user_lastname(self, lastname, id):
        info = get_user_with_id(id)
        user = functions.return_user(info)
        user.set_lastname(lastname)
        functions.modify_user(user)

    def modify_user_firstname(self, firstname, id):
        info = get_user_with_id(id)
        user = functions.return_user(info)
        user.set_firstname(firstname)
        functions.modify_user(user)

    def modify_user_email(self, email, id):
        info = get_user_with_id(id)
        user = functions.return_user(info)
        user.set_email(email)
        functions.modify_user(user)

    def modify_user_dob(self, dob, id):
        info = get_user_with_id(id)
        user = functions.return_user(info)
        user.set_dob(dob)
        functions.modify_user(user)

    def modify_user_pob(self, cob, id):
        info = get_user_with_id(id)
        user = functions.return_user(info)
        user.set_pob(cob)
        functions.modify_user(user)