create database TuVanGiaoDuc;
SET SQL_SAFE_UPDATES = 0;
use TuVanGiaoDuc;

CREATE TABLE ThongTinNguoiDung (
     id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
     hovaten VARCHAR(150) NOT NULL,
     sdt VARCHAR(13),
     cauhoi VARCHAR(1000) NOT NULL,
     cautraloi VARCHAR(10000) NOT NULL,
     thoigianhoi DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE TaiKhoan (
    id VARCHAR(120) PRIMARY KEY,
    hovaten VARCHAR(150) NOT NULL,
    taikhoan VARCHAR(50) NOT NULL,
    matkhau VARCHAR(50) NOT NULL,
    vaitro VARCHAR(30) NOT NULL,
    thoigiancapnhat DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE CauHoiTuVan (
    macauhoi VARCHAR(50) NOT NULL PRIMARY KEY,
    cauhoi VARCHAR(1000) NOT NULL,
    thoigiancapnhat DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    admin_id VARCHAR(120),
    FOREIGN KEY (admin_id) REFERENCES TaiKhoan(id)
);

CREATE TABLE TraLoiTuVan (
    macautraloi INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    macauhoi VARCHAR(50) NOT NULL,
    cautraloi VARCHAR(10000) NOT NULL,
    thoigiancapnhat DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    FOREIGN KEY (macauhoi) REFERENCES CauHoiTuVan(macauhoi)
);

CREATE TABLE CauHoiCongNgheThongTin (
    macauhoi VARCHAR(50) NOT NULL PRIMARY KEY,
    cauhoi VARCHAR(1000) NOT NULL,
    thoigiancapnhat DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    admin_id VARCHAR(120),
    FOREIGN KEY (admin_id) REFERENCES TaiKhoan(id)
);

CREATE TABLE TraLoiCongNgheThongTin (
    macautraloi INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    macauhoi VARCHAR(50) NOT NULL,
    cautraloi VARCHAR(10000) NOT NULL,
    thoigiancapnhat DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    FOREIGN KEY (macauhoi) REFERENCES CauHoiCongNgheThongTin(macauhoi)
);

CREATE TABLE CauHoiQuanTriKinhDoanh (
    macauhoi VARCHAR(50) NOT NULL PRIMARY KEY,
    cauhoi VARCHAR(1000) NOT NULL,
    thoigiancapnhat DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    admin_id VARCHAR(120),
    FOREIGN KEY (admin_id) REFERENCES TaiKhoan(id)
);

CREATE TABLE TraLoiQuanTriKinhDoanh (
    macautraloi INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    macauhoi VARCHAR(50) NOT NULL,
    cautraloi VARCHAR(10000) NOT NULL,
    thoigiancapnhat DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    FOREIGN KEY (macauhoi) REFERENCES CauHoiQuanTriKinhDoanh(macauhoi)
);

CREATE TABLE CauHoiDuLich (
    macauhoi VARCHAR(50) NOT NULL PRIMARY KEY,
    cauhoi VARCHAR(1000) NOT NULL,
    thoigiancapnhat DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    admin_id VARCHAR(120),
    FOREIGN KEY (admin_id) REFERENCES TaiKhoan(id)
);

CREATE TABLE TraLoiDuLich (
    macautraloi INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    macauhoi VARCHAR(50) NOT NULL,
    cautraloi VARCHAR(10000) NOT NULL,
    thoigiancapnhat DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    FOREIGN KEY (macauhoi) REFERENCES CauHoiDuLich(macauhoi)
);


INSERT INTO TaiKhoan (id, hovaten, taikhoan, matkhau, vaitro) VALUES (UUID(), 'nguyễn thanh bằng', 'bang', 'bang', 'Admin');
INSERT INTO TaiKhoan (id, hovaten, taikhoan, matkhau, vaitro) VALUES (UUID(), 'nguyễn thanh đức', 'duc', 'duc', 'Admin');
INSERT INTO TaiKhoan (id, hovaten, taikhoan, matkhau, vaitro) VALUES (UUID(), 'nguyễn trung kiên', 'kien', 'kien', 'Cán Bộ');

insert into ThongTinNguoiDung (hovaten, sdt, cauhoi, cautraloi) values ('nguyễn thanh bằng', '0973636954', 'ngày học', 'Sau ngày 3/5/2023 sinh viên đi học bình thường');
insert into thongtinnguoidung (hovaten, sdt, cauhoi, cautraloi) values ('nguyễn lam trường', '0973636954', 'bao nhiêu 1 tín chỉ', '398000 1 tín chỉ cho môn học chuyên ngành và 356000 cho tín chỉ môn chung ạ');

INSERT INTO CauHoiTuVan (macauhoi, cauhoi, admin_id) VALUES ('CH1', 'ngày học , ngày học là ngày nào , khi nào bắt đầu học , học khi nào , khi nào học', (SELECT id FROM TaiKhoan WHERE taikhoan = 'bang'));
INSERT INTO CauHoiTuVan (macauhoi, cauhoi, admin_id) VALUES ('CH2', 'bao nhiêu 1 tín chỉ, 1 tín chỉ bao nhiêu, tín chỉ, học phí bao nhiêu, học phí, học phí bao nhiêu 1 tín chỉ, bao nhiêu 1 chỉ', (SELECT id FROM TaiKhoan WHERE taikhoan = 'bang'));
INSERT INTO CauHoiTuVan (macauhoi, cauhoi, admin_id) VALUES ('CH3', 'Học bao lâu, học mấy năm, học lau không, học lâu không', (SELECT id FROM TaiKhoan WHERE taikhoan = 'bang'));
INSERT INTO CauHoiTuVan (macauhoi, cauhoi, admin_id) VALUES ('CH4', 'hoạt động ngoại khóa, Hoạt động ngoại khóa, HOẠT ĐỘNG NGOẠI KHÓA, ngoại khóa', (SELECT id FROM TaiKhoan WHERE taikhoan = 'bang'));
INSERT INTO CauHoiTuVan (macauhoi, cauhoi, admin_id) VALUES ('CH5', 'nhập học, nhập học online, thao tác nhập học, thao tác nhập học online, cách nhập học online, nhập học online', (SELECT id FROM TaiKhoan WHERE taikhoan = 'bang'));

INSERT INTO TraLoiTuVan (macauhoi, cautraloi)
VALUES ((SELECT macauhoi FROM CauHoiTuVan WHERE macauhoi = 'CH1'), 'Sau ngày 3/5/2023 sinh viên đi học bình thường');
INSERT INTO TraLoiTuVan (macauhoi, cautraloi)
VALUES ((SELECT macauhoi FROM CauHoiTuVan WHERE macauhoi = 'CH2'), '398000 1 tín chỉ cho môn học chuyên ngành và 356000 cho tín chỉ môn chung ạ');
INSERT INTO TraLoiTuVan (macauhoi, cautraloi)
VALUES ((SELECT macauhoi FROM CauHoiTuVan WHERE macauhoi = 'CH3'), 'do lượng kiến thức đầu ra tiêu chuẩn yêu cầu bắt buộc cho mỗi sinh viên là 150 tin chỉ nên thời gian học trung bình sẽ thường kéo dài từ 3 đến 4 năm bạn nhé');
INSERT INTO TraLoiTuVan (macauhoi, cautraloi)
VALUES ((SELECT macauhoi FROM CauHoiTuVan WHERE macauhoi = 'CH4'), 'trường đại học công nghệ sài gòn nói chung và khoa công nghệ thông tin nói riêng có nhiều các hoạt động ngoại khóa cho sinh viên như câu lạc bộ tin học, câu lạc bộ tiếng anh, câu lạc bộ tình nguyện, câu lạc bộ văn nghệ cùng rất nhiều các hoạt động khác như các giải thi đấu thể thao, thời trang, miss uneti vân vân. sinh viên có thể đăng ký tham gia các câu lạc bộ và các hoạt động phù hợp ');
INSERT INTO TraLoiTuVan (macauhoi, cautraloi)
VALUES ((SELECT macauhoi FROM CauHoiTuVan WHERE macauhoi = 'CH5'), 'Hiện tại Trường không có phương thức nhập học online. Em nên đến thẳng trực tiếp trường để tiến hành nộp hồ sơ.');