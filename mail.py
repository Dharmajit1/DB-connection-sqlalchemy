from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,DateTime,create_engine
from  datetime import datetime
# import  os
# BASE_DIR = os.path.dirname(os.path.realpath(__file__))
# connection_string = "sqlite:///"+os.path.join(BASE_DIR,'users.db')

connection_string = "sqlite:///D:/users.db"

base = declarative_base()

engine = create_engine(connection_string,echo=True)

session = sessionmaker()

class User(base):
    __tablename__ = 'users'
    id = Column(Integer(),primary_key=True)
    username = Column(String(25),nullable=False)
    password = Column(String(8),nullable=False)
    createTime = Column(DateTime(),default=datetime.utcnow())
    email = Column(String(70),nullable=True)

#     def __repr__(self):
#         return f"id={self.id},username={self.username}"
#
# newUser = User(id=1,username="Niladri")
# print(newUser)

BaseCreate = base.metadata.create_all(engine)
