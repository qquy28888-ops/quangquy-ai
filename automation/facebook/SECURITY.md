# Bảo mật và kiểm soát luồng Facebook

## Tuyệt đối không lưu trong GitHub

- OpenAI API key.
- Facebook access token.
- Make webhook secret.
- Telegram bot token.
- Cookie hoặc mật khẩu Facebook.
- File `.env` thật.

## Nơi lưu secret

- Make Connections hoặc Make Variables/Secrets.
- Google Colab Secrets khi chạy notebook.
- GitHub Actions Secrets nếu sau này dùng workflow.

## Kiểm soát trước khi đăng

1. Kiểm tra caption không chứa dữ liệu cá nhân.
2. Kiểm tra ảnh không có logo bên thứ ba hoặc nội dung nhạy cảm.
3. Kiểm tra Page/Fanpage được chọn đúng.
4. Kiểm tra lịch đăng không chạy quá nhiều lần.
5. Chặn bài khi trường `status` chưa phải `approved` ở Review mode.
6. Nếu module ảnh lỗi, không đăng bài chỉ có caption trừ khi đã cấu hình rõ.

## Xử lý lỗi

- Ghi lỗi vào Google Sheets.
- Gửi Telegram thông báo.
- Không retry vô hạn.
- Tối đa 2 lần retry cho lỗi tạm thời.
- Với lỗi quyền Facebook hoặc token, dừng scenario và yêu cầu kết nối lại.

## Giới hạn đăng

- Khởi động: tối đa 1 bài/ngày.
- Sau 10 bài ổn định: tối đa 2 bài/ngày nếu có nhu cầu thật.
- Không dùng lịch 15 phút cho scenario xuất bản.

## Quyền hành động

Phải hỏi người dùng trước khi:

- Chuyển từ Review mode sang Auto mode.
- Thay Fanpage đích.
- Tăng tần suất đăng.
- Bật đăng Reel/video.
- Thay đổi CTA hoặc định vị thương hiệu.
