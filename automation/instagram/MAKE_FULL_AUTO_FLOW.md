# Make Full Auto Flow — Instagram → Facebook + Threads

## Mục tiêu

Đăng tự động mỗi ngày vào 08:00, 13:00 và 18:00 theo giờ Việt Nam.

Điểm xuất bản chính:

- Instagram: `quy28_01`
- Facebook nhận đồng bộ: `quangquy88`
- Threads nhận đồng bộ qua Accounts Center

## Quy tắc xác thực

Chỉ dùng OAuth/API chính thức.

Không dùng:

- mật khẩu gửi qua chat
- cookie
- OTP
- session token
- Selenium hoặc Playwright giả lập đăng nhập

## Điều kiện tài khoản

1. Instagram phải là tài khoản Professional.
2. Giữ bật Accounts Center → Sharing across profiles.
3. Không đổi sang Instagram Business chỉ để dùng module Make nếu việc đó làm mất khả năng chia sẻ sang Facebook Profile cá nhân.
4. Nếu tài khoản là Creator và module `Instagram for Business (Facebook login)` không nhận tài khoản, dùng Make HTTP với Instagram API with Instagram Login hoặc chuyển sang n8n HTTP Request.

## Lịch chạy

Trong Schedule settings của Make:

- Type: Daily
- Time zone: `Asia/Ho_Chi_Minh`
- Run times:
  - `08:00`
  - `13:00`
  - `18:00`

Một scenario có thể chứa nhiều giờ chạy trong Daily schedule.

## Luồng chính

```text
1. Scheduler
2. Google Sheets — Search Rows
3. Google Sheets — lấy 30 chủ đề đã đăng gần nhất
4. OpenAI — tạo JSON gồm caption + image_prompt + alt_text
5. JSON — Parse JSON
6. OpenAI hoặc Gemini — tạo ảnh 4:5
7. HTTP — lưu ảnh ở URL công khai nếu API yêu cầu
8. Instagram API — tạo media container
9. Instagram API — publish media
10. Delay 60–120 giây
11. Kiểm tra bài đã xuất hiện trên Instagram
12. Google Sheets — lưu media_id, caption, topic và URL
13. Telegram — báo kết quả
```

## Nội dung theo khung giờ

### 08:00 — Giáo dục thị trường

- Kiến thức AI dễ hiểu
- Sai lầm khi ứng dụng AI
- Checklist hoặc framework

### 13:00 — Workflow thực tế

- Quy trình tự động hóa cụ thể
- Case dành cho spa hoặc doanh nghiệp nhỏ
- Sơ đồ đầu vào → AI → CRM → nhân viên

### 18:00 — Góc nhìn và CTA

- Quan điểm cá nhân của Nguyễn Quang Quý
- Bài học triển khai
- CTA bình luận hoặc nhắn tin

## Chống lặp

Trước mỗi lần tạo bài:

1. Lấy 30 chủ đề gần nhất có trạng thái `posted`.
2. Đưa danh sách đó vào prompt.
3. Yêu cầu không lặp hook, ví dụ và CTA trong 14 ngày.
4. Tính một `topic_key` chuẩn hóa và kiểm tra trùng trước khi đăng.

## Chế độ kiểm thử bắt buộc

Trước khi bật Auto mode, chạy ba bài thử qua API:

1. Một ảnh 4:5 không nhạc.
2. Một carousel 2 ảnh không nhạc.
3. Một Reel có original audio nếu cần.

Mỗi bài phải được kiểm tra:

- xuất hiện đúng trên Instagram
- tự đồng bộ sang Facebook `quangquy88`
- tự đồng bộ sang Threads
- caption không bị lỗi định dạng
- quyền riêng tư Facebook là Public

Chỉ bật Auto mode khi cả ba bài thử đạt yêu cầu.

## Nhạc

Không xem nhạc trong thư viện Instagram là một phần mặc định của flow API.

- Bài ảnh có nhạc chọn trong app có thể không tái tạo được qua API.
- Với Reel, có thể dùng original audio đã ghép sẵn trong file MP4.
- Không tự động tải hoặc nhúng nhạc có bản quyền không có quyền sử dụng.

## Bảo vệ thương hiệu

- Tối đa 3 bài/ngày theo lịch đã chốt.
- Không đăng khi caption rỗng hoặc ảnh lỗi.
- Không đăng lại cùng `topic_key` trong 14 ngày.
- Dừng scenario sau 2 lỗi liên tiếp và gửi Telegram.
- Không đưa API key/token vào Google Sheets hoặc GitHub.
