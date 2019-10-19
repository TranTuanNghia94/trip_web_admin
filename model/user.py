import datetime


class User(object):
    def __init__(self, username, password, first_name, last_name, role, is_active):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.date_create = datetime.datetime.utcnow()
        self.role = role
        self.is_active = is_active


