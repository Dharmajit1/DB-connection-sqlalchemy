from  main import User,session,engine

# allUsers=[{
#     "username" : "Dharmajit",
#     "password" : "Tutu@4354",
#     "email" : "dharmajit@000"
#     },
# {
#     "username" : "Ranjan",
#     "password" : "ranjan1",
#     "email" : "ranjan@000"
# },
# {
#     "username" : "Prusty",
#     "password" : "pr000",
#     "email" : "prusty@000"
# },
# ]
#
# def InsertData():
#     try:
#         local_session = session(bind=engine)
#         for user in allUsers:
#             new_user = User(username=user["username"],password=user["password"],email=user["email"])
#             local_session.add(new_user)
#             local_session.commit()
#     except Exception as  e:
#         print(e)
# InsertData()
class CreateUsers:

    def __init__(self,allUsers):
        self.allUsers = allUsers

    def InsertData(self):
        try:
            self.local_session = session(bind=engine)
            for user in allUsers:
                self.new_user = User(username=user["username"], password=user["password"], email=user["email"])
                self.local_session.add(self.new_user)
                self.local_session.commit()
        except Exception as e:
            print(e)


allUsers = [{
            "username": "jyoti",
            "password": "jy000",
            "email": "jyoti@000"
        },
            {
                "username": "Bishnu",
                "password": "bis000",
                "email": "Bishnu@000"
            },
            {
                "username": "Lata",
                "password": "Lt000",
                "email": "Lata@000"
            },
        ]
create= CreateUsers(allUsers)
create.InsertData()
