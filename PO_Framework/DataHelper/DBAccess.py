
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from GetConfiguration.SeleniumTestsConfigurationSection import seleniumTestsConfigurationSection


class dbAccess:
    configuration = seleniumTestsConfigurationSection()

    def __init__(self):
        self.engine = create_engine(self.configuration.eurodatConnectionString, echo=True)  # 初始化数据库连接

    @property
    def dbSession(self):
        DBsession = sessionmaker(bind=self.engine)  # 创建DBsession类
        self.session = DBsession()  # 创建对象
        return self.session

    def SaveChanges(self):
        self.session.commit()

    def query_all(self, target_class, query_filter):  # 查询内容
        result_list = self.session.query(target_class).filter(query_filter).all()
        return result_list

    def update_by_filter(self, obj, update_hash, query_filter):
        self.session.query(obj.__class__).filter(query_filter).update(update_hash)

    def Close(self):
        self.session.close()

    def execute_sql(self, sql_str):  # 执行sql语句
        return self.session.execute(sql_str)








