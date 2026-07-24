# Thiết lập Make Scenario — Tạo bài, tạo ảnh và đăng Fanpage

## Tài khoản Facebook đích

```text
URL: https://www.facebook.com/profile.php?id=61578883028862
ID: 61578883028862
Trạng thái: chưa bật tự động đăng
```

Trước khi bật scenario, mở module `Facebook Pages` trong Make và kiểm tra tài khoản này có xuất hiện trong danh sách **Page** hay không.

- Nếu xuất hiện bằng đúng tên và ID, chọn từ danh sách; không nhập ID thủ công.
- Nếu không xuất hiện, đây không phải đối tượng Page mà kết nối Facebook Pages được quyền đăng. Khi đó dừng luồng và không dùng cookie, Selenium hoặc token không chính thức.
- Chỉ đổi `auto_publish_enabled` thành `true` sau khi `Run once` đăng thành công một bài thử và người dùng xác nhận đúng nơi nhận.

## Luồng khuyến nghị

```text
1. Scheduler
2. Google Sheets — Search Rows
3. OpenAI — Simple text prompt hoặc Generate a response
4. JSON — Parse JSON
5. OpenAI — Generate an image
6. HTTP — Get a file (chỉ khi module ảnh trả URL)
7. Facebook Pages — Create a Post with Photos
8. Google Sheets — Add/Update a Row
9. Telegram Bot — Send a Message
```

## 1. Scheduler

- Chạy thử: thủ công bằng `Run once`.
- Khi ổn định: mỗi ngày 19:00, múi giờ `Asia/Ho_Chi_Minh`.
- Không dùng lịch 15 phút cho luồng đăng bài.

## 2. Google Sheets

Tạo Sheet tên `Facebook_Content_Queue` với các cột:

```text
id,status,planned_date,category,topic,caption,image_prompt,post_url,error
```

Giá trị `status`:

- `idea`
- `ready`
- `approved`
- `posted`
- `failed`

Ở chế độ Review, chỉ đăng dòng có `status = approved`.

## 3. OpenAI tạo nội dung

Dùng prompt tại:

```text
automation/facebook/prompts/content_and_image_prompt.md
```

Yêu cầu đầu ra là JSON. Không map toàn bộ bundle sang Facebook.

## 4. Parse JSON

Schema tối thiểu:

```json
{
  "topic": "string",
  "category": "string",
  "caption": "string",
  "image_prompt": "string",
  "alt_text": "string"
}
```

Sau khi Parse JSON:

- `caption` → Facebook Post caption.
- `image_prompt` → module tạo ảnh.
- `topic` và `category` → lưu lại Google Sheets.

## 5. Tạo ảnh

Khuyến nghị:

- Tỷ lệ: `4:5`.
- Kích thước mục tiêu: `1080 × 1350`.
- Phong cách: chuyên nghiệp, hiện đại, đen–vàng–trắng.
- Không tạo quá nhiều chữ trong ảnh.
- Không dùng logo hoặc nhãn hiệu của bên thứ ba.

Nếu module trả URL ảnh, thêm `HTTP → Get a file` rồi map file đó sang Facebook.

## 6. Đăng Facebook

Chọn:

```text
Facebook Pages → Create a Post with Photos
```

Map:

```text
Page: chọn đúng Fanpage từ danh sách
Post caption: JSON Parse → caption
Photo/File: OpenAI image hoặc HTTP → Data
```

Không nhập Page ID thủ công nếu Make đã hiển thị được danh sách Fanpage.

## 7. Lưu kết quả

Sau khi đăng thành công:

- `status = posted`
- `post_url = link bài đăng`
- lưu thời gian đăng
- lưu chủ đề và caption

Nếu lỗi:

- `status = failed`
- lưu nguyên văn thông báo lỗi vào cột `error`
- gửi Telegram cho người dùng

## 8. Telegram duyệt bài

Review mode:

```text
AI tạo caption + ảnh
→ Telegram gửi bản xem trước
→ người dùng đổi status thành approved
→ scenario đăng bài chạy sau đó
```

Có thể nâng cấp thành nút `Đăng / Sửa / Bỏ qua` sau khi luồng cơ bản hoạt động ổn định.

## 9. Chống lặp

Trước khi tạo bài, lấy 20 dòng gần nhất có `status = posted`, rồi đưa danh sách `topic` vào prompt với yêu cầu không lặp lại.

## 10. Nhánh video/Reel tùy chọn

```text
OpenAI tạo kịch bản
→ công cụ tạo video xuất MP4 9:16
→ Facebook Pages → Publish a Reel
```

Chỉ xây nhánh Reel sau khi luồng ảnh hoạt động ổn định.
