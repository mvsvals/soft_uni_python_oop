class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, account_name):
        if not 5 <= len(account_name) <= 15:
            raise ValueError('The username must be between 5 and 15 characters.')
        self.__username = account_name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, pw):
        is_allowed_length = len(pw) >= 8
        has_an_uppercase_letter = any(x.isupper() for x in pw)
        has_a_digit = any(x.isdigit() for x in pw)
        if not is_allowed_length or not has_an_uppercase_letter or not has_a_digit:
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')
        self.__password = pw


    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'

