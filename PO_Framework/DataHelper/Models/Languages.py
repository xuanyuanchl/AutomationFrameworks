from sqlalchemy import Column, INT, SMALLINT, Boolean, NVARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # 创建对象的基类

class Languages(Base):  # 定义一个类，继承Base
    __tablename__ = 'Languages'
    __table_args__ = ({"schema": "dbo"})
    languageIncId = Column(INT(), primary_key=True)
    languageSqlId = Column(SMALLINT(), primary_key=True)
    languageCode = Column(NVARCHAR(10), nullable= True)
    languageName = Column(NVARCHAR(40), nullable= True)
    isDeleted = Column(Boolean(), nullable= False)
    isoLanguageCode = Column(NVARCHAR(10), nullable= True)
    isSupported = Column(Boolean(), nullable=False)
    translationTag = Column(NVARCHAR(40), nullable= True)