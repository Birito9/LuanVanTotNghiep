from library import *
from database import Database
from utils import Utils

class Mainwindow():
    # *******************window1*********************
    # khởi chạy chương trình
    def __init__(self):
        self.window_startupwin = QMainWindow()
        self.uic_startupwin = Ui_startup_window()
        self.uic_startupwin.setupUi(self.window_startupwin)
        self.uic_startupwin.admissions_consultancy.clicked.connect(self.show_admissionswindow)
        self.uic_startupwin.loggin_admin.clicked.connect(self.show_choosetablewindow)
        self.is_greeted_voice = False
        self.is_greeted_text = False

    # load form đăng nhập
    def show_startupwindow(self):
        self.window_startupwin.show()

    # *******************window2*********************

    # load form tư vấn Giáo dục
    def show_admissionswindow(self):
        bot_process = "Chào mừng bạn đến với tư vấn Giáo dục của trường Đại Học Công Nghệ Sài Gòn"
        utils.speakoutput(bot_process)
        self.window_startupwin.close()
        self.window_admissionswindow = QtWidgets.QMainWindow()
        self.uic_admissionswindow= Ui_admissions_window()
        self.uic_admissionswindow.setupUi(self.window_admissionswindow)
        self.window_admissionswindow.show()
        self.uic_admissionswindow.bot_output.setText(bot_process)
        self.uic_admissionswindow.question_send.clicked.connect(self.btn_sendadmissions)
        self.uic_admissionswindow.record.clicked.connect(self.btn_record)
        self.uic_admissionswindow.logout.clicked.connect(self.btn_logout_admissionswindow)
        self.uic_admissionswindow.refresh_button.clicked.connect(self.btn_resetwindow)
        self.loaddatahintquestion()

    #Nút Gửi
    def btn_sendadmissions(self):
        tensv = self.uic_admissionswindow.name_input.text()
        sdt = self.uic_admissionswindow.numberphone_input.text()
        checksdt = len(self.uic_admissionswindow.numberphone_input.text())
        self.timestop()

        if not self.validate_personal_info(tensv, sdt, checksdt):
            return

        self.disable_personal_info_fields()

        if not self.validate_question_input():
            return

        if not self.is_greeted_text:
            self.greet_user_text(tensv)
            QTimer.singleShot(5000, self.continue_execution)
        else:
            self.continue_execution()

    def continue_execution(self):
        user_question_text = self.uic_admissionswindow.question_input.text()
        bot_process = self.get_response(user_question_text)
        utils.speakoutput(bot_process)
        self.uic_admissionswindow.bot_output.setText(bot_process)

        # Lấy thông tin cá nhân
        ten = self.uic_admissionswindow.name_input.text()
        sdt = self.uic_admissionswindow.numberphone_input.text()
        cauhoi = self.uic_admissionswindow.question_input.text()
        cautl = self.uic_admissionswindow.bot_output.toPlainText()

        # Lưu thông tin vào cơ sở dữ liệu
        self.adddb_userinfowindow(ten, sdt, cauhoi, cautl)

        # Cập nhật giao diện
        self.uic_admissionswindow.user_ouput.setText(self.uic_admissionswindow.question_input.text())
        self.loaddatahintquestion()
        self.timestart()

    # Nút ghi âm
    def btn_record(self):
        tensv = self.uic_admissionswindow.name_input.text()
        sdt = self.uic_admissionswindow.numberphone_input.text()
        checksdt = len(sdt)
        self.timestop()

        if not self.validate_personal_info(tensv, sdt, checksdt):
            return

        self.disable_personal_info_fields()

        if not self.is_greeted_voice:
            self.greet_user_voice(tensv)
            QTimer.singleShot(3200, lambda: self.handle_audio_question(tensv, sdt))
        else:
            self.uic_admissionswindow.bot_output.setText("Trợ lý đang nghe")
            utils.speakoutput("Trợ lý đang nghe")
            QTimer.singleShot(2000, lambda: self.handle_audio_question(tensv, sdt))

    def handle_audio_question(self, tensv, sdt):
        # Ghi âm giọng nói
        with lis.Microphone() as mic:
            bot_listen = lis.Recognizer()
            audio = bot_listen.listen(mic, phrase_time_limit=5)

        try:
            # Chuyển đổi giọng nói thành văn bản
            user_question_voice = bot_listen.recognize_google(audio, language="vi-VN")
            self.cauhoi = user_question_voice
            self.uic_admissionswindow.user_ouput.setText(user_question_voice)

            # Lấy phản hồi từ hàm get_response
            bot_process = self.get_response(user_question_voice)
            utils.speakoutput(bot_process)
            self.uic_admissionswindow.bot_output.setText(bot_process)

            # Lưu thông tin vào cơ sở dữ liệu
            self.adddb_userinfowindow(tensv, sdt, user_question_voice, bot_process)
            self.loaddatahintquestion()
            self.timestart()
        except lis.UnknownValueError:
            self.uic_admissionswindow.bot_output.setText(
                "Hệ thống chưa nhận diện được giọng nói của bạn. Vui lòng thử lại!")
            utils.speakoutput("Hệ thống chưa nhận diện được giọng nói của bạn. Vui lòng thử lại")
        except lis.RequestError:
            error_message = "Lỗi kết nối mạng. Vui lòng kiểm tra kết nối và thử lại!"
            utils.showDialog(error_message)

    def validate_personal_info(self, tensv, sdt, checksdt):
        if tensv == "":
            bot_process = "Bạn vui lòng nhập họ và tên"
            utils.speakoutput(bot_process)
            return False
        elif not tensv.replace(' ', '').isalpha():
            bot_process = "Bạn vui lòng nhập họ và tên chính xác không có kí tự đặc biệt"
            utils.speakoutput(bot_process)
            return False
        elif sdt and (not sdt.isnumeric() or checksdt != 10 or not sdt.startswith('0')):
            bot_process = "Bạn vui lòng nhập số điện thoại chính xác 10 số và số 0 ở đầu"
            utils.speakoutput(bot_process)
            return False
        return True

    def disable_personal_info_fields(self):
        self.uic_admissionswindow.name_input.setEnabled(False)
        self.uic_admissionswindow.numberphone_input.setEnabled(False)

    def validate_question_input(self):
        if self.uic_admissionswindow.question_input.text().isspace() or self.uic_admissionswindow.question_input.text() == "":
            bot_process = "Bạn chưa nhập câu hỏi"
            utils.speakoutput(bot_process)
            self.uic_admissionswindow.bot_output.setText(bot_process)
            return False
        return True

    def greet_user_text(self, tensv):
        bot_process = f"Xin chào {tensv}. Chúng tôi đang tìm kiếm câu trả lời"
        self.is_greeted_text = True
        utils.speakoutput(bot_process)
        self.uic_admissionswindow.bot_output.setText(bot_process)
        QCoreApplication.processEvents()

    def greet_user_voice(self, tensv):
        bot_process = f"Xin chào {tensv}. Bạn cần hỏi gì?"
        self.is_greeted_voice = True
        utils.speakoutput(bot_process)
        self.uic_admissionswindow.bot_output.setText(bot_process)
        QCoreApplication.processEvents()

    # nút quay lại của win 2
    def btn_logout_admissionswindow(self):
        self.window_admissionswindow.close()
        self.window_startupwin.show()

    # nút tải lại
    def btn_resetwindow(self):
        self.timestop()
        text = "Chào mừng bạn đến với tư vấn Giáo dục của trường Đại Học Công Nghệ Sài Gòn"
        self.uic_admissionswindow.name_input.setText("")
        self.uic_admissionswindow.bot_output.setText(text)
        self.uic_admissionswindow.numberphone_input.setText("")
        self.uic_admissionswindow.user_ouput.setText("")
        self.uic_admissionswindow.question_input.setText("")
        self.uic_admissionswindow.name_input.setDisabled(False)
        self.uic_admissionswindow.numberphone_input.setDisabled(False)

    # thời gian tự động
    def timestart(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.btn_resetwindow)
        self.timer.start(300000)

    # ngừng đếm thời gian tự động
    def timestop(self):
        self.timestart()
        self.timer.stop()

    # tải câu hỏi gợi ý
    def loaddatahintquestion(self):
        self.uic_admissionswindow.hintquestion.setColumnWidth(0, 380)
        self.uic_admissionswindow.hintquestion.setHorizontalHeaderLabels(["Câu Hỏi Gợi Ý"])
        con = db.condb()
        print('đã kết nối thành công')
        try:
            cur = con.cursor()
            cur.execute("   select distinct cauhoi, cautraloi from ThongTinNguoiDung\
                            where cauhoi not like 'Hệ thống chưa nhận diện được giọng nói của bạn xin hãy thử lại!'\
                            having cautraloi != 'Vấn đề này không có trong phạm vi của tôi. Bạn hãy liên hệ trực tiếp cán bộ phòng, khoa để được hỗ trợ thêm.' ORDER BY cauhoi, cautraloi;")
            data = cur.fetchall()
            self.uic_admissionswindow.hintquestion.setRowCount(len(data))
            self.uic_admissionswindow.hintquestion.setColumnCount(1)
            for rownumber, rowdata in enumerate(data):
                for colnumber, data in enumerate(rowdata):
                    self.uic_admissionswindow.hintquestion.setItem(rownumber, colnumber,
                                                                   QtWidgets.QTableWidgetItem(str(data)))
        except:
            return con.rollback()
        finally:
            db.discondb()
            print('đã ngắt kết nối')

    # lọc tên bảng cơ sở dữ liệu của admissionswindow
    def cb_tablename_admissionswindow(self):
        table_mapping = {
            'Tư vấn chung': 'CauHoiTuVan',
            'Du lịch': 'CauHoiDuLich',
            'Công nghệ thông tin': 'CauHoiCongNgheThongTin',
            'Quản Trị Kinh Doanh': 'CauHoiQuanTriKinhDoanh'
        }
        current_text = self.uic_admissionswindow.choosetable_box.currentText()
        table = table_mapping.get(current_text, 'CauHoiTuVan')
        return table

    def selectdb_admissionswindow(self, question):
        con = db.condb()  # Kết nối tới cơ sở dữ liệu
        table = self.cb_tablename_admissionswindow()  # Lấy tên bảng từ combobox
        print('Đã kết nối thành công')

        traloi_table = f"TraLoi{table[6:]}"  # Tách từ kí tự thứ 6 của table để lấy traloi_table
        search_query = f"'{question}'"  # Lấy nội dung tìm kiếm từ tham số question

        try:
            query = f"SELECT ch.macauhoi, ch.cauhoi, tl.cautraloi FROM {table} ch INNER JOIN {traloi_table} tl ON ch.macauhoi = tl.macauhoi WHERE MATCH(ch.cauhoi) AGAINST ({search_query});"
            cur = con.cursor()  # Tạo đối tượng con trỏ để thực hiện truy vấn SQL
            cur.execute(query)  # Thực thi truy vấn
            data = cur.fetchall()  # Lấy tất cả các hàng kết quả của truy vấn
            return data
        except:
            return con.rollback()  # Rollback nếu có lỗi xảy ra
        finally:
            db.discondb()  # Đóng kết nối tới cơ sở dữ liệu
            print('Đã ngắt kết nối')

    def calculate_keyword_match(self, user_question_input, database_question):
        # Chuyển đổi câu hỏi người dùng và câu hỏi trong cơ sở dữ liệu thành chuỗi lowercase
        user_question = user_question_input.lower()
        db_question = database_question.lower()

        # Tách từ trong câu hỏi người dùng và câu hỏi trong cơ sở dữ liệu
        user_keywords = set(user_question.split())
        db_keywords = set(db_question.split())

        # Tính toán tỷ lệ khớp bằng cách tính số từ khóa chung giữa hai câu hỏi và chia cho số từ trong câu hỏi trong cơ sở dữ liệu
        keyword_match_ratio = len(user_keywords.intersection(db_keywords)) / len(db_keywords)

        return keyword_match_ratio

    def calculate_keyword_match_ratio_list(self, user_question, data):
        keyword_match_ratios = []
        for row in data:
            macauhoi = row[0]
            cauhoi = row[1]
            cautraloi = row[2]

            # Tính toán keyword_match_ratio cho mỗi cặp cauhoi và cautraloi
            keyword_match_ratio = self.calculate_keyword_match(user_question, cauhoi)

            # Thêm vào danh sách keyword_match_ratios
            keyword_match_ratios.append((macauhoi, cauhoi, cautraloi, keyword_match_ratio))

        return keyword_match_ratios

    def get_response(self, user_question_input):
        # Chuyển đổi câu hỏi người dùng thành chữ thường
        user_question = user_question_input.lower()

        data = self.selectdb_admissionswindow(user_question)

        # Kiểm tra xem câu hỏi nguyên thủy có chứa cặp từ khóa về thời gian hay không
        if self.contains_time_keywords(user_question):
            # Tính toán danh sách keyword_match_ratios
            keyword_match_ratios = self.calculate_keyword_match_ratio_list(user_question, data)

            # Sắp xếp danh sách keyword_match_ratios theo giảm dần của keyword_match_ratio
            sorted_ratios = sorted(keyword_match_ratios, key=lambda x: x[3], reverse=True)

            # Lấy câu trả lời từ cặp có tỷ lệ khớp từ khóa cao nhất
            if sorted_ratios:
                best_match = sorted_ratios[0]
                response = best_match[2]
                current_year = datetime.datetime.now().year

                # Xác định năm từ câu trả lời
                year_in_response = None
                words = response.split()
                for i in range(len(words)):
                    if words[i].isdigit():
                        year_in_response = int(words[i])
                        break

                # So sánh năm trong câu trả lời với năm hiện tại
                if year_in_response is not None and year_in_response < current_year:
                    response = "Vấn đề này không có trong phạm vi của tôi. Bạn hãy liên hệ trực tiếp cán bộ phòng, khoa để được hỗ trợ thêm."

                return response
        else:
            # Tính toán danh sách keyword_match_ratios
            keyword_match_ratios = self.calculate_keyword_match_ratio_list(user_question, data)

            # Sắp xếp danh sách keyword_match_ratios theo giảm dần của keyword_match_ratio
            sorted_ratios = sorted(keyword_match_ratios, key=lambda x: x[3], reverse=True)

            # Lấy câu trả lời từ cặp có tỷ lệ khớp từ khóa cao nhất
            if sorted_ratios:
                best_match = sorted_ratios[0]
                response = best_match[2]

                return response

        # Trả về câu response "liên hệ khoa" nếu không có kết quả khớp từ khóa hoặc không chứa cặp từ khóa về thời gian
        return "Vấn đề này không có trong phạm vi của tôi. Bạn hãy liên hệ trực tiếp cán bộ phòng, khoa để được hỗ trợ thêm."

    def contains_time_keywords(self, question):
        time_keywords = ["năm", "tháng", "ngày", "tuần", "quý", "học kỳ", "kỳ học", "mùa hè", "mùa đông", "thời hạn",
                         "lịch trình", "thời điểm", "thời vụ", "thời hạn", "thời gian", "học kỳ", "học kỳ",
                         "kỳ nghỉ", "kỳ thi"]

        time_phrases = ["lịch học kỳ", "thời gian nghỉ", "ngày học", "thời gian thi", "học kỳ 1", "học kỳ 2",
                        "học kỳ mùa hè", "học kỳ mùa đông", "kỳ học phụ", "kỳ nghỉ giữa học kỳ", "kỳ thi", "kỳ báo cáo",
                        "kỳ đánh giá", "lịch học kỳ"]

        # Kiểm tra xem các từ khóa đơn có xuất hiện trong câu hỏi nguyên thủy hay không
        for keyword in time_keywords:
            if keyword in question:
                return True

        # Kiểm tra xem các cụm từ khóa có xuất hiện trong câu hỏi nguyên thủy hay không
        for phrase in time_phrases:
            if phrase in question:
                return True

        return False

    # thêm ttsv vào dbbase trong admissionswindow
    def adddb_userinfowindow(self, ten, sdt, cauhoi, cautrl):
        con = db.condb()
        print('đã kết nối thành công')
        try:
            query = "insert into ThongTinNguoiDung (hovaten, sdt, cauhoi, cautraloi) values ('" + ten + "', '" + sdt + "', '" + cauhoi + "', '" + cautrl + "');"
            cur = con.cursor()
            cur.execute(query)
            con.commit()
        except:
            con.rollback()
        finally:
            db.discondb()
            print('đã ngắt kết nối')

    # *******************window3*********************

    # load form chọn dbase
    def show_choosetablewindow(self):
        # Lấy thông tin từ các trường nhập liệu
        taikhoan = self.uic_startupwin.username_input.text()
        matkhau = self.uic_startupwin.password_input.text()

        # Khởi tạo các biến
        con = db.condb()

        # Hàm để thiết lập giao diện cho từng vai trò
        def set_ui_for_role(role, admin_id_taikhoan):
            # Cài đặt các giá trị và thao tác giao diện cho từng vai trò
            self.uic_startupwin.username_input.setText("")
            self.uic_startupwin.password_input.setText("")
            self.uic_startupwin.note.setText("")
            self.window_startupwin.close()
            self.window_choosetablewindow = QtWidgets.QMainWindow()
            self.uic_choosetablewindow = Ui_choosetable_window()
            self.uic_choosetablewindow.setupUi(self.window_choosetablewindow)
            self.window_choosetablewindow.show()
            self.uic_choosetablewindow.data_table.clicked.connect(self.show_datatablewindow)
            self.uic_choosetablewindow.infouser_table.clicked.connect(self.show_userinfowindow)
            self.uic_choosetablewindow.logout.clicked.connect(self.btn_logout_choosetablewindow)
            self.uic_choosetablewindow.account_input.setText(taikhoan)
            self.uic_choosetablewindow.account_input.setDisabled(True)
            self.uic_choosetablewindow.password_input.setText(matkhau)
            self.uic_choosetablewindow.update_button.clicked.connect(self.btn_upddbpass_admin)

            # Lưu admin_id vào biến instance để có thể sử dụng trong phạm vi của lớp
            self.admin_id = admin_id_taikhoan

        try:
            cur = con.cursor()
            cur.execute("SELECT id, taikhoan, matkhau, vaitro FROM taikhoan WHERE taikhoan = %s;", (taikhoan,))
            data = cur.fetchall()
            if data:
                admin_id, username, password, vaitro = data[0]
                # Kiểm tra tên đăng nhập và mật khẩu
                if username == taikhoan and password == matkhau:
                    if vaitro == 'Admin':
                        # Thiết lập giao diện cho vai trò 1
                        set_ui_for_role(vaitro, admin_id)
                        self.uic_choosetablewindow.signup_admin.clicked.connect(self.show_createadminwindow)
                    elif vaitro == 'Cán Bộ':
                        # Thiết lập giao diện cho vai trò 2
                        set_ui_for_role(vaitro, admin_id)
                        self.uic_choosetablewindow.signup_admin.hide()
                        self.uic_choosetablewindow.signup_admin.setDisabled(True)
                    else:
                        self.uic_startupwin.note.setText("Vai trò không hợp lệ")
                else:
                    self.uic_startupwin.note.setText("Sai tên đăng nhập hoặc mật khẩu")
            else:
                self.uic_startupwin.note.setText("Người dùng không tồn tại")
        except:
            self.uic_startupwin.note.setText("Lỗi khi truy vấn cơ sở dữ liệu")
        finally:
            db.discondb()
            print('Đã ngắt kết nối')

    # window3
    def btn_logout_choosetablewindow(self):
        self.window_choosetablewindow.close()
        self.window_startupwin.show()

    # nút cập nhật mật khẩu
    def btn_upddbpass_admin(self):
        taikhoan = self.uic_choosetablewindow.account_input.text()
        matkhau = self.uic_choosetablewindow.password_input.text()
        con = db.condb()
        print('đã kết nối thành công')
        try:
            query = "update taikhoan set matkhau = '"+matkhau+"' where taikhoan = '"+taikhoan+"';"
            cur = con.cursor()
            cur.execute(query)
            con.commit()
        except:
            con.rollback()
        finally:
            db.discondb()
            print('đã ngắt kết nối')
            utils.showDialog('cập nhật mật khẩu thành công')

    # *******************window4*********************

    # # load bảng câu hỏi tư vấn
    def show_datatablewindow(self):
        self.window_choosetablewindow.close()
        self.window_datatablewindow = QtWidgets.QMainWindow()
        self.uic_datatablewindow = Ui_datatable_window()
        self.window_datatablewindow.show()
        self.uic_datatablewindow.setupUi(self.window_datatablewindow)
        self.uic_datatablewindow.datatable.setHorizontalHeaderLabels(
            ["Mã Câu Hỏi", "Câu Hỏi", "Câu Trả Lời", "Thời Gian"])
        self.uic_datatablewindow.datatable.setColumnWidth(3, 235)
        self.uic_datatablewindow.datatable.setColumnWidth(2, 445)
        self.uic_datatablewindow.datatable.setColumnWidth(1, 347)
        self.uic_datatablewindow.datatable.setColumnWidth(0, 140)
        self.uic_datatablewindow.choosetable_box.currentIndexChanged.connect(self.cb_tablename_datatablewindow)
        self.uic_datatablewindow.logout_button.clicked.connect(self.btn_log_datatablewindow)
        self.uic_datatablewindow.back_button.clicked.connect(self.btn_back_datatablewindow)
        self.uic_datatablewindow.add_button.clicked.connect(self.btn_add)
        self.uic_datatablewindow.add_button_ctl.clicked.connect(self.btn_add_ctl)
        self.uic_datatablewindow.update_button.clicked.connect(self.btn_uppdate)
        self.uic_datatablewindow.delete_button.clicked.connect(self.btn_delete)
        self.uic_datatablewindow.search_input.textChanged.connect(self.searchdata)

        # Load dữ liệu bảng đầu tiên
        default_table = 'CauHoiTuVan'
        self.loaddb_admissions(default_table)

    # Lọc tên bảng cơ sở dữ liệu của datatablewindow
    def cb_tablename_datatablewindow(self):
        table_mapping = {
            'Tư vấn chung': 'CauHoiTuVan',
            'Du lịch': 'CauHoiDuLich',
            'Công nghệ thông tin': 'CauHoiCongNgheThongTin',
            'Quản Trị Kinh Doanh': 'CauHoiQuanTriKinhDoanh'
        }
        current_text = self.uic_datatablewindow.choosetable_box.currentText()
        choosetable = table_mapping.get(current_text, 'CauHoiTuVan')
        self.loaddb_admissions(choosetable)
        return choosetable

    # Load data datatablewindow
    def loaddb_admissions(self, choosetable):
        self.uic_datatablewindow.datatable.setColumnWidth(3, 235)
        self.uic_datatablewindow.datatable.setColumnWidth(2, 445)
        self.uic_datatablewindow.datatable.setColumnWidth(1, 347)
        self.uic_datatablewindow.datatable.setColumnWidth(0, 140)
        self.uic_datatablewindow.datatable.setHorizontalHeaderLabels(
            ["Mã Câu Hỏi", "Câu Hỏi", "Câu Trả Lời", "Thời Gian"])

        con = db.condb()
        print('Đã kết nối thành công')

        try:
            traloi_table = f"TraLoi{choosetable[6:]}"
            query = f"""
                SELECT ch.macauhoi, ch.cauhoi, tl.cautraloi, ch.thoigiancapnhat FROM  {choosetable}  ch LEFT JOIN {traloi_table} tl ON ch.macauhoi = tl.macauhoi ORDER BY ch.thoigiancapnhat desc, CAST(SUBSTRING(ch.macauhoi, 3) AS UNSIGNED) ASC
                """
            cur = con.cursor()
            cur.execute(query)
            data = cur.fetchall()

            self.uic_datatablewindow.datatable.setRowCount(len(data))
            self.uic_datatablewindow.datatable.setColumnCount(4)

            for rownumber, rowdata in enumerate(data):
                for colnumber, cellData in enumerate(rowdata):
                    self.uic_datatablewindow.datatable.setItem(rownumber, colnumber,
                                                               QtWidgets.QTableWidgetItem(str(cellData)))
        except:
            return con.rollback()
        finally:
            db.discondb()
            print('Đã ngắt kết nối')

    # window4
    def btn_log_datatablewindow(self):
        self.window_datatablewindow.close()
        self.window_startupwin.show()

    # nút quay lại của win4
    def btn_back_datatablewindow(self):
        self.window_datatablewindow.close()
        self.window_choosetablewindow.show()

    # chức năng thêm trong win 4
    def btn_add(self):
        try:
            choosetable = self.cb_tablename_datatablewindow()
            macauhoi = self.uic_datatablewindow.idkeyword_input.text()
            cauhoi = self.uic_datatablewindow.question_input.text()
            cautl = self.uic_datatablewindow.answer_input.text()
            admin_id = self.admin_id  # Lấy admin_id từ biến instance

            if not all(c.isalnum() or c.isspace() or c == '.' or c == '?' or c == ',' for c in cauhoi):
                utils.showDialog('Câu hỏi chỉ được chứa chữ cái, chữ số, dấu cách, dấu chấm, dấu chấm hỏi và dấu phẩy')
                return

            if cauhoi.strip() == "":
                utils.showDialog('Bạn cần nhập câu hỏi')
                return

            if cautl.strip() == "":
                utils.showDialog('Bạn cần nhập câu trả lời')
                return

            self.adddb_admissionwindows(macauhoi, cauhoi, cautl, admin_id, choosetable)
            self.loaddb_admissions(choosetable)
        except:
            utils.showDialog('Lỗi! Thêm dữ liệu thất bại')
        finally:
            self.uic_datatablewindow.idkeyword_input.setText("")
            self.uic_datatablewindow.question_input.setText("")
            self.uic_datatablewindow.answer_input.setText("")

    def adddb_admissionwindows(self, macauhoi, cauhoi, cautl, admin_id, table=''):
        con = db.condb()
        print('Đã kết nối thành công')
        try:
            # Thêm câu hỏi vào bảng tương ứng
            query1 = f"INSERT INTO {table} (macauhoi, cauhoi, admin_id) VALUES ('{macauhoi}', '{cauhoi}', '{admin_id}');"
            cur = con.cursor()
            cur.execute(query1)

            # Thêm câu trả lời vào bảng tương ứng
            traloi_table = f"TraLoi{table[6:]}"
            query2 = f"INSERT INTO {traloi_table} (macauhoi, cautraloi) VALUES ('{macauhoi}', '{cautl}');"
            cur.execute(query2)
            con.commit()
            utils.showDialog('Thêm dữ liệu thành công')
        except:
            con.rollback()
            utils.showDialog('Lỗi! Thêm dữ liệu thất bại')
        finally:
            db.discondb()
            print('Đã ngắt kết nối')

    def btn_add_ctl(self):
        currentItem = self.uic_datatablewindow.datatable.currentItem()
        if currentItem is not None:
            selected_row = currentItem.row()
            macauhoi = self.uic_datatablewindow.datatable.item(selected_row, 0).text()
            cauhoi = self.uic_datatablewindow.datatable.item(selected_row, 1).text()

            if self.uic_datatablewindow.answer_input.text() == "":
                self.uic_datatablewindow.idkeyword_input.setText(macauhoi)
                self.uic_datatablewindow.question_input.setText(cauhoi)
                utils.showDialog('Bạn hãy nhập câu trả lời')
                return
            else:
                choosetable = self.cb_tablename_datatablewindow()
                cautl = self.uic_datatablewindow.answer_input.text()
                self.adddb_answer_addmission(macauhoi, cauhoi, cautl, choosetable)
                self.loaddb_admissions(choosetable)

            self.uic_datatablewindow.answer_input.setText("")

            # Chọn dòng tương ứng với câu hỏi được chọn
            self.uic_datatablewindow.datatable.selectRow(selected_row)
        else:
            utils.showDialog('Lỗi! Chưa chọn dữ liệu')

    def adddb_answer_addmission(self, macauhoi, cauhoi, cautl, table=''):
        con = db.condb()
        print('Đã kết nối thành công')
        try:
            # Kiểm tra mã câu hỏi đã tồn tại hay chưa
            query_check = f"SELECT macauhoi FROM {table} WHERE macauhoi = '{macauhoi}';"
            cur = con.cursor()
            cur.execute(query_check)
            result = cur.fetchone()

            if result is None:
                utils.showDialog(f'Mã câu hỏi "{macauhoi}" không tồn tại')
                return

            # Thêm câu trả lời vào bảng tương ứng
            traloi_table = f"TraLoi{table[6:]}"
            query = f"INSERT INTO {traloi_table} (macauhoi, cautraloi) VALUES ('{macauhoi}', '{cautl}');"
            cur.execute(query)
            con.commit()
            utils.showDialog('Thêm câu trả lời thành công')
        except:
            con.rollback()
            utils.showDialog('Lỗi! Thêm câu trả lời thất bại')
        finally:
            db.discondb()
            print('Đã ngắt kết nối')

    # nút sửa data trên giao diện
    def btn_uppdate(self):
        currentItem = 0  # Khởi tạo biến currentItem
        for currentItem in self.uic_datatablewindow.datatable.selectedItems():
            currentItem.row()  # Lấy chỉ số dòng của item hiện tại
        self.uic_datatablewindow.idkeyword_input.setDisabled(True)
        if self.uic_datatablewindow.idkeyword_input.text() == "":
            # Nếu không có từ khóa đầu vào được nhập, lấy dữ liệu từ dòng được chọn trên bảng và hiển thị trong các trường nhập liệu tương ứng
            try:
                self.uic_datatablewindow.idkeyword_input.setText(
                    self.uic_datatablewindow.datatable.item(currentItem.row(), 0).text())
                self.uic_datatablewindow.question_input.setText(
                    self.uic_datatablewindow.datatable.item(currentItem.row(), 1).text())
                self.uic_datatablewindow.answer_input.setText(
                    self.uic_datatablewindow.datatable.item(currentItem.row(), 2).text())
            except:
                utils.showDialog('Lỗi! Chưa chọn dữ liệu')
        else:
            choosetable = self.cb_tablename_datatablewindow()  # Lấy tên bảng được chọn từ combobox

            try:
                macauhoi = self.uic_datatablewindow.idkeyword_input.text()
                cauhoi = self.uic_datatablewindow.question_input.text()
                cautl = self.uic_datatablewindow.answer_input.text()
                if not all(c.isalnum() or c.isspace() or c == '.' or c == '?' or c == ',' for c in cauhoi):
                    utils.showDialog(
                        'Câu hỏi chỉ được chứa chữ cái, chữ số, dấu cách, dấu chấm, dấu chấm hỏi và dấu phẩy')
                    return
                if cauhoi.strip() == "":
                    utils.showDialog('Bạn cần nhập câu hỏi')
                    return

                if cautl.strip() == "":
                    utils.showDialog('Bạn cần nhập câu trả lời')
                    return
                admin_id = self.admin_id  # Sử dụng admin_id đã có sẵn từ hàm show_choosetablewindow
                self.upddatedb_admissionswindow(macauhoi, cauhoi, cautl, choosetable,
                                                admin_id)  # Thực hiện cập nhật dữ liệu
                success = self.upddatedb_admissionswindow(macauhoi, cauhoi, cautl, choosetable,
                                                          admin_id)  # Thực hiện cập nhật dữ liệu
                if success:
                    utils.showDialog('Cập nhật thành công!')
                else:
                    utils.showDialog('Lỗi! Cập nhật không thành công')
            except:
                utils.showDialog('Lỗi! Cập nhật không thành công')
            finally:
                self.loaddb_admissions(choosetable)  # Tải lại dữ liệu trong bảng
                self.uic_datatablewindow.idkeyword_input.setDisabled(False)
                self.uic_datatablewindow.idkeyword_input.setText("")
                self.uic_datatablewindow.question_input.setText("")
                self.uic_datatablewindow.answer_input.setText("")

    # Chức năng update dữ liệu admissionswindow
    def upddatedb_admissionswindow(self, macauhoi, cauhoi, cautl, table='', admin_id=''):
        con = db.condb()
        print('Đã kết nối thành công')
        try:
            cur = con.cursor()

            # Cập nhật câu hỏi trong bảng CauHoiTuVan
            query1 = f"UPDATE {table} SET cauhoi = '{cauhoi}', admin_id = '{admin_id}', thoigiancapnhat = CURRENT_TIMESTAMP() WHERE macauhoi = '{macauhoi}';"
            cur.execute(query1)

            # Lấy macautraloi của câu trả lời cuối cùng trong bảng TraLoiTuVan
            traloi_table = f"TraLoi{table[6:]}"
            query2_subquery = f"SELECT macautraloi FROM {traloi_table} WHERE macauhoi = '{macauhoi}' ORDER BY thoigiancapnhat DESC LIMIT 1;"
            cur.execute(query2_subquery)
            macautraloi = cur.fetchone()[0]  # Lấy giá trị macautraloi từ kết quả của subquery

            # Cập nhật câu trả lời trong bảng TraLoiTuVan
            query2 = f"UPDATE {traloi_table} SET cautraloi = '{cautl}', thoigiancapnhat = CURRENT_TIMESTAMP() WHERE macautraloi = '{macautraloi}' AND macauhoi = '{macauhoi}';"
            cur.execute(query2)

            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            db.discondb()
            print('Đã ngắt kết nối')

    # chức năng hỏi trước khi xóa trong win 4
    def btn_delete(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("Bạn có muốn xóa dữ liệu không?")
        msgBox.setWindowTitle("Thông báo")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.delete_datatablewindow()

    # chức năng xóa bảng trong datatablewindow
    def delete_datatablewindow(self):
        selected_items = self.uic_datatablewindow.datatable.selectedItems()
        if len(selected_items) > 0:
            currentRow = selected_items[0].row()
            choosetable = self.cb_tablename_datatablewindow()
            macauhoi = self.uic_datatablewindow.datatable.item(currentRow, 0).text()
            self.delete_from_tables(macauhoi, choosetable)
            self.loaddb_admissions(choosetable)
            utils.showDialog('Xóa dữ liệu thành công')
        else:
            utils.showDialog('Lỗi! Chưa chọn dữ liệu')

    # chức năng xóa dữ liệu trong hai bảng
    def delete_from_tables(self, macauhoi, choosetable):
        con = db.condb()
        print('Đã kết nối thành công')
        try:
            # Xóa bản ghi trong bảng TraLoiTuVan trước
            traloi_table = f"TraLoi{choosetable[6:]}"
            query2 = f"DELETE FROM {traloi_table} WHERE macauhoi = '{macauhoi}';"
            cur = con.cursor()
            cur.execute(query2)

            # Xóa câu hỏi trong bảng CauHoiTuVan
            query1 = f"DELETE FROM {choosetable} WHERE macauhoi = '{macauhoi}';"
            cur.execute(query1)

            con.commit()
        except:
            con.rollback()
        finally:
            db.discondb()
            print('Đã ngắt kết nối')

    # Tìm kiếm dữ liệu từ hai bảng CauHoi và TraLoi và sắp xếp thời gian cập nhật cuối cùng trên đầu
    def searchdata(self, i=''):
        self.uic_datatablewindow.datatable.resizeColumnToContents(0)
        self.uic_datatablewindow.datatable.resizeColumnToContents(1)
        self.uic_datatablewindow.datatable.resizeColumnToContents(2)
        self.uic_datatablewindow.datatable.resizeColumnToContents(3)
        con = db.condb()
        print('Đã kết nối thành công')
        try:
            # Xây dựng câu truy vấn SELECT
            choosetable = self.cb_tablename_datatablewindow()
            traloi_table = f"TraLoi{choosetable[6:]}"
            query = f"SELECT c.macauhoi, c.cauhoi, t.cautraloi, t.thoigiancapnhat " \
                    f"FROM {choosetable} c " \
                    f"JOIN {traloi_table} t ON c.macauhoi = t.macauhoi " \
                    f"WHERE c.macauhoi LIKE '%{i}%' OR c.cauhoi LIKE '%{i}%' " \
                    f"ORDER BY t.thoigiancapnhat DESC;"
            cur = con.cursor()
            cur.execute(query)
            data = cur.fetchall()
            self.uic_datatablewindow.datatable.setRowCount(len(data))
            self.uic_datatablewindow.datatable.setColumnCount(4)
            for rownumber, rowdata in enumerate(data):
                for colnumber, data in enumerate(rowdata):
                    # Đặt giá trị dữ liệu vào ô trong bảng
                    self.uic_datatablewindow.datatable.setItem(rownumber, colnumber,
                                                               QtWidgets.QTableWidgetItem(str(data)))
        except:
            return con.rollback()
        finally:
            db.discondb()
            print('Đã ngắt kết nối')

    # *******************window5*********************

    # load bảng câu hỏi người dùng
    def show_userinfowindow(self):
        self.window_choosetablewindow.close()
        self.window_userinfowindow = QtWidgets.QMainWindow()
        self.uic_userinfowindow = Ui_userinfo_window()
        self.uic_userinfowindow.setupUi(self.window_userinfowindow)
        self.window_userinfowindow.show()
        self.loaddata_userinfowindow()
        self.uic_userinfowindow.search_input.textChanged.connect(self.searchstudent)
        self.uic_userinfowindow.excel_button.clicked.connect(self.btn_exportexcel)
        self.uic_userinfowindow.deleteall_button.clicked.connect(self.btn_deleteall)
        self.uic_userinfowindow.logout_button.clicked.connect(self.btn_logout_userinfowindow)
        self.uic_userinfowindow.back_button.clicked.connect(self.btn_back_userinfowindow)

    # tìm dữ liệu sinh viên
    def searchstudent(self, i=''):
        self.uic_userinfowindow.datatable.setColumnWidth(0, 300)
        self.uic_userinfowindow.datatable.setColumnWidth(1, 220)
        self.uic_userinfowindow.datatable.setColumnWidth(2, 220)
        self.uic_userinfowindow.datatable.setColumnWidth(3, 220)
        self.uic_userinfowindow.datatable.setColumnWidth(4, 235)
        con = db.condb()
        print('đã kết nối thành công')
        try:
            cur = con.cursor()
            cur.execute("select hovaten, sdt, cauhoi, cautraloi, thoigianhoi from ThongTinNguoiDung where sdt LIKE '%" + i + "%' or hovaten LIKE '%" + i + "%'")
            data = cur.fetchall()
            self.uic_userinfowindow.datatable.setRowCount(len(data))
            self.uic_userinfowindow.datatable.setColumnCount(5)
            for rownumber, rowdata in enumerate(data):
                for colnumber, data in enumerate(rowdata):
                    self.uic_userinfowindow.datatable.setItem(rownumber, colnumber, QtWidgets.QTableWidgetItem(str(data)))
        except:
            return con.rollback()
        finally:
            db.discondb()
            print('đã ngắt kết nối')

    # nút xuất file exe
    def btn_exportexcel(self):
        columnheader = ["Họ Và Tên", "Số Điện Thoại", "Câu Hỏi", "Câu Trả Lời", "Thời Gian"]
        con = db.condb()
        print('đã kết nối thành công')
        try:
            cur = con.cursor()
            cur.execute("select hovaten, sdt, cauhoi, cautraloi, thoigianhoi from ThongTinNguoiDung")
            data = cur.fetchall()
            wb = Workbook()
            ws = wb.active
            ws.append(columnheader)
            for row in data:
                ws.append(row)
            savespot = QFileDialog.getSaveFileName(directory='c:/', filter="Excel Files (*.xlsx)")
            print(savespot[0])
            wb.save(savespot[0])
            utils.showDialog('đã xuất dữ liệu thành công')
        except:
            utils.showDialog('lỗi! xuất dữ liệu không thành công')
        finally:
            db.discondb()
            print('đã ngắt kết nối')

    # nút xóa tất cả ghi bản thông tin sinh viên
    def btn_deleteall(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("bạn có muốn xóa dữ liệu không??")
        msgBox.setWindowTitle("Thông báo")
        msgBox.setStandardButtons(QMessageBox.Ok| QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.delalldb_userinfowindow()

    # chức năng xóa tất cả ghi bản thông tin sinh viên
    def delalldb_userinfowindow(self):
        try:
            self.deletedb_userinfowindow()
            self.clearsavefilemp3()
            utils.showDialog('xóa thành công')
        except:
            utils.showDialog('lỗi! chưa xóa được dữ liệu')
        finally:
            self.loaddata_userinfowindow()

    # chức năng xóa bảng trong userinfowindow
    def deletedb_userinfowindow(self):
        con = db.condb()
        print('đã kết nối thành công')
        try:
            cur = con.cursor()
            cur.execute("DELETE FROM ThongTinNguoiDung", ())
            con.commit()
        except:
            con.rollback()
        finally:
            db.discondb()
            print('đã ngắt kết nối')

    # đăng xuất userinfowindow
    def btn_logout_userinfowindow(self):
        self.window_userinfowindow.close()
        self.window_startupwin.show()

    # nút quay lại của userinfowindow
    def btn_back_userinfowindow(self):
        self.window_userinfowindow.close()
        self.window_choosetablewindow.show()

    # tải dữ liệu từ sql lên userinfowindow
    def loaddata_userinfowindow(self):
        self.uic_userinfowindow.datatable.setColumnWidth(0, 300)
        self.uic_userinfowindow.datatable.setColumnWidth(1, 220)
        self.uic_userinfowindow.datatable.setColumnWidth(2, 220)
        self.uic_userinfowindow.datatable.setColumnWidth(3, 220)
        self.uic_userinfowindow.datatable.setColumnWidth(4, 235)
        self.uic_userinfowindow.datatable.setHorizontalHeaderLabels(
            ["Họ Và Tên", "Số Điện Thoại", "Câu Hỏi", "Câu Trả Lời", "Thời Gian"])
        con = db.condb()
        print('đã kết nối thành công')
        try:
            cur = con.cursor()
            cur.execute("select hovaten, sdt, cauhoi, cautraloi, thoigianhoi from ThongTinNguoiDung")
            data = cur.fetchall()
            self.uic_userinfowindow.datatable.setRowCount(len(data))
            self.uic_userinfowindow.datatable.setColumnCount(5)
            for rownumber, rowdata in enumerate(data):
                for colnumber, data in enumerate(rowdata):
                    self.uic_userinfowindow.datatable.setItem(rownumber, colnumber,
                                                              QtWidgets.QTableWidgetItem(str(data)))
        except:
            return con.rollback()
        finally:
            db.discondb()
            print('đã ngắt kết nối')

    # *******************window 6*********************

    # load bảng quản lý quản trị viên
    def show_createadminwindow(self):
        self.window_choosetablewindow.close()
        self.window_createadminwindow = QtWidgets.QMainWindow()
        self.uic_createadminwindow = Ui_createadmin_window()
        self.uic_createadminwindow.setupUi(self.window_createadminwindow)
        self.window_createadminwindow.show()
        self.loaddata_accountnadmin()
        self.uic_createadminwindow.datatable.setColumnWidth(0, 150)
        self.uic_createadminwindow.datatable.setColumnWidth(1, 450)
        self.uic_createadminwindow.datatable.setColumnWidth(2, 200)
        self.uic_createadminwindow.datatable.setColumnWidth(3, 200)
        self.uic_createadminwindow.datatable.setColumnWidth(4, 150)
        self.uic_createadminwindow.search_input.textChanged.connect(self.searchdata_createadminwindow)
        self.uic_createadminwindow.back_button.clicked.connect(self.btn_back_createadminwindow)
        self.uic_createadminwindow.logout_button.clicked.connect(self.btn_logout_createadminwindow)
        self.uic_createadminwindow.add_button.clicked.connect(self.btn_addadmin)
        self.uic_createadminwindow.update_button.clicked.connect(self.btn_updateadmin)
        self.uic_createadminwindow.delete_button.clicked.connect(self.btn_deleteadmin)

    # chức năng tìm kiếm thông tin quản trị viên
    def searchdata_createadminwindow(self, i=''):
        self.uic_createadminwindow.datatable.setColumnWidth(0, 150)
        self.uic_createadminwindow.datatable.setColumnWidth(1, 450)
        self.uic_createadminwindow.datatable.setColumnWidth(2, 200)
        self.uic_createadminwindow.datatable.setColumnWidth(3, 200)
        self.uic_createadminwindow.datatable.setColumnWidth(4, 150)
        con = db.condb()
        print('đã kết nối thành công')
        try:
            query = "select id, hovaten, taikhoan, matkhau, vaitro from taikhoan where hovaten LIKE '%" + i + "%' or taikhoan LIKE '%" + i + "%';"
            cur = con.cursor()
            cur.execute(query)
            data = cur.fetchall()
            self.uic_createadminwindow.datatable.setRowCount(len(data))
            self.uic_createadminwindow.datatable.setColumnCount(5)
            for rownumber, rowdata in enumerate(data):
                for colnumber, data in enumerate(rowdata):
                    self.uic_createadminwindow.datatable.setItem(rownumber, colnumber,
                                                                 QtWidgets.QTableWidgetItem(str(data)))
        except:
            return con.rollback()
        finally:
            db.discondb()
            print('đã ngắt kết nối')

    # nút trở về chọn bảng
    def btn_back_createadminwindow(self):
        self.window_createadminwindow.close()
        self.window_choosetablewindow.show()

    # nút đăng xuất khỏi quản lý tài khoản quản trị viên
    def btn_logout_createadminwindow(self):
        self.window_createadminwindow.close()
        self.window_startupwin.show()

    # nút thêm quản trị viên
    def btn_addadmin(self):
        hovaten = self.uic_createadminwindow.fullname_input.text()
        taikhoan = self.uic_createadminwindow.account_input.text()
        matkhau = self.uic_createadminwindow.password_input.text()
        vaitro = self.uic_createadminwindow.role_input.text()

        if hovaten.strip() == "":
            utils.showDialog('Bạn cần nhập họ và tên')
            return

        if vaitro.strip() == "":
            utils.showDialog('Bạn cần nhập vai trò')
            return

        if not taikhoan.isalnum():
            utils.showDialog('Tài khoản chỉ được chứa chữ cái và chữ số')
            return

        if taikhoan.strip() == "":
            utils.showDialog('Bạn cần nhập tài khoản')
            return

        if matkhau.strip() == "":
            utils.showDialog('Bạn cần nhập mật khẩu')
            return

        if not all(c.isalpha() or c.isspace() for c in hovaten):
            utils.showDialog('Họ và tên chỉ được chứa chữ cái và dấu cách')
            return

        if vaitro.strip() == "":
            utils.showDialog('Bạn cần nhập vai trò')
            return

        if vaitro != 'Admin' and vaitro != 'Cán Bộ':
            utils.showDialog('Vai trò chỉ được sử dụng "Admin" hoặc "Cán Bộ"')
            return

        self.adddb_createadminwindow(hovaten, taikhoan, matkhau, vaitro)
        self.loaddata_accountnadmin()
        self.uic_createadminwindow.fullname_input.setText("")
        self.uic_createadminwindow.account_input.setText("")
        self.uic_createadminwindow.password_input.setText("")
        self.uic_createadminwindow.role_input.setText("")

    # chức năng quản trị viên
    def adddb_createadminwindow(self, hovaten, taikhoan, matkhau, vaitro):
        con = db.condb()
        print('đã kết nối thành công')
        try:
            query = "INSERT INTO taikhoan (id, hovaten, taikhoan, matkhau, vaitro) VALUES (%s, %s, %s, %s, %s);"
            cur = con.cursor()
            id = str(uuid.uuid4())  # Tạo giá trị UUID ngẫu nhiên
            values = (id, hovaten, taikhoan, matkhau, vaitro)
            cur.execute(query, values)
            con.commit()
        except:
            con.rollback()
        finally:
            db.discondb()
            print('đã ngắt kết nối')
            utils.showDialog('thêm quản trị viên thành công')

        # nút cập nhật thông tin tài khoản quản trị viên
    def btn_updateadmin(self):
        currentItem = 0
        for currentItem in self.uic_createadminwindow.datatable.selectedItems():
            currentItem.row()
        if (self.uic_createadminwindow.fullname_input.text() == ""):
            try:
                self.uic_createadminwindow.id_input.setText(
                    self.uic_createadminwindow.datatable.item(currentItem.row(), 0).text())
                self.uic_createadminwindow.fullname_input.setText(
                    self.uic_createadminwindow.datatable.item(currentItem.row(), 1).text())
                self.uic_createadminwindow.account_input.setText(
                    self.uic_createadminwindow.datatable.item(currentItem.row(), 2).text())
                self.uic_createadminwindow.password_input.setText(
                    self.uic_createadminwindow.datatable.item(currentItem.row(), 3).text())
                self.uic_createadminwindow.role_input.setText(
                    self.uic_createadminwindow.datatable.item(currentItem.row(), 4).text())
            except:
                utils.showDialog('lỗi! chưa chọn dữ liệu')
        else:
            try:
                id = ""
                if self.uic_createadminwindow.id_input.text() == "":
                    utils.showDialog('Cảnh báo: không tìm thấy Mã tài khoản để cập nhật')
                else:
                    id = self.uic_createadminwindow.id_input.text()
                hoten = self.uic_createadminwindow.fullname_input.text()
                taikhoan = self.uic_createadminwindow.account_input.text()
                matkhau = self.uic_createadminwindow.password_input.text()
                vaitro = self.uic_createadminwindow.role_input.text()
                if hoten.strip() == "":
                    utils.showDialog('Bạn cần nhập họ và tên')
                    return

                if taikhoan.strip() == "":
                    utils.showDialog('Bạn cần nhập tài khoản')
                    return

                if not taikhoan.isalnum():
                    utils.showDialog('Tài khoản chỉ được chứa chữ cái và chữ số')
                    return

                if matkhau.strip() == "":
                    utils.showDialog('Bạn cần nhập mật khẩu')
                    return

                if not all(c.isalpha() or c.isspace() for c in hoten):
                    utils.showDialog('Họ và tên chỉ được chứa chữ cái và dấu cách')
                    return

                if vaitro.strip() == "":
                    utils.showDialog('Bạn cần nhập vai trò')
                    return

                if vaitro != 'Admin' and vaitro != 'Cán Bộ':
                    utils.showDialog('Vai trò chỉ được sử dụng "Admin" hoặc "Cán Bộ"')
                    return
                self.upddbadmin_createadminwindow(id, hoten, taikhoan, matkhau, vaitro)
                utils.showDialog('cập nhật thành công')
            except:
                utils.showDialog('lỗi! tài khoản chưa được cập nhật')
            finally:
                self.loaddata_accountnadmin()
                self.uic_createadminwindow.id_input.setText("")
                self.uic_createadminwindow.fullname_input.setText("")
                self.uic_createadminwindow.account_input.setText("")
                self.uic_createadminwindow.password_input.setText("")
                self.uic_createadminwindow.role_input.setText("")

        # chức năng cập nhật thông tin tài khoản quản trị viên
    def upddbadmin_createadminwindow(self, id, hoten, taikhoan, matkhau, vaitro):
        con = db.condb()
        print('đã kết nối thành công')
        try:
            query = "update taikhoan set hovaten = '"+ hoten +"', taikhoan = '"+ taikhoan +"', matkhau = '"+ matkhau +"', vaitro = '"+ vaitro +"' where id = '"+ id +"';"
            cur = con.cursor()
            cur.execute(query)
            con.commit()
        except:
            con.rollback()
        finally:
            db.discondb()
            print('đã ngắt kết nối')

    # nút xóa tài khoản quản trị viên
    def btn_deleteadmin(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("bạn có muốn xóa dữ liệu không??")
        msgBox.setWindowTitle("Thông báo")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.function_delectadmin()

    # chức năng xóa tài khoản quản trị viên
    def function_delectadmin(self):
        currentItem = 0
        for currentItem in self.uic_createadminwindow.datatable.selectedItems():
            currentItem.row()
        try:
            id = self.uic_createadminwindow.datatable.item(currentItem.row(), 0).text()
            if id == self.admin_id:
                utils.showDialog('Lỗi! Bạn không thể xóa tài khoản đang sử dụng chức năng')
                return
            self.delselectdb_createadminwindow(id)
            self.loaddata_accountnadmin()
            utils.showDialog('xóa quản trị viên thành công')
        except:
            utils.showDialog('lỗi! chưa chọn quản trị viên')


    # chức năng xóa csdl trên tài khoản quản trị viên
    def delselectdb_createadminwindow(self, id):
        con = db.condb()
        print('đã kết nối thành công')
        try:
            query = "DELETE FROM taikhoan WHERE id = %s;"
            cur = con.cursor()
            cur.execute(query, (id,))
            con.commit()
        except:
            con.rollback()
        finally:
            db.discondb()
            print('đã ngắt kết nối')

    # tải dữ liệu tài khoản quản trị viên
    def loaddata_accountnadmin(self):
        self.uic_createadminwindow.datatable.setColumnWidth(4, 70)
        self.uic_createadminwindow.datatable.setColumnWidth(3, 250)
        self.uic_createadminwindow.datatable.setColumnWidth(2, 250)
        self.uic_createadminwindow.datatable.setColumnWidth(1, 400)
        self.uic_createadminwindow.datatable.setColumnWidth(0, 150)
        self.uic_createadminwindow.datatable.setHorizontalHeaderLabels(
            ["Mã tài khoản", "Họ và tên", "Tài khoản", "Mật khẩu", "Vai trò"])
        con = db.condb()
        print('đã kết nối thành công')
        try:
            query = "select id, hovaten, taikhoan, matkhau, vaitro from taikhoan;"
            cur = con.cursor()
            cur.execute(query)
            data = cur.fetchall()
            self.uic_createadminwindow.datatable.setRowCount(len(data))
            self.uic_createadminwindow.datatable.setColumnCount(5)
            for rownumber, rowdata in enumerate(data):
                for colnumber, data in enumerate(rowdata):
                    self.uic_createadminwindow.datatable.setItem(rownumber, colnumber,
                                                                 QtWidgets.QTableWidgetItem(str(data)))
        except:
            return con.rollback()
        finally:
            db.discondb()
            print('đã ngắt kết nối')
# # *******************chức năng chung*********************
#
#     # chức năng show thông báo
#     def showDialog(self, text):
#         msgBox = QMessageBox()
#         msgBox.setIcon(QMessageBox.Information)
#         msgBox.setText(text)
#         msgBox.setWindowTitle("Thông báo")
#         msgBox.setStandardButtons(QMessageBox.Ok)
#         msgBox.exec()
#
#     # chức năng chuyển văn bản thành giọng nói
#     def speakoutput(self, text):
#         if self.check_network_connection():
#             unique_filename = str(uuid.uuid4()) + ".mp3"
#
#             # Lấy đường dẫn thư mục gốc của ứng dụng
#             app_path = os.path.dirname(os.path.abspath(__file__))
#
#             # Tạo đường dẫn đến file âm thanh tạm trong cùng thư mục với ứng dụng
#             temp_file_path = os.path.join(app_path, unique_filename)
#
#             tts = gTTS(text=text, lang='vi', slow=False)
#
#             # Lưu file âm thanh
#             tts.save(temp_file_path)
#
#             self.player = QMediaPlayer()
#
#             # Tạo URL từ đường dẫn đến file âm thanh
#             url = QUrl.fromLocalFile(temp_file_path)
#
#             # Tạo nội dung media từ URL
#             content = QMediaContent(url)
#
#             self.player.setMedia(content)
#             self.player.play()
#
#             # Xóa file âm thanh sau khi đã phát xong
#             self.player.mediaStatusChanged.connect(lambda status: self.delete_temp_file(temp_file_path))
#
#     def delete_temp_file(self, file_path):
#         if os.path.exists(file_path):
#             os.remove(file_path)\

utils = Utils()

db = Database()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Mainwindow()
    main_win.show_admissionswindow()
    sys.exit(app.exec())


