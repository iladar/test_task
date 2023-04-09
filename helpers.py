import re


def is_id(variable):
    if type(variable) == int:
        return True
    else:
        return False


def is_integer(variable):
    if type(variable) == int:
        return True
    else:
        return False


def is_number(variable):
    if (type(variable) == float) or (type(variable) == int):
        return True
    else:
        return False


def is_string(variable):
    if variable and variable != '':
        if type(variable) == str:
            return True
        else:
            return False


def is_url(variable):
    if type(variable) == str:
        if re.fullmatch('^(https?:\/\/)?([\w-]{1,32}\.[\w-]{1,32})[^\s@]*$',variable): # проверка на подобные https://reqres.in/api/users/2
            return True
        elif re.fullmatch('^(\/)?[^\s@]*',variable): #проверка на подобные /api/users/2
            return True
        else:
            return False


def is_email(variable):
    if type(variable) == str:
        if re.fullmatch('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',variable):
            return True
        else:
            return False


def is_bool(variable):
    if type(variable) == bool:
        return True
    else:
        return False


def is_none(variable):
    if variable is None:
        return True
    else:
        return False


def is_array(variable):
    if type(variable) == list:
        return True
    else:
        return False
