from  main import User,session,engine

# def displayData():
#     try:
#         local_session = session(bind=engine)
#         allUsers = local_session.query(User).all()[:3]
#         for user in allUsers:
#             print(f"Username={user.username},Email={user.email}")
#     except Exception as  e:
#         print(e)
# displayData()
class ShowTableData:
    def displayData(self):
        try:
            self.local_session = session(bind=engine)
            self.allUsers = self.local_session.query(User).all() #[:3]
            for user in self.allUsers:
                print(f"Username={user.username},Email={user.email}")
        except Exception as e:
            print(e)

showData = ShowTableData()
showData.displayData()
