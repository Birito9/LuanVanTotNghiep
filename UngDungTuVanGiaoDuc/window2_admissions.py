# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window2_admissions.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_admissions_window(object):
    def setupUi(self, admissions_window):
        admissions_window.setObjectName("admissions_window")
        admissions_window.resize(1280, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(admissions_window.sizePolicy().hasHeightForWidth())
        admissions_window.setSizePolicy(sizePolicy)
        admissions_window.setMinimumSize(QtCore.QSize(1280, 800))
        admissions_window.setMaximumSize(QtCore.QSize(1280, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        admissions_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(admissions_window)
        self.centralwidget.setObjectName("centralwidget")
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.logout.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.logout.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Tahoma\";\n"
"    border-radius: 10px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"    font: 75 14pt \"Tahoma\";\n"
"    border-radius: 10px;\n"
"    border: 3px solid #2f638e;\n"
"    font-weight: bold;\n"
"}")
        self.logout.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout.setIcon(icon1)
        self.logout.setIconSize(QtCore.QSize(57, 25))
        self.logout.setAutoDefault(False)
        self.logout.setObjectName("logout")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(40, 80, 181, 131))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.record = QtWidgets.QPushButton(self.centralwidget)
        self.record.setGeometry(QtCore.QRect(700, 730, 121, 51))
        self.record.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.record.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Tahoma\";\n"
"    border-radius: 10px;\n"
"    background-color: rgba(74,167,72,95%);\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"    font: 75 14pt \"Tahoma\";\n"
"    border-radius: 10px;\n"
"    border: 3px solid #4AA748;\n"
"    background-color: rgba(132,193,65,65%);\n"
"    font-weight: bold;\n"
"}")
        self.record.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/microphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.record.setIcon(icon2)
        self.record.setIconSize(QtCore.QSize(64, 64))
        self.record.setAutoRepeat(False)
        self.record.setAutoRepeatDelay(301)
        self.record.setAutoDefault(False)
        self.record.setDefault(False)
        self.record.setObjectName("record")
        self.question_send = QtWidgets.QPushButton(self.centralwidget)
        self.question_send.setGeometry(QtCore.QRect(700, 660, 121, 51))
        self.question_send.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.question_send.setStyleSheet("QPushButton{\n"
"    font: 75 12pt \"Tahoma\";\n"
"    border-radius: 10px;\n"
"    background-color: rgba(34,65,134,90%);\n"
"    color: rgb(255, 255, 255);\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"    font: 75 14pt \"Tahoma\";\n"
"    border-radius: 10px;\n"
"    border: 3px solid rgb(59,108,212);\n"
"    background-color: rgba(59,108,212,65%);\n"
"    font-weight: bold;\n"
"}")
        self.question_send.setIconSize(QtCore.QSize(57, 25))
        self.question_send.setAutoDefault(False)
        self.question_send.setObjectName("question_send")
        self.user_ouput = QtWidgets.QLabel(self.centralwidget)
        self.user_ouput.setEnabled(True)
        self.user_ouput.setGeometry(QtCore.QRect(60, 560, 761, 81))
        self.user_ouput.setStyleSheet("QLabel{\n"
"    font: 75 10pt \"HungHau\";\n"
"    border-radius: 10px;\n"
"    background-color: rgba(255, 255, 255,80%);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"    font: 75 12pt \"HungHau\";\n"
"    border: 2px solid #92D050;\n"
"    background-color: rgba(255, 255, 255,90%);\n"
"    font-weight: bold;\n"
"}")
        self.user_ouput.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.user_ouput.setObjectName("user_ouput")
        self.question_input = QtWidgets.QLineEdit(self.centralwidget)
        self.question_input.setGeometry(QtCore.QRect(220, 660, 441, 51))
        self.question_input.setStyleSheet("QLineEdit{\n"
"    font: 75 10pt \"HungHau\";\n"
"    border-radius: 10px;\n"
"    background-color: rgba(255, 255, 255,80%);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    font: 75 12pt \"HungHau\";\n"
"    border: 2px solid #92D050;\n"
"    background-color: rgba(255, 255, 255,90%);\n"
"    font-weight: bold;\n"
"}")
        self.question_input.setObjectName("question_input")
        self.name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.name_input.setGeometry(QtCore.QRect(460, 90, 351, 41))
        self.name_input.setStyleSheet("QLineEdit{\n"
"    font: 75 10pt \"HungHau\";\n"
"    border-radius: 10px;\n"
"    background-color: rgba(255, 255, 255,80%);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    font: 75 12pt \"HungHau\";\n"
"    border: 2px solid #92D050;\n"
"    background-color: rgba(255, 255, 255,90%);\n"
"    font-weight: bold;\n"
"}")
        self.name_input.setObjectName("name_input")
        self.numberphone_input = QtWidgets.QLineEdit(self.centralwidget)
        self.numberphone_input.setGeometry(QtCore.QRect(460, 190, 351, 41))
        self.numberphone_input.setStyleSheet("QLineEdit{\n"
"    font: 75 10pt \"HungHau\";\n"
"    border-radius: 10px;\n"
"    background-color: rgba(255, 255, 255,80%);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    font: 75 12pt \"HungHau\";\n"
"    border: 2px solid #92D050;\n"
"    background-color: rgba(255, 255, 255,90%);\n"
"    font-weight: bold;\n"
"}")
        self.numberphone_input.setObjectName("numberphone_input")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1920, 800))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("img/background.jpg"))
        self.background.setScaledContents(True)
        self.background.setWordWrap(False)
        self.background.setOpenExternalLinks(False)
        self.background.setObjectName("background")
        self.background_fillter = QtWidgets.QLabel(self.centralwidget)
        self.background_fillter.setEnabled(False)
        self.background_fillter.setGeometry(QtCore.QRect(0, 0, 1291, 800))
        self.background_fillter.setMouseTracking(False)
        self.background_fillter.setTabletTracking(False)
        self.background_fillter.setFocusPolicy(QtCore.Qt.NoFocus)
        self.background_fillter.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.background_fillter.setAutoFillBackground(False)
        self.background_fillter.setStyleSheet("QLabel{\n"
"    background: rgb(8, 78, 142,60%);\n"
"}")
        self.background_fillter.setText("")
        self.background_fillter.setObjectName("background_fillter")
        self.bot_output = QtWidgets.QTextEdit(self.centralwidget)
        self.bot_output.setEnabled(True)
        self.bot_output.setGeometry(QtCore.QRect(56, 300, 761, 181))
        self.bot_output.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.bot_output.setStyleSheet("QTextEdit{\n"
"    font: 75 10pt \"HungHau\";\n"
"    border-radius: 10px;\n"
"    background-color: rgba(255, 255, 255,80%);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTextEdit:hover{\n"
"    font: 75 12pt \"HungHau\";\n"
"    border: 2px solid #92D050;\n"
"    background-color: rgba(255, 255, 255,90%);\n"
"    font-weight: bold;\n"
"}")
        self.bot_output.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.bot_output.setObjectName("bot_output")
        self.choosetable_box = QtWidgets.QComboBox(self.centralwidget)
        self.choosetable_box.setGeometry(QtCore.QRect(460, 140, 351, 41))
        self.choosetable_box.setStyleSheet("QComboBox{\n"
"    font: 75 10pt \"Tahoma\";\n"
"    border-radius: 10px;\n"
"    background-color: rgba(255, 255, 255,80%);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    font: 75 12pt \"Tahoma\";\n"
"    border: 2px solid #92D050;\n"
"    background-color: rgba(255, 255, 255,90%);\n"
"    font-weight: bold;\n"
"}")
        self.choosetable_box.setObjectName("choosetable_box")
        self.choosetable_box.addItem("")
        self.choosetable_box.addItem("")
        self.choosetable_box.addItem("")
        self.choosetable_box.addItem("")
        self.hintquestion = QtWidgets.QTableWidget(self.centralwidget)
        self.hintquestion.setGeometry(QtCore.QRect(850, 90, 401, 691))
        self.hintquestion.setStyleSheet("QTableWidget{\n"
"    font: 75 10pt \"HungHau\";\n"
"    border-radius: 10px;\n"
"    background-color: rgba(255, 255, 255,80%);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"    font: 75 12pt \"HungHau\";\n"
"    border: 2px solid #92D050;\n"
"    background-color: rgba(255, 255, 255,90%);\n"
"    font-weight: bold;\n"
"}")
        self.hintquestion.setColumnCount(2)
        self.hintquestion.setObjectName("hintquestion")
        self.hintquestion.setRowCount(0)
        self.tittle_hintquestion = QtWidgets.QPushButton(self.centralwidget)
        self.tittle_hintquestion.setGeometry(QtCore.QRect(900, 40, 291, 31))
        font = QtGui.QFont()
        font.setFamily("HungHau")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tittle_hintquestion.setFont(font)
        self.tittle_hintquestion.setTabletTracking(False)
        self.tittle_hintquestion.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"HungHau\";\n"
"    border-radius: 20px;\n"
"    font-weight: bold;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    font: 75 18pt \"HungHau\";\n"
"    border-radius: 20px;\n"
"    font-weight: bold;\n"
"\n"
"}")
        self.tittle_hintquestion.setObjectName("tittle_hintquestion")
        self.tittle_name = QtWidgets.QPushButton(self.centralwidget)
        self.tittle_name.setGeometry(QtCore.QRect(280, 90, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tittle_name.setFont(font)
        self.tittle_name.setTabletTracking(False)
        self.tittle_name.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Tahoma\";\n"
"    border-radius: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"    font: 75 14pt \"Tahoma\";\n"
"    border-radius: 20px;\n"
"    font-weight: bold;\n"
"}")
        self.tittle_name.setObjectName("tittle_name")
        self.tittle_choosetable = QtWidgets.QPushButton(self.centralwidget)
        self.tittle_choosetable.setGeometry(QtCore.QRect(280, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tittle_choosetable.setFont(font)
        self.tittle_choosetable.setTabletTracking(False)
        self.tittle_choosetable.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Tahoma\";\n"
"    border-radius: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"    font: 75 14pt \"Tahoma\";\n"
"    border-radius: 20px;\n"
"    font-weight: bold;\n"
"}")
        self.tittle_choosetable.setObjectName("tittle_choosetable")
        self.tittle_numberphone = QtWidgets.QPushButton(self.centralwidget)
        self.tittle_numberphone.setGeometry(QtCore.QRect(280, 190, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tittle_numberphone.setFont(font)
        self.tittle_numberphone.setTabletTracking(False)
        self.tittle_numberphone.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Tahoma\";\n"
"    border-radius: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"    font: 75 14pt \"Tahoma\";\n"
"    border-radius: 20px;\n"
"    font-weight: bold;\n"
"}")
        self.tittle_numberphone.setObjectName("tittle_numberphone")
        self.tittle_bot = QtWidgets.QPushButton(self.centralwidget)
        self.tittle_bot.setGeometry(QtCore.QRect(60, 250, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tittle_bot.setFont(font)
        self.tittle_bot.setTabletTracking(False)
        self.tittle_bot.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"Tahoma\";\n"
"    border-radius: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"    font: 75 16pt \"Tahoma\";\n"
"    border-radius: 20px;\n"
"    font-weight: bold;\n"
"}")
        self.tittle_bot.setObjectName("tittle_bot")
        self.tittle_user = QtWidgets.QPushButton(self.centralwidget)
        self.tittle_user.setGeometry(QtCore.QRect(640, 510, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tittle_user.setFont(font)
        self.tittle_user.setTabletTracking(False)
        self.tittle_user.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"Tahoma\";\n"
"    border-radius: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"    font: 75 16pt \"Tahoma\";\n"
"    border-radius: 20px;\n"
"    font-weight: bold;\n"
"}")
        self.tittle_user.setObjectName("tittle_user")
        self.refresh_button = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_button.setGeometry(QtCore.QRect(60, 660, 131, 51))
        self.refresh_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.refresh_button.setStyleSheet("QPushButton{\n"
"    color: rgb(255,255,255);\n"
"    font: 75 14pt \"Tahoma\";\n"
"    border-radius: 10px;\n"
"    background-color: rgb(177, 196, 229,75%);\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"    font: 75 16pt \"Tahoma\";\n"
"    border-radius: 10px;\n"
"    border: 3px solid #b1c4e5;\n"
"    background-color: rgb(177, 196, 229,60%);\n"
"    font-weight: bold;\n"
"}")
        self.refresh_button.setIconSize(QtCore.QSize(57, 25))
        self.refresh_button.setAutoDefault(False)
        self.refresh_button.setObjectName("refresh_button")
        self.background.raise_()
        self.background_fillter.raise_()
        self.logout.raise_()
        self.logo.raise_()
        self.record.raise_()
        self.question_send.raise_()
        self.user_ouput.raise_()
        self.question_input.raise_()
        self.name_input.raise_()
        self.numberphone_input.raise_()
        self.bot_output.raise_()
        self.choosetable_box.raise_()
        self.hintquestion.raise_()
        self.tittle_hintquestion.raise_()
        self.tittle_name.raise_()
        self.tittle_choosetable.raise_()
        self.tittle_numberphone.raise_()
        self.tittle_bot.raise_()
        self.tittle_user.raise_()
        self.refresh_button.raise_()
        admissions_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(admissions_window)
        QtCore.QMetaObject.connectSlotsByName(admissions_window)

    def retranslateUi(self, admissions_window):
        _translate = QtCore.QCoreApplication.translate
        admissions_window.setWindowTitle(_translate("admissions_window", "TƯ VẤN GIÁO DỤC"))
        self.question_send.setText(_translate("admissions_window", "Gửi"))
        self.user_ouput.setText(_translate("admissions_window", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.question_input.setPlaceholderText(_translate("admissions_window", "  Nhập nội dung tại đây"))
        self.choosetable_box.setItemText(0, _translate("admissions_window", "Tư vấn chung"))
        self.choosetable_box.setItemText(1, _translate("admissions_window", "Du lịch"))
        self.choosetable_box.setItemText(2, _translate("admissions_window", "Công nghệ thông tin"))
        self.choosetable_box.setItemText(3, _translate("admissions_window", "Quản Trị Kinh Doanh"))
        self.tittle_hintquestion.setText(_translate("admissions_window", "CÂU HỎI GỢI Ý"))
        self.tittle_name.setText(_translate("admissions_window", "Họ Và Tên"))
        self.tittle_choosetable.setText(_translate("admissions_window", "Ngành"))
        self.tittle_numberphone.setText(_translate("admissions_window", "Số Điện Thoại"))
        self.tittle_bot.setText(_translate("admissions_window", "Trợ Lý Tư Vấn"))
        self.tittle_user.setText(_translate("admissions_window", "Người Dùng"))
        self.refresh_button.setText(_translate("admissions_window", "Tải lại"))
