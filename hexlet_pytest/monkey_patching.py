class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


def alice():
    return 'Alice_2'

user = User("John")
user.get_name() # John

# anonimus function
patch_name = lambda: "Alice"
user.get_name = patch_name

print(user.get_name()) # Alice


# non anonimus function
patch_name = alice
user.get_name = patch_name

print(user.get_name()) # Alice_2