import json

# The User class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password
        }

    @classmethod
    def from_dict(cls, dct):
        return cls(dct['username'], dct['password'])

# The UserManager class
class UserManager:
    def __init__(self, filename='users.json'):
        self.filename = filename

    def create_user(self, username, password):
        user = User(username, password)
        users = self.load_users()
        users.append(user.to_dict())
        self.write_users(users)

    def login(self, username, password):
        users = self.load_users()
        for user in users:
            if user['username'] == username and user['password'] == password:
                return True
        return False

    def load_users(self):
        try:
            with open(self.filename, 'r') as f:
                users = json.load(f)
                return [User.from_dict(user) for user in users]
        except FileNotFoundError:
            return []

    def write_users(self, users):
        with open(self.filename, 'w') as f:
            json.dump([user.to_dict() for user in users], f)

# The main function
def main():
    user_manager = UserManager()

    print('1. Create a user account')
    print('2. Login')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        username = input('Enter a username: ')
        password = input('Enter a password: ')
        user_manager.create_user(username, password)
        print('User account created successfully!')
    elif choice == 2:
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        if user_manager.login(username, password):
            print('Login successful!')
        else:
            print('Login failed. Incorrect username or password.')
    else:
        print('Invalid choice. Try again.')

if __name__ == '__main__':
    main()
