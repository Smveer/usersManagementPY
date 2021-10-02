import sys
sys.path.append("../../usersManagementPY")

from classes.User import *
from functions import *
from dbFunctions import *


class Admin(User):
    def __init__(self, lastname, firstname, dateBirth, pob, email):
        super().__init__(lastname, firstname, dateBirth, pob, email)


