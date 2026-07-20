# Caption Guard — Instagram → Facebook Profile

## Vấn đề đã xác nhận

Bài thử nghiệm được đăng đồng thời lên Instagram `quy28_01`, Facebook cá nhân `quangquy88` và Threads. Khi caption dài, nội dung chữ bị mất trên các kênh sau khi đăng.

## Nguyên tắc vận hành

- Instagram và Facebook là hai kênh chính.
- Threads tắt mặc định trong workflow tự động.
- Không dùng một caption dài chung cho cả Instagram, Facebook và Threads.
- Không đăng nếu caption sau xử lý bị rỗng.

## Giới hạn nội bộ

Đây là giới hạn an toàn của workflow, không phải tuyên bố giới hạn tối đa của nền tảng:

- Reel Instagram → Facebook: tối đa 700 ký tự.
- Bài ảnh Instagram → Facebook: tối đa 900 ký tự.
- Khi bật Threads thủ công: tối đa 450 ký tự, đã tính hashtag và emoji.
- Hashtag: 3–5 hashtag liên quan.
- CTA: một hành động duy nhất.

## Cơ chế xử lý caption

1. AI tạo bản dài để lưu trữ.
2. AI tạo bản xuất bản ngắn theo định dạng.
3. Đếm ký tự Unicode sau khi thêm hashtag.
4. Nếu vượt giới hạn, tóm tắt lại; không cắt giữa câu.
5. Nếu caption rỗng, chỉ có hashtag hoặc lỗi mã hóa: dừng đăng và gửi cảnh báo.
6. Sau khi đăng, kiểm tra caption Instagram còn tồn tại.
7. Kiểm tra bài Facebook đã xuất hiện và có nội dung chữ.
8. Thiếu caption ở một trong hai kênh: tạm dừng scenario, không đăng bài kế tiếp.

## Nội dung dài

Nội dung chi tiết chuyển sang một trong các dạng:

- lời thoại và phụ đề trong Reel;
- carousel nhiều trang;
- bài Facebook riêng được biên tập thủ công;
- tài liệu/landing page, caption chỉ dùng hook và CTA.

## Mẫu caption Reel

```text
Ủa, rồi workflow đâu? 😅

Làm thủ công kiểu này thì Tết chưa xong. Khách nhắn chậm một chút là lead bay màu.

Một workflow đơn giản có thể giúp:
Khách nhắn → AI hỏi nhu cầu → lưu thông tin → báo người phụ trách.

Bấm một cái, đỡ cày cả ngày.
AI làm phần cực, mình làm phần có tiền.

Bình luận WORKFLOW để Quý gửi sơ đồ mẫu.

#AIAutomation #Workflow #NguyenQuangQuy
```
