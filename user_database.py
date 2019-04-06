class UserDatabase(object):

    def __init__(self):
        self.user_names = {}
        self.addresses = {}
        self.readDb()

    def readDb(self):
        for row in open("seed_data/user_database.txt"):
            splits = row.strip().split("\t")
            integer = int(splits[0])

            self.user_names[integer] = splits[1]
            self.addresses[integer] = splits[2]


    def add_new_user(self,userId, username, address):
        self.user_names[userId] = username
        self.addresses[userId] = address



