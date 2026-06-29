class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @classmethod
    def admin(cls, name):
        return cls(name, role = "admin")
    
    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

a = User.admin('Thamid')
print(a.is_valid_email("asdf@gmail.com"))
print(a.role)