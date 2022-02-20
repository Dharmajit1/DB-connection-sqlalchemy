from  main import User,session,engine

# def deleteData():
#     try:
#         local_session = session(bind=engine)
#         user_to_delete = local_session.query(User).filter(User.username=="Ashis").first()
#         local_session.delete(user_to_delete)
#         local_session.commit()
#     except Exception as ex:
#         print(ex)
# deleteData()
class DeleteData:
    def deleteData(self):
        try:
            self.local_session = session(bind=engine)
            self.user_to_delete = self.local_session.query(User).filter(User.username == "jyoti").first()
            self.local_session.delete(self.user_to_delete)
            self.local_session.commit()
        except Exception as ex:
            print(ex)

delete = DeleteData()
delete.deleteData()
