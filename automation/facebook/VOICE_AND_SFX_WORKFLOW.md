# Voice & Sound Effects Workflow — QuangQuy AI Reels

## Mục tiêu

Dùng giọng thật của Nguyễn Quang Quý làm voice-over chính cho video người que chia sẻ kinh nghiệm, kỹ năng, AI Automation và Marketing.

## Nguyên tắc giọng nói

- Ưu tiên giọng thật thu trực tiếp để giữ độ tin cậy và cá tính.
- Có thể tạo voice profile/voice clone chỉ từ mẫu giọng do chính Nguyễn Quang Quý cung cấp và đồng ý sử dụng.
- Không dùng giọng của người khác hoặc giả danh người khác.
- Không lưu file giọng gốc trong GitHub công khai.
- File mẫu giọng lưu trong Google Drive riêng tư: `QuangQuy AI Workspace/03_Assets/Voice/`.

## Mẫu giọng cần thu

- Tối thiểu: 3–5 phút để thử nghiệm.
- Khuyến nghị: 10–15 phút để giọng ổn định hơn.
- Phòng yên tĩnh, không nhạc nền, không tiếng quạt.
- Điện thoại cách miệng khoảng 15–20 cm.
- Đọc tự nhiên, có câu ngắn, câu dài, câu hỏi và câu nhấn mạnh.
- Xuất WAV hoặc MP3 chất lượng cao.

## Nguồn hiệu ứng âm thanh ưu tiên

1. TiếngĐộng.com cho SFX mang ngữ cảnh Việt Nam: câu nói viral, meme, bất ngờ, thất bại, game, chuyển cảnh, tiếng cười.
2. Mixkit Sound Effects.
3. Pixabay Sound Effects.
4. Meta Sound Collection cho nội dung trong hệ sinh thái Meta.
5. Freesound chỉ dùng file có giấy phép phù hợp; tránh giấy phép NonCommercial nếu mục tiêu là kiếm tiền hoặc bán dịch vụ.

Không tải âm thanh bằng cách rip từ video YouTube hoặc nguồn không rõ giấy phép.

### Quy tắc riêng với TiếngĐộng.com

- Không mặc định mọi file đều an toàn cho thương mại hoặc kiếm tiền.
- Trước khi dùng phải lưu: tên âm thanh, URL nguồn, ngày kiểm tra, ghi chú nguồn gốc và credit nếu cần.
- Ưu tiên SFX ngắn, không chứa đoạn nhạc hoặc lời thoại có bản quyền rõ ràng.
- Với câu nói viral, meme có giọng người nổi tiếng, phim, gameshow hoặc chương trình truyền hình: không tự động đăng nếu chưa xác minh quyền sử dụng.
- Nếu nguồn không rõ hoặc có nguy cơ khiếu nại, thay bằng SFX tương đương từ Mixkit, Pixabay hoặc Meta Sound Collection.
- Có thể ghi nguồn theo gợi ý của website khi phù hợp.

## Bộ hiệu ứng cuốn hút

- `whoosh`: chuyển cảnh, kéo sự chú ý.
- `pop`: chữ hoặc icon xuất hiện.
- `click`: thao tác phần mềm, nút bấm.
- `typing`: mô phỏng nhập prompt hoặc quy trình.
- `notification`: lead hoặc tin nhắn mới.
- `error/buzzer`: sai lầm, cảnh báo.
- `success/ding`: kết quả, hoàn thành workflow.
- `cash/register`: chỉ dùng nhẹ khi nói về tiết kiệm chi phí; không ám chỉ doanh thu bảo đảm.
- `riser`: tăng nhịp trước phần giải pháp.
- `impact`: nhấn mạnh hook hoặc kết luận.
- `vietnamese_meme_sfx`: chỉ dùng khi đã xác minh nguồn và quyền sử dụng.

## Quy tắc mix âm thanh

- Voice-over là lớp âm thanh chính.
- Nhạc nền thấp hơn voice-over rõ rệt.
- Hiệu ứng chỉ xuất hiện khi có hành động hình ảnh tương ứng.
- Không dùng hiệu ứng liên tục gây mệt.
- Hook 0–2 giây có thể dùng một impact hoặc whoosh ngắn.
- Mỗi cảnh tối đa 1–2 hiệu ứng chính.
- Giảm âm nhạc khi voice-over bắt đầu (ducking).
- Kiểm tra bằng loa điện thoại trước khi đăng.

## Workflow

```text
AI tạo kịch bản
→ tách voice-over thành từng câu
→ tạo giọng Nguyễn Quang Quý từ voice profile hoặc dùng file thu thật
→ chọn hiệu ứng theo hành động từng cảnh
→ kiểm tra nguồn và quyền sử dụng SFX
→ ghép voice + SFX + nhạc nền an toàn
→ chuẩn hóa âm lượng
→ tạo phụ đề
→ xuất MP4 9:16
→ kiểm tra thủ công 3 video đầu
→ đăng thử Instagram → Facebook cá nhân
```

## Cơ chế fail-closed

Không đăng tự động nếu:

- chưa có sự đồng ý sử dụng voice profile;
- file giọng lỗi hoặc phát âm sai tên thương hiệu;
- hiệu ứng quá lớn che giọng;
- không xác minh được giấy phép hoặc nguồn SFX;
- SFX chứa lời thoại/nghệ sĩ/nội dung có nguy cơ bản quyền;
- video không có phụ đề;
- video không xuất đúng 9:16.
