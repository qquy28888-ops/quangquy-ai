# QuangQuy AI — Facebook Content Automation

Hệ thống tạo nội dung, tạo ảnh và đăng tự động lên **Facebook Fanpage** bằng Make.

## Kiến trúc

```text
Scheduler
  → Google Sheets lấy chủ đề và lịch sử gần nhất
  → OpenAI tạo caption + prompt ảnh dạng JSON
  → JSON Parse
  → OpenAI tạo ảnh
  → Facebook Pages: Create a Post with Photos
  → Google Sheets lưu kết quả
  → Telegram gửi thông báo
```

## Nguyên tắc

1. Chỉ đăng bằng module **Facebook Pages**, không dùng cookie hoặc giả lập trình duyệt.
2. Không lưu API key, token Facebook hoặc thông tin đăng nhập trong GitHub.
3. Chạy thử bằng `Run once` trước khi bật lịch.
4. Bật chế độ duyệt thủ công trong giai đoạn đầu.
5. Lưu ít nhất 20 chủ đề gần nhất để tránh lặp nội dung.
6. Không đăng trực tiếp lên Facebook Profile cá nhân bằng luồng này.

## Hai chế độ

### Review mode — khuyến nghị khi mới chạy

```text
AI tạo bài + ảnh
→ gửi Telegram
→ người dùng duyệt
→ Make đăng Fanpage
```

### Auto mode

```text
AI tạo bài + ảnh
→ kiểm tra điều kiện
→ đăng Fanpage
→ báo kết quả
```

Chỉ bật Auto mode sau khi đã chạy ổn định ít nhất 10 bài thử.

## File liên quan

- `MAKE_SCENARIO.md`: hướng dẫn dựng scenario.
- `prompts/content_and_image_prompt.md`: prompt chuẩn để sinh caption và prompt ảnh.
- `config/content_plan.json`: định vị nội dung và lịch mẫu.
- `examples/webhook_payload.json`: payload mẫu khi gọi từ ChatGPT hoặc webhook.
- `content_queue_template.csv`: mẫu dữ liệu quản lý chủ đề.
- `SECURITY.md`: quy tắc bảo mật và kiểm soát lỗi.
