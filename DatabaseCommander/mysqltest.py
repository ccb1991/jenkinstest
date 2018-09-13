import pymysql

strHost = 'localhost'
strDB = 'be_app'
strUser = 'root'
strPasswd = '123456'


'''链接数据库'''
def getConnect(db=strDB, host=strHost, user=strUser, passwd=strPasswd, charset="utf8"):
    return pymysql.connect(host=strHost, db=strDB, user=strUser, passwd=strPasswd, charset="utf8")

'''初始化数据库游标'''
def init_client_cursor_encode(conn):
    '''''mysql client encoding=utf8'''
    curs = conn.cursor()
    curs.execute("SET NAMES utf8")
    conn.commit()
    return curs

class SplitMySQLData():
    '''将数据库数据分页'''
    def __init__(self, Conn, NumPerPage=100):
        self.Conn = Conn
        self.NumPerPage = NumPerPage


    def query_for_list(self, TableName, param=None):
        TotalPageNum = self.__calculate_total_pages(TableName, param)
        for PageIndex in range(TotalPageNum):
            yield self.__query_each_page(TableName, PageIndex, param)


    def __create_pagination_query_sql(self, TableName, CurrentPageIndex):
        '''创建获取当前页后面数据的SQL语句'''
        StartIndex = self.__calculate_start_index(CurrentPageIndex)
        Sql = r'select * from %s total_table limit %s,%s' % (TableName, StartIndex, self.NumPerPage)
        return Sql

    def __query_each_page(self, sql, CurrentPageIndex, param=None):
        '''返回每一页查询的数据'''
        curs = init_client_cursor_encode(self.Conn)
        qSql = self.__create_pagination_query_sql(sql, CurrentPageIndex)
        if param is None:
            curs.execute(qSql)
        else:
            curs.execute(qSql, param)
        result = curs.fetchall()
        curs.close()
        return result

    def __calculate_start_index(self, CurrentPageIndex):
        '''计算当前开始的行数'''
        startIndex = CurrentPageIndex * self.NumPerPage
        return startIndex

    def __calculate_total_rows_num(self, TableName, param=None):
        ''''' 计算总行数 '''
        Sql = r'select count(*) from %s total_table' % TableName
        Curs = init_client_cursor_encode(self.Conn)
        if param is None:
            Curs.execute(Sql)
        else:
            Curs.execute(Sql, param)
        Result = Curs.fetchone()
        Curs.close()
        if Result != None:
            TotalRowsNum = int(Result[0])
            return TotalRowsNum

    def __calculate_total_pages(self, TableName, param=None):
        ''''' 计算总页数 '''
        TotalRowsNum = self.__calculate_total_rows_num(TableName, param)
        TotalPages = 0
        if (TotalRowsNum % self.NumPerPage) == 0:
            TotalPages = TotalRowsNum / self.NumPerPage
        else:
            TotalPages = (TotalRowsNum//self.NumPerPage) + 1
        return TotalPages

    def __calculate_last_index(self, TotalRows, TotalPages, CurrentPageIndex):
        '''''计算结束时候的索引'''
        lastIndex = 0
        if TotalRows < self.NumPerPage:
            lastIndex = TotalRows
        elif ((TotalRows % self.NumPerPage == 0)
              or (TotalRows % self.NumPerPage != 0 and CurrentPageIndex < TotalPages)):
            lastIndex = CurrentPageIndex * self.NumPerPage
        elif (TotalRows % self.NumPerPage != 0 and CurrentPageIndex == TotalPages):  # 最后一页
            lastIndex = TotalRows
        return lastIndex

    # def get_table_data_number(self,TableName='attr_template'):
    #     '''获取某一张表下数据数量'''
    #     sql="SELECT COUNT(*) FROM "+TableName
    #     self.Cursor.execute(sql)
    #     TableLenth=self.Cursor.fetchall()
    #     return TableLenth
    #
    # def get_table_data(self,BeginNumber,EndNumber,TableName='attr_template'):
    #     '''获取分批获取某一张表下数据'''
    #     sql="SELECT * FROM "+TableName+" limit "+BeginNumber+","+EndNumber
    #     print(sql)
    #     self.Cursor.execute(sql)
    #     Result=self.Cursor.fetchall()
    #     return Result

    # def nested_list_to_list(self,TableName):
    #     Nested=self.get_table_data(TableName)
    #     for Sublist in Nested:
    #         yield Sublist


if __name__=='__main__':

    conn = getConnect()
    pag = SplitMySQLData(conn)
    # sql = r'SELECT * FROM `websit_base_info` WHERE id>%s'
    # param = [3]
    # for ret in pag.queryForList(sql, param):
    sql ='attr_template'
    for ret in pag.query_for_list(sql):
        print (ret)
    conn.close()



