from library import *

class Utils:

    # kiểm tra kết nối mạng
    def check_network_connection(self):
        try:
            requests.get('https://www.google.com')
            return True
        except requests.ConnectionError:
            return False

    # chức năng show thông báo
    def showDialog(self, text):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setWindowTitle("Thông báo")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    # chức năng chuyển văn bản thành giọng nói
    def speakoutput(self, text):
        if self.check_network_connection():
            unique_filename = str(uuid.uuid4()) + ".mp3"

            # Lấy đường dẫn thư mục gốc của ứng dụng
            app_path = os.path.dirname(os.path.abspath(__file__))

            # Tạo đường dẫn đến file âm thanh tạm trong cùng thư mục với ứng dụng
            temp_file_path = os.path.join(app_path, unique_filename)

            tts = gTTS(text=text, lang='vi', slow=False)

            # Lưu file âm thanh
            tts.save(temp_file_path)

            self.player = QMediaPlayer()

            # Tạo URL từ đường dẫn đến file âm thanh
            url = QUrl.fromLocalFile(temp_file_path)

            # Tạo nội dung media từ URL
            content = QMediaContent(url)

            self.player.setMedia(content)
            self.player.play()

            # Xóa file âm thanh sau khi đã phát xong
            self.player.mediaStatusChanged.connect(lambda status: self.delete_temp_file(temp_file_path))

    def delete_temp_file(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
