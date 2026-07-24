# Instagram Bridge → Facebook cá nhân

## Mục tiêu

Dùng Instagram `quy28_01` làm điểm xuất bản kỹ thuật, sau đó để Accounts Center tự động chia sẻ bài sang Facebook cá nhân `quangquy88`.

Fanpage không tham gia luồng đăng chính. Threads tạm tắt.

## Luồng dự kiến

```text
Scheduler 08:00 / 13:00 / 18:00
→ Google Sheets lấy lịch sử 30 chủ đề gần nhất
→ AI tạo caption + prompt ảnh
→ AI tạo ảnh 4:5
→ Make HTTP gọi Instagram API with Instagram Login
→ đăng lên Instagram quy28_01
→ Accounts Center tự chia sẻ sang Facebook quangquy88
→ kiểm tra bài Facebook xuất hiện và để chế độ Public
→ lưu kết quả + gửi Telegram
```

## Điều kiện bắt buộc

1. Chuyển Instagram `quy28_01` từ Personal sang Creator.
2. Không liên kết Creator account với Facebook Page nếu mục tiêu là chia sẻ sang Facebook Profile cá nhân.
3. Instagram và Facebook `quangquy88` phải nằm trong cùng Accounts Center.
4. Bật `Sharing across profiles` từ Instagram sang Facebook cá nhân.
5. Facebook audience đặt `Public`.
6. Xác thực Instagram bằng OAuth/API chính thức; không dùng mật khẩu, cookie, OTP hoặc session token.

## Công cụ Make

Không dùng module `Instagram for Business (Facebook login)` vì module đó yêu cầu Business account và Facebook Page.

Dùng một trong hai cách:

- Make HTTP + Instagram API with Instagram Login.
- n8n HTTP Request + Instagram API with Instagram Login nếu Make không hỗ trợ OAuth phù hợp.

API cần quyền tối thiểu:

- `instagram_business_basic`
- `instagram_business_content_publish`

## Điểm chưa được Meta bảo đảm

Accounts Center đã được người dùng kiểm chứng hoạt động khi đăng bài thủ công trong ứng dụng Instagram. Tuy nhiên, tài liệu công khai không cam kết rõ rằng bài được tạo qua API sẽ luôn kích hoạt tự động chia sẻ sang Facebook Profile cá nhân.

Do đó phải chạy bài thử API trước khi bật lịch:

1. Một ảnh 4:5 không nhạc.
2. Kiểm tra bài xuất hiện trên Instagram.
3. Chờ 3–5 phút.
4. Kiểm tra bài xuất hiện trên Facebook `quangquy88` với audience Public.
5. Chỉ khi đạt mới chạy thêm hai bài thử.

## Chính sách lỗi

Nếu Instagram không đăng được:

- không tạo bài;
- ghi lỗi;
- báo Telegram.

Nếu Instagram đăng được nhưng Facebook không nhận bài:

- dừng scenario;
- không đăng bài kế tiếp;
- báo Telegram và cung cấp link bài Instagram;
- người dùng xử lý hoặc xóa thủ công.

Không thể bảo đảm xóa tự động bài trên Facebook Profile cá nhân bằng API chính thức.

## Nhạc

Full-auto mặc định không dùng nhạc thư viện Instagram.

Các bài cần nhạc bản quyền phải chuyển sang bán tự động: AI tạo caption và ảnh, người dùng mở ứng dụng Instagram, chọn nhạc được cấp phép rồi đăng.
