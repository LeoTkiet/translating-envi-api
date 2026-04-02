# Translation API Project (English to Vietnamese)

Đây là một API đơn giản sử dụng **FastAPI** và mô hình **Helsinki-NLP/opus-mt-en-vi** từ Hugging Face để thực hiện dịch thuật từ tiếng Anh sang tiếng Việt.

## Mục tiêu
Cung cấp một dịch vụ web API cho phép người dùng gửi văn bản tiếng Anh và nhận lại bản dịch tiếng Việt chính xác nhờ vào các mô hình Transformer hiện đại.

## Cài đặt

### 1. Yêu cầu hệ thống
- Python 3.8 trở lên.
- Đã cài đặt `pip`.

### 2. Cài đặt thư viện
Chạy lệnh sau để cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

*Lưu ý: Bạn cũng cần cài đặt `sentencepiece` và `sacremoses` để hỗ trợ tokenization cho mô hình Marian.*

## Cấu trúc Project
- `main.py`: Chứa mã nguồn chính của API (sử dụng FastAPI).
- `requirements.txt`: Danh sách các thư viện cần thiết.
- `test_api.py`: Script dùng để kiểm tra hoạt động của API.

## Cách chạy ứng dụng

### 1. Khởi chạy API Server
Sử dụng `uvicorn` để chạy server:
```bash
uvicorn main:app --reload
```
Mặc định server sẽ chạy tại `http://127.0.0.1:8000`.

### 2. Tài liệu API (Swagger UI)
Bạn có thể truy cập giao diện thử nghiệm API trực tiếp tại:
`http://127.0.0.1:8000/docs`

## Kiểm tra API
Bạn có thể chạy script `test_api.py` để gửi một yêu cầu mẫu:
```bash
python test_api.py
```

## Đóng góp
Mọi đóng góp vui lòng tạo Pull Request hoặc Issue.

## Video demo
https://github.com/user-attachments/assets/e11ca5fc-22e3-49ee-9bb9-9cb2c93c207c




