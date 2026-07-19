# Facebook-first Funnel — QuangQuy AI

## Mục tiêu

Tập trung toàn bộ thử nghiệm tuần đầu vào Facebook:

- Fanpage là nơi đăng nội dung tự động.
- Messenger là nơi thu lead và tư vấn.
- Google Sheets lưu lead và trạng thái xử lý.
- Telegram báo lead nóng và lỗi hệ thống.
- Instagram và Threads không tham gia luồng hiện tại.

## Tài khoản

- Fanpage mục tiêu: `https://www.facebook.com/profile.php?id=61578883028862`
- Page ID dự kiến: `61578883028862`
- Facebook cá nhân hỗ trợ thương hiệu: `https://www.facebook.com/quangquy88/`

Chỉ bật Auto mode nếu Fanpage mục tiêu xuất hiện trong danh sách Page của module Facebook Pages trên Make.

## Scenario A — Content Engine

```text
Scheduler: 08:00, 13:00, 18:00
→ Google Sheets: lấy 30 chủ đề gần nhất
→ OpenAI: tạo JSON caption + image_prompt + topic_key + CTA keyword
→ JSON Parse
→ OpenAI/Gemini: tạo ảnh 4:5
→ HTTP Get a file nếu ảnh trả URL
→ Facebook Pages: Create a Post with Photos
→ Google Sheets: lưu post_id, post_url, chủ đề, CTA
→ Telegram: báo kết quả
```

### Nội dung theo giờ

- 08:00: kiến thức AI dễ hiểu, checklist, lỗi thường gặp.
- 13:00: workflow dành cho doanh nghiệp nhỏ hoặc spa.
- 18:00: góc nhìn cá nhân, case triển khai và CTA nhắn tin.

## Scenario B — Messenger Lead Funnel

### Điểm vào

- Người dùng nhắn Fanpage.
- Người dùng bình luận từ khóa dưới bài.
- Người dùng bấm nút CTA trên Page hoặc quảng cáo.

### Từ khóa

- `AI`
- `SPA`
- `WORKFLOW`
- `TƯ VẤN`

### Kịch bản hỏi lead

1. Anh/chị đang kinh doanh lĩnh vực gì?
2. Quy trình nào đang tốn thời gian nhất?
3. Hiện có bao nhiêu người xử lý marketing/chăm sóc khách?
4. Anh/chị muốn tự triển khai hay cần Quang Quý setup?
5. Xin số điện thoại để Quang Quý liên hệ tư vấn.

### Phân loại

- `new_lead`: mới bắt đầu trò chuyện.
- `qualified`: đã có lĩnh vực + nhu cầu.
- `hot_lead`: đã cung cấp số điện thoại hoặc yêu cầu báo giá.
- `follow_up`: cần nhắc lại.
- `not_fit`: không có nhu cầu phù hợp.

### Hành động

```text
Messenger nhận tin
→ xác định từ khóa/ý định
→ AI tạo câu trả lời theo kịch bản
→ lưu tên, PSID, lĩnh vực và nhu cầu vào Google Sheets
→ nếu có số điện thoại hoặc yêu cầu tư vấn: gửi Telegram cho Nguyễn Quang Quý
→ gắn trạng thái lead
```

## Nguyên tắc tư vấn

- Không tự cam kết doanh thu.
- Không báo giá khi chưa có dữ liệu tối thiểu.
- Không gửi tin nhắn chủ động khi khách chưa bắt đầu cuộc trò chuyện.
- Khi câu hỏi liên quan pháp lý, tài chính, khiếu nại hoặc giá trị hợp đồng lớn: chuyển cho người thật.
- AI chỉ thu thập thông tin, giải thích dịch vụ và đặt lịch sơ bộ.

## Chống spam nội dung

- Không lặp `topic_key` trong 14 ngày.
- Không lặp hook trong 7 ngày.
- Không dùng cùng CTA quá 2 lần liên tiếp.
- Tối đa 3 bài/ngày trong thử nghiệm 7 ngày.

## Điều kiện bật tự động

1. Ba bài `Run once` đăng đúng Fanpage.
2. Ảnh và caption hiển thị đúng.
3. Google Sheets ghi được post URL.
4. Messenger instant reply hoạt động.
5. Một cuộc trò chuyện thử được lưu thành lead.
6. Telegram nhận được cảnh báo lead nóng.

## Đánh giá sau 7 ngày

- Số bài đăng thành công.
- Reach và engagement theo khung giờ.
- Số bình luận từ khóa.
- Số cuộc trò chuyện Messenger.
- Số lead đủ điều kiện.
- Số số điện thoại thu được.
- Số lịch tư vấn.
- Chi phí Make và AI trên mỗi lead.
