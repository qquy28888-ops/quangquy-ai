# Make Daily Flow — Instagram → Facebook Profile → Threads

## Tài khoản đã kiểm chứng thủ công

- Instagram nguồn: `https://www.instagram.com/quy28_01/`
- Facebook nhận đồng bộ: `https://www.facebook.com/quangquy88/`
- Threads: tài khoản Threads liên kết với Instagram `quy28_01`
- Bài Facebook kiểm chứng: `https://www.facebook.com/quangquy88/posts/pfbid02R2fn889CA3j7mBiFVyXT6tazq9N91hBybLFMov3nwgyTNXhqC58ZpugW9HxyVXwPl`

Người dùng đã xác nhận rằng khi đăng thủ công từ ứng dụng Instagram, nội dung được chia sẻ sang Facebook và Threads.

## Blind spot bắt buộc kiểm tra

Việc đăng thủ công trong ứng dụng Instagram và việc đăng qua API có thể cho kết quả khác nhau. Trước khi bật lịch hằng ngày, phải kiểm tra một bài do Make tạo có tự đồng bộ sang cả Facebook và Threads hay không.

## Cổng tương thích tài khoản

Module chuẩn của Make là `Instagram for Business (Facebook login)`.

Trước khi xây scenario, kiểm tra loại tài khoản Instagram:

- Nếu là **Business** và Make kết nối được: có thể dùng module `Create a photo post`, `Create a carousel post` hoặc `Create a reel post`.
- Nếu là **Creator/Personal** và Make không kết nối được: không đổi loại tài khoản ngay. Việc chuyển sang Business có thể làm thay đổi đích cross-post sang Facebook Page thay vì Facebook Profile cá nhân. Khi đó cần dùng API chính thức qua HTTP hoặc giữ chế độ bán tự động.

Không dùng cookie, mật khẩu, Selenium hoặc trình duyệt giả lập để đăng.

## Scenario A — Ảnh hằng ngày

```text
1. Scheduler — mỗi ngày 19:00 Asia/Ho_Chi_Minh
2. Google Sheets — lấy 20 chủ đề gần nhất
3. OpenAI — tạo JSON caption + image_prompt
4. JSON — Parse JSON
5. OpenAI / Gemini — tạo ảnh 4:5
6. Lưu ảnh ở URL công khai phù hợp API
7. Instagram for Business — Create a photo post
8. Tools — Sleep 180 giây
9. Instagram — List posts, lấy permalink bài mới
10. Google Sheets — ghi trạng thái
11. Telegram — báo kết quả và yêu cầu kiểm tra Facebook/Threads
```

## Scenario B — Ảnh có nhạc dưới dạng Reel

Make không nên giả định có thể chọn bài hát trực tiếp từ thư viện nhạc Instagram. Phương án ổn định hơn:

```text
1. AI tạo ảnh 1080×1920 hoặc 1080×1350
2. Chọn audio do người dùng sở hữu quyền hoặc audio royalty-free
3. CloudConvert/FFmpeg/Shotstack ghép ảnh + audio thành MP4
4. Instagram for Business — Create a reel post
5. Accounts Center xử lý chia sẻ sang Facebook
6. Kiểm tra Threads
```

Không nhúng nhạc thương mại tải từ Internet nếu không có quyền sử dụng.

## Review mode khuyến nghị

Trong 7 ngày đầu:

```text
AI tạo caption + ảnh/video
→ Telegram gửi bản xem trước
→ người dùng bấm duyệt hoặc đổi status trong Google Sheets
→ scenario đăng bài
```

Chỉ chuyển sang Auto mode sau khi:

- Có ít nhất 3 bài ảnh do Make đăng và tự đồng bộ đúng.
- Có ít nhất 2 Reel do Make đăng và tự đồng bộ đúng.
- Không xuất hiện bài trùng, sai tài khoản hoặc lỗi bản quyền âm thanh.

## Test matrix

| Test | Nguồn đăng | Định dạng | Nhạc | Facebook | Threads | Kết quả |
|---|---|---|---|---|---|---|
| T1 | Instagram app | 1 ảnh | Có | Đã thành công | Đã thành công | Đã xác nhận |
| T2 | Make/API | 1 ảnh | Không | Chưa test | Chưa test | Bắt buộc |
| T3 | Make/API | Reel MP4 | Audio sở hữu quyền | Chưa test | Chưa test | Bắt buộc |
| T4 | Make/API | Carousel | Không | Chưa test | Chưa test | Tùy chọn |

## Dữ liệu cần lưu trong Google Sheets

```text
id
planned_at
status
category
topic
caption
image_prompt
media_type
media_url
instagram_permalink
facebook_verified
threads_verified
error
```

Giá trị `status`:

- `idea`
- `generated`
- `approved`
- `posted_instagram`
- `verified_all`
- `partial_crosspost`
- `failed`

## Điều kiện dừng tự động

Scenario phải dừng và gửi Telegram nếu:

- Tài khoản Instagram không đúng `quy28_01`.
- Bài Instagram đăng thành công nhưng không xuất hiện trên Facebook sau 15 phút.
- Threads không nhận bài sau 15 phút trong 2 lần liên tiếp.
- Caption hoặc ảnh chứa dữ liệu nhạy cảm.
- Có lỗi bản quyền audio.
- Có hơn 1 bài trong 24 giờ khi chưa được duyệt.
