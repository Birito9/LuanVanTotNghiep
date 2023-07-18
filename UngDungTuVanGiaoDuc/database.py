from library import *
from utils import Utils

class Database:
    # kết nối csdl
    def condb(self):
        try:
            db = mysql.connector.connect(user='root', password='Tenshi23@2', host='localhost', port='3306',
                                         database='tuvangiaoduc')
            return db
        except mysql.connector.Error as err:
            Utils.showDialog(f"Lỗi khi kết nối cơ sở dữ liệu: {err}")
            return None

    # hủy kết nối csdl
    def discondb(self):
        self.condb().close()

