from DatabaseCommander.DataBaseUserInfo import WhiteAndCommonTableInfo
from DatabaseCommander.OperateDataBase import QueryExportData
from ZipCommander.zipfiledata import ZipFileData
import os

path=os.path.dirname(__file__)
whiteandcommoninfo=WhiteAndCommonTableInfo()
commoninfo=whiteandcommoninfo.commontable_section_data
whiteinfo=whiteandcommoninfo.white_section_data
EXPORT_DATA_PATH = path + os.path.sep + "ExportData" + os.path.sep + "export"
zipfile=ZipFileData(EXPORT_DATA_PATH)
print(commoninfo)
print(whiteinfo)

class ExportDataCompare():
    def compare_common_data(self):
        pass

    def compare_white_data(self):
        pass

    def compare_epid_correlation_data(self):
        pass