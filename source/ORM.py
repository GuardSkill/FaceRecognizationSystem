from sqlalchemy import create_engine, Column, Integer, String, Time, DateTime, MetaData, Table, Sequence, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import datetime

tableName = "CheckInfo"
Base = declarative_base()
class CheckInfo(Base):
    __tablename__ = tableName
    info_id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    name = Column(String(30),primary_key=True)
    up_time = Column(DateTime(timezone=True), server_default=func.now())
    off_time = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    date_time = Column(String(8))
    # str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+str(datetime.datetime.now().day)
    # def __repr__(self):
    #     return "<User(name='%s', up_time='%s', off_time='%s')>" % (
    #         self.name, self.up_time, self.off_time)
def returndate():
    return str(datetime.datetime.now().year) + str(datetime.datetime.now().month) + str(datetime.datetime.now().day)

class Service(object):
    def __init__(self):
        self.engine = create_engine("mysql://user:S1042h28@Guardskill.cn/checkin?charset=utf8", echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.createDB()
    def createDB(self):
        Base.metadata.create_all(self.engine)
    def delDB(self):
        Base.metadata.drop_all(self.engine)
    def newinfo(self,thename):
        info=self.session.query(CheckInfo).filter_by(name=thename,date_time=returndate()).first()
        if info==None:
            data=CheckInfo(name=thename,date_time=returndate())
            self.session.add(data)
            self.session.commit()
            return  True
        else:
            return False#people have sign up today
    def updateinfo(self,thename):
        info = self.session.query(CheckInfo).filter_by(name=thename, date_time=returndate()).first()
        if info == None or info.up_time!=info.off_time:
            print("fail to sign off ")
            return False
        else:
            info.name=thename+'temp'
            self.session.commit()
            info.name = thename
            self.session.commit()
            return  True
    def listinfo(self):
        infos=self.session.query(CheckInfo).filter_by(date_time=returndate()).all()
        return infos
