# Thử nghiệm 7 ngày — Instagram → Facebook + Threads

## Quyết định đã chốt

- Instagram nguồn: `quy28_01`
- Facebook nhận đồng bộ: `quangquy88`
- Threads nhận đồng bộ qua Accounts Center
- Lịch: 08:00, 13:00, 18:00 hằng ngày
- Thời gian thử: 7 ngày
- Tổng số bài dự kiến: 21
- Chủ đề: AI Automation, doanh nghiệp nhỏ, spa, marketing thực chiến

## Điều kiện trước khi chạy

1. Chuyển Instagram từ Personal sang Creator.
2. Bật tài khoản công khai trong thời gian thử nghiệm.
3. Giữ bật Accounts Center và Sharing across profiles.
4. Kết nối Instagram với Make bằng OAuth chính thức.
5. Không nhập mật khẩu, cookie, OTP hoặc session token vào Make, GitHub, Google Sheets hay notebook.

## Ba bài kiểm thử ban đầu

1. Ảnh đơn 4:5, không nhạc.
2. Carousel hai ảnh, không nhạc.
3. Reel ngắn với original audio hoặc nhạc royalty-free có quyền sử dụng.

Chỉ bật lịch 3 bài/ngày nếu cả ba bài đều xuất hiện đúng trên Instagram, Facebook và Threads.

## Chính sách đồng bộ

Mục tiêu nghiệp vụ là: giữ cả ba hoặc xóa cả ba.

Giới hạn kỹ thuật:

- Cross-post từ Instagram sang Facebook Profile và Threads không phải giao dịch nguyên tử.
- API chính thức không bảo đảm có thể tự xóa đồng thời bài đã cross-post trên cả ba nền tảng.
- Không sử dụng browser automation, cookie hoặc session token để cưỡng ép xóa.

Vì vậy flow thực tế dùng fail-closed:

1. Preflight kiểm tra kết nối và trạng thái tài khoản.
2. Tạo nội dung và media.
3. Đăng Instagram.
4. Chờ 90–180 giây.
5. Xác minh Instagram, Facebook và Threads.
6. Nếu thiếu bất kỳ nền tảng nào:
   - tạm dừng scenario;
   - không đăng bài kế tiếp;
   - gửi cảnh báo Telegram;
   - ghi trạng thái `partial_sync` vào Google Sheets;
   - cung cấp link để người dùng xóa thủ công toàn bộ.

## Âm nhạc

- Không tự tải, ghép hoặc đăng các bài của Đen Vâu dưới dạng original audio.
- Nhạc có bản quyền chỉ được chọn thủ công trong ứng dụng Meta khi thư viện hiển thị quyền sử dụng.
- Full-auto mặc định dùng ảnh không nhạc hoặc Reel có original audio/royalty-free audio hợp lệ.
- Nếu muốn dùng nhạc Đen Vâu, chuyển bài đó sang chế độ bán tự động: AI chuẩn bị caption và media, người dùng mở app chọn bài nhạc rồi đăng.

## Nội dung theo giờ

### 08:00

- Kiến thức nền tảng AI
- Checklist
- Sai lầm thường gặp

### 13:00

- Workflow cụ thể
- Case dành cho spa
- Quy trình lead, CRM, chatbot và chăm sóc khách

### 18:00

- Góc nhìn cá nhân
- Bài học triển khai
- CTA bình luận hoặc nhắn tin

## Chỉ số theo dõi

Mỗi bài lưu:

- thời gian đăng
- chủ đề
- định dạng
- hook
- CTA
- link Instagram
- link Facebook
- link Threads
- lượt tiếp cận
- lượt thích
- bình luận
- lượt lưu
- lượt chia sẻ
- tin nhắn hoặc lead phát sinh
- trạng thái đồng bộ

## Đánh giá sau 7 ngày

Tạm dừng lịch và review:

- khung giờ tốt nhất
- content pillar tốt nhất
- định dạng tốt nhất
- tỷ lệ đồng bộ thành công
- chi phí AI/Make
- số lead thực tế
- có nên giữ 3 bài/ngày, giảm còn 1–2 bài/ngày hay đổi chiến lược
