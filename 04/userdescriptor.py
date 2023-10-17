class Username:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return None  # pragma: no cover
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value in instance.__class__.existing_usernames:
            raise ValueError("Username already exists")
        instance.__dict__[self.name] = value
        instance.__class__.existing_usernames.add(value)

    def __delete__(self, instance):
        if "username" in instance.__dict__:
            del instance.__dict__[self.name]


class Email:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return None  # pragma: no cover
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email address")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        if "email" in instance.__dict__:
            del instance.__dict__[self.name]


class Password:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return None  # pragma: no cover
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not any(char.isdigit() for char in value) or not any(
            char.isalpha() for char in value
        ):
            raise ValueError("Password must contain both letters and numbers")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        if "password" in instance.__dict__:
            del instance.__dict__[self.name]


class User:
    existing_usernames = set()
    list_users = []

    username = Username("username")
    email = Email("email")
    password = Password("password")

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.list_users.append(self)

    def change_password(self, new_password):
        self.password = new_password

    def delete_account(self):
        self.existing_usernames.remove(self.username)
        del self.username
        del self.password
        del self.email
        self.list_users.remove(self)

    @classmethod
    def get_all_users(cls):
        return [(user.username, user.email, user.password) for user in cls.list_users]
