# ỨNG DỤNG CÔNG NGHỆ CHATBOT XÂY DỰNG GIÁO VỤ ẢO HỖ TRỢ SINH VIÊN

Luận văn tốt nghiệp 

Luận văn tập trung vào việc nghiên cứu và phát triển một ứng dụng Chatbot dùng để giải đáp các thắc mắc liên quan đến giáo vụ trong môi trường trường Đại học Công nghệ Sài Gòn STU. Ứng dụng Chatbot hỗ trợ giáo vụ có thể giảm bớt lượng công việc của các cán bộ quản lý giáo dục trong mùa cao điểm, không tập trung đông người và gây ồn ào ở các phòng, khoa giáo vụ. Chatbot có thể tự động trả lời câu hỏi phổ biến và cung cấp thông tin liên quan đến tuyển sinh, học phí, lịch học, và các dịch vụ khác trong trường.

![messenger](https://i.imgur.com/Hdlubdf.png)


### Chức năng chính
- Quản lý tài khoản ứng dụng: Quản lý tài khoản của cán bộ phòng ban và các quản trị viên
- Quản lý dữ liệu tư vấn: Lưu trữ và quản lý dữ liệu tư vấn giữa cán bộ phòng ban và sinh viên, giúp dễ dàng tra cứu và thống kê thông tin.
- Hỏi đáp tự động: Người dùng có thể đặt câu hỏi về các vấn đề liên quan đến giáo vụ, và chatbot sẽ cung cấp câu trả lời một cách tự động và nhanh chóng.
- Hỗ trợ giọng nói: Chatbot hỗ trợ tính năng giọng nói để người dùng có thể tương tác bằng cách nói câu hỏi và nghe câu trả lời.


Nhiều tính năng mới sẽ được cập nhật thêm sau (Nếu tôi đủ trình độ).



### Yêu cầu cài đặt
 Pycharm  
 MySQL 8.0  
 Qt Designer  
 Python 3.10  

### Hướng dẫn cài đặt
Mình đã viết một file word để hướng dẫn sử dụng.

## Tải Source Code về
#### Clone the Repository (Phương án khuyên dùng)

Nếu đã cài đặt Github desktop thì đây là phương án tôi khuyên dùng, vì như thế bạn sẽ có thể nhanh chóng cập nhật cùng phiên bản mới nhất. Và đây cũng là cách phù hợp nhất nếu bạn có ý định đóng góp thêm vào dự án này.

Hãy dùng các lệnh sau để clone rep về:
```bash
$ mkdir TuVanGiaoDuc
$ cd TuVanGiaoDuc
$ git clone https://github.com/Birito9/UngDungTuVanGiaoDuc.git
```

### Luôn cập nhật bản mới nhất
Tôi không quan tâm bạn chọn tải source code về bằng kiểu gì, nhưng việc cập nhật phiên bản mới nhất là rất quan trọng, vì trong đó sẽ chứa các tính năng (thậm chí là bugs mới). Nhớ hãy gắn **Sao(*)** cho project này để được thông báo khi tôi update bản mới nhé. 

## Build

Trước khi chúng ta nhảy vào build và chạy app Godchat, hãy đảm bảo kỹ lưỡng những yếu tố sau .

 - Chạy ứng dụng bằng Pycharm và cài đặt một số thư viện: 
wheel, pipwin, pyaudio, pyttsx3, speechrecognition, PyQt5 tools, PyQt5designer, PyQt5, pyinstaller, mysql-connector-python, gTTS


Build lại rất đơn giản:

 1. Mở Pycharm
 2. Mở project này ở folder mà bạn đã tải xuống bằng menu `File -> Open`
 3. Chạy các thư viện đã có sẵn trong file library.py
 5. Một khi build xong `Run -> Run file TuVanGiaoDuc.py`
 6. Xong xuôi rồi đó, bạn sẽ thấy màn hình chào mừng như hình dưới.


## Credit

- [Thanh Bằng - Developer](https://www.facebook.com/nguyenthanhbang6/)
