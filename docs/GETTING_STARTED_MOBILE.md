# Bắt đầu từ điện thoại

## 1. Mở Google Drive

Tìm thư mục **QuangQuy AI Workspace**. Dùng các thư mục:

- `06_Inbox`: thả file mới cần xử lý.
- `03_Assets`: ảnh, video và logo.
- `04_Exports`: file AI đã tạo.
- `05_Backups`: bản sao trước thay đổi lớn.

## 2. Mở notebook Colab

Notebook chính: `QuangQuy_AI_Control_Center.ipynb`.

Trong Colab:

1. Bật quyền truy cập Drive.
2. Thêm `GEMINI_API_KEY` và `GITHUB_TOKEN` trong mục Secrets.
3. Chạy từng ô từ trên xuống.
4. Điền `TASK` bằng tiếng Việt.
5. Xem kế hoạch trước khi bật `APPROVE = True`.
6. Chỉ push lên branch mới; không push thẳng `main`.

## 3. Giao việc qua ChatGPT

Mẫu ngắn:

```text
Dự án: qquy28888-ops/quangquy-ai
Mục tiêu: ...
Hãy đọc branch ... và review thay đổi. Chỉ ra lỗi trước khi merge.
```

## 4. Khi máy tính mượn phải trả lại

- Kiểm tra code đã push GitHub.
- Kiểm tra file đầu vào/đầu ra đã nằm trong Drive.
- Đăng xuất GitHub, Google và xóa credential khỏi máy.
- Không để dữ liệu quan trọng chỉ nằm trên ổ cứng máy mượn.
