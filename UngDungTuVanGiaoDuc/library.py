'''
các gói cài đặt thư viện cài đặt:
pip install wheel
pip install pipwin
pipwin refresh
pipwin install pyaudio
pip install pyttsx3
pip install speechrecognition
Pip install PyQt5designer
Pip install PyQt5 tools
Pip install PyQt5
pip install pyinstaller
pip install mysql-connector-python
pip install gTTS

# Kết nối giao diện
pyuic5 -x [tên file của qt].ui -o [tên file của python].py
pyuic5 window6_createadmin.ui -o window6_createadmin.py
pyuic5 window5_infouser.ui -o window5_infouser.py
pyuic5 window4_datatable.ui -o window4_datatable.py
pyuic5 window3_choosetable.ui -o window3_choosetable.py
pyuic5 window2_admissions.ui -o window2_admissions.py
pyuic5 window1_startup.ui -o window1_startup.py
# Nén thành ứng dụng
pyinstaller --onefile --windowed --icon=logo.ico --add-data "database.py;." --add-data "library.py;." --add-data "utils.py;." tuvangiaoduc.py

'''

import datetime
import uuid #Tạo giá trị ngẫu nhiên cho id
import speech_recognition as lis #lấy giọng nói
from gtts import gTTS #lấy giọng nói của chị google
import mysql.connector #kết nối với mysql
import sys #thư viện hệ thống
import os #thư viện tương tác với hệ điều hành
from openpyxl import Workbook #xuất file excel
import requests

#thư viện của qtdesigner
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl, QTimer, QCoreApplication
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent

#kết nối file qt
from window1_startup import Ui_startup_window
from window2_admissions import Ui_admissions_window
from window3_choosetable import Ui_choosetable_window
from window4_datatable import Ui_datatable_window
from window5_infouser import Ui_userinfo_window
from window6_createadmin import Ui_createadmin_window