# 方案一
class User:
    def __init__(self,user_id):
        self.user_id = user_id

    def __repr__(self):
        return "User({})".format(self.user_id)


def sort_notcompare():
    users = [User(23),User(3),User(99)]
    print(users)
    print(sorted(users,key=lambda x:x.user_id))


# 方案二
from operator import attrgetter
users = [User(23),User(3),User(99)]
print(sorted(users,key=attrgetter('user_id')))



