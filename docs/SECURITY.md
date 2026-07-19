# Bảo mật và giới hạn quyền

## Không lưu secret tại

- GitHub repository
- Notebook `.ipynb`
- Google Docs/Sheets thông thường
- Ảnh chụp màn hình hoặc tin nhắn công khai

## Lưu secret an toàn hơn

- Colab Secrets cho `GEMINI_API_KEY` và `GITHUB_TOKEN`.
- Biến môi trường tạm thời trong phiên chạy.
- Secret manager của nền tảng deploy khi website cần biến môi trường.

## Quyền GitHub token tối thiểu

Token chỉ cần quyền truy cập repository `quangquy-ai` và quyền Contents/Commit cần thiết. Không cấp quyền cho toàn bộ tài khoản nếu không cần.

## Hành động luôn cần xác nhận

- Xóa file
- Deploy production
- Thay domain/DNS
- Mở repository private thành public hoặc ngược lại
- Đưa dữ liệu khách hàng lên dịch vụ ngoài
- Bất kỳ thao tác nào có thể phát sinh phí
