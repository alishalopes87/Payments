class UserDatabase(object):
    user_names = {}
    addresses = {}

    def __init__(self):
        self.readDb()

    def readDb():
        for row in open("user_database.txt"):
            splits = row.split("\t")
            integer = int(splits[0])

            user_name[integer] = splits[1]
            addresses[integer] = splits[2]


    def add_new_user(userId, username, address):
        user_names[userId] = username
        addresses[userId] = address



