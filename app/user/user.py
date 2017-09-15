class User:
    def __init__(self, name, email, passwrod):
        self.name = name
        self.email = email
        self.password = passwrod

    def __str__(self):
        return '<User {} {} {}>'.format(self.name, self.email, self.password)

    def user_is_valid(self, name, password):
        if self.name == name and self.password == password:
            return True
        else:
            return False

    def add(self, a, b):
        return a + b