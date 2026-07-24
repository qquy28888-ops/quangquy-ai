# Agent Roles

## 1. Orchestrator — ChatGPT

- Làm rõ mục tiêu kinh doanh.
- Chia tác vụ thành đầu ra cụ thể.
- Chỉ ra giả định, rủi ro và tiêu chí hoàn thành.
- Review pull request và quyết định bước tiếp theo.

## 2. Builder — Gemini trong Colab

- Đọc các file được lựa chọn.
- Trả về kế hoạch có cấu trúc JSON.
- Chỉ tạo/cập nhật file; không tự xóa.
- Chạy kiểm tra được cho phép sau khi sửa.

## 3. Reviewer — ChatGPT hoặc Claude

- Kiểm tra lỗi logic, bảo mật, UX và khả năng bảo trì.
- Không tự merge nếu chưa được chủ sở hữu duyệt.

## 4. Automation Runner — Make/n8n

- Nhận webhook hoặc lịch chạy.
- Tạo nội dung, gửi Telegram duyệt, lưu Google Sheets.
- Không tự thực hiện hành động công khai nếu chưa có cơ chế duyệt.

## Mẫu giao việc

```text
Mục tiêu:
Phạm vi file:
Kết quả mong muốn:
Không được làm:
Tiêu chí hoàn thành:
Mức tự động: chỉ lập kế hoạch / tự sửa rủi ro thấp / hỏi trước mọi thay đổi
```
