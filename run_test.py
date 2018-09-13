import CompareDataBase
from DatabaseCommander.OperateDataBase import ImportDataOperater
from DatabaseCommander.DataBaseUserInfo import DataBaseInfoManager
from DatabaseCommander.ConnectDB import ConnectDataBase
from PublicMethod.OperationJson import OperationJson
from PublicMethod.OperateIniFile import OperateIni
from ZipCommander.zipfiledata import ZipFileData
from datetime import datetime
import os
path=os.path.dirname(__file__)

if __name__=='__main__':
    RIGHT_DATA_REPORT_PATH= "."+os.path.sep+"report"+os.path.sep+"rightdatareport.txt"
    WRONG_DATA_REPORT_PATH= "."+os.path.sep+"report"+os.path.sep+"wrongdatareport.txt"
    EXPORT_DATA_PATH= path + os.path.sep+"ExportData"+os.path.sep+"export"
    INI_NAME= "all-luban-subsystem-db-config.ini"
    TARGET_DATA_SECTION_NAME= "TargetDataBase"
    OPERATE_INI=OperateIni("DataBaseInfo.ini")
    TIME=datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "------->>>"
    Zip_File_Data=ZipFileData(EXPORT_DATA_PATH)
    # dirnames=Zip_File_Data.get_mysql_dir_name()
    Assert=CompareDataBase.CompareDataTest()

    for dirname in Zip_File_Data.datadirlist:
    # for dirname in dirnames:
        '''遍历文件夹名称'''
        databaseini = DataBaseInfoManager(dirname, INI_NAME)
        databasename=databaseini.get_value("mysql.database")
        OPERATE_INI.modify_section_data(TARGET_DATA_SECTION_NAME, databasename, "databasename")
        TargetDataBaseConnect = ImportDataOperater(TARGET_DATA_SECTION_NAME)
        # filepathlist = Zip_File_Data.get_file_path_list(EXPORT_DATA_PATH + os.path.sep + dirname)
        print(TIME, "开始对比数据库" + dirname)
        # for filepath in filepathlist:
        filelist=Zip_File_Data.filepathsdict[dirname]
        for file in filelist:
            '''遍历文件夹下文件'''
            with open(RIGHT_DATA_REPORT_PATH, mode='a') as rightreportfile:
                with open(file, encoding="utf-8") as csvfile:
                    with open(WRONG_DATA_REPORT_PATH, mode='a') as wrongreportfile:
                        datalist=(datalist for datalist in csvfile)
                        filename= file.split('\\')[-1][:-4]
                        print(TIME,"开始对比表" + filename, file=rightreportfile)
                        for data in datalist:
                            totalpages = TargetDataBaseConnect.calculate_total_pages(filename)
                            linedata = list(data.rstrip("\n").replace('"', '').split(","))
                            for page in range(totalpages):
                                tabledata=TargetDataBaseConnect.query_each_page(filename,page)
                                try:
                                    Assert.test_contain_data(linedata,tabledata)
                                    print(TIME+"pass", file=rightreportfile)
                                    continue
                                except:
                                    pass
                                print(TIME, filename, str(linedata) +"不存在", file=wrongreportfile)
                        print(TIME, "结束对比表" + filename, file=rightreportfile)
        print(TIME, "结束对比数据库" + dirname)





    # databasenames=OperationJson("DataBaseName.json").get_data("DataBaseName")
    # with open (reportpath,"w") as f:
    #     for databasename in databasenames:
    #         OperateIni("DataBaseInfo.ini").modify_section_data("TargetDataBase",databasename,"databasename")
    #         OperateIni("DataBaseInfo.ini").modify_section_data("OriginalDataBase",databasename,"databasename")
    #         Assert=CompareDataBase.CompareDataTest()
    #         OriginalDataBaseConnect=OperateDataBase("OriginalDataBase")
    #         TargetDataBaseConnect=OperateDataBase("TargetDataBase")
    #         OriginalTables=OriginalDataBaseConnect.get_all_table_name()
    #         for OriginalTable in OriginalTables:
    #             '''判断每张表格中数据行数是否相等'''
    #             OriginalTableTotalNumber=OriginalDataBaseConnect.calculate_total_rows_num(OriginalTable)
    #             TargetTableTotalNumber=TargetDataBaseConnect.calculate_total_rows_num(OriginalTable)
    #             try:
    #                 Assert.test_data_number(OriginalTableTotalNumber,TargetTableTotalNumber)
    #             except AssertionError:
    #                 print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"------->>>","%s MySQL原始表数据条数<--不等于-->迁移后数据"%OriginalTable,file=f)
    #                 continue
    #             else:
    #                 print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"------->>>","%s MySQL原始表数据条数<--等于-->迁移后数据"%OriginalTable,file=f)
    #             '''对比每一条数据的每一个字段'''
    #             TotalPages=OriginalDataBaseConnect.calculate_total_pages(OriginalTable)
    #             for page in range(TotalPages):
    #                 OriginalData=OriginalDataBaseConnect.query_each_page(OriginalTable,page)
    #                 TargetData=TargetDataBaseConnect.query_each_page(OriginalTable,page)
    #                 try:
    #                     Assert.test_compare_data(OriginalData,TargetData)
    #                     print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"------->>>","%s MySQL原始表数据与迁移后数据<--相同-->"%OriginalTable,file=f)
    #                 except AssertionError as error:
    #                     print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"------->>>","%s MySQL原始表数据与迁移后数据<--不相同-->"%OriginalTable,file=f)
    #                     print(error,file=f)






