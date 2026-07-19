# Facebook Automation — QuangQuy AI

## Chiến lược hiện tại: Facebook-first

Mục tiêu ưu tiên là xây phễu khách hàng trên Facebook, không phụ thuộc Instagram hoặc Threads.

- Fanpage mục tiêu: `61578883028862`
- Hồ sơ cá nhân hỗ trợ uy tín: `quangquy88`
- Kênh đăng nội dung: Facebook Page qua Make OAuth
- Kênh thu lead: Facebook Messenger
- Kho dữ liệu ban đầu: Google Sheets
- Cảnh báo lead nóng và lỗi: Telegram

## Hai luồng chính

### 1. Content Engine

Đăng tự động vào 08:00, 13:00 và 18:00 trong 7 ngày thử nghiệm.

```text
Scheduler
→ Google Sheets lấy lịch sử nội dung
→ OpenAI tạo caption + prompt ảnh
→ tạo ảnh 4:5
→ Facebook Pages đăng bài ảnh
→ lưu kết quả
→ Telegram báo trạng thái
```

### 2. Messenger Lead Funnel

```text
Khách nhắn Page hoặc bình luận CTA
→ tự động chào và xác định nhu cầu
→ AI hỏi từng bước
→ lưu lead vào Google Sheets
→ khi có số điện thoại/yêu cầu tư vấn: báo Nguyễn Quang Quý
```

## Tài liệu

- `FACEBOOK_FIRST_FUNNEL.md`: kiến trúc phễu đầy đủ.
- `MAKE_SCENARIO.md`: cấu hình scenario đăng bài.
- `prompts/content_and_image_prompt.md`: prompt tạo nội dung và ảnh.
- `prompts/messenger_lead_qualifier.md`: prompt tư vấn và phân loại lead.
- `facebook_leads_template.csv`: mẫu bảng lead.
- `config/content_plan.json`: cấu hình thương hiệu, lịch và phễu.
- `config/trial_state.json`: trạng thái thử nghiệm.
- `SECURITY.md`: quy tắc bảo mật.

## Điều kiện bật tự động

1. Fanpage xuất hiện trong module Facebook Pages của Make.
2. Ba lần `Run once` đăng đúng Page.
3. Messenger instant reply hoạt động.
4. Một cuộc trò chuyện thử được lưu vào Google Sheets.
5. Telegram nhận được cảnh báo lead nóng.

Không dùng mật khẩu, cookie, OTP hoặc session token. Chỉ dùng OAuth và API chính thức.
