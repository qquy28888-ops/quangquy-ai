# Chính sách âm thanh cho video AI người que

## Kết luận vận hành

Không tự động dùng nhạc NCS cho video AI người que khi chưa có xác nhận bằng văn bản từ NCS.

Lý do: chính sách sử dụng hiện hành của NCS có liệt kê `Training AI music models or other generative AI content` trong nhóm nội dung họ có quyền phản đối. Vì video người que được tạo bằng AI có thể bị xếp vào generative AI content, workflow phải xử lý theo hướng thận trọng.

## Thứ tự ưu tiên âm thanh

1. Meta Sound Collection cho nội dung đăng trên hệ sinh thái Meta.
2. Giọng đọc nguyên bản của Nguyễn Quang Quý + hiệu ứng âm thanh có giấy phép rõ ràng.
3. Nhạc royalty-free có điều khoản cho phép dùng thương mại và video tạo bằng AI.
4. NCS chỉ khi:
   - bài nhạc lấy từ trang chính thức NCS;
   - lưu bản chụp điều khoản tại thời điểm dùng;
   - có credit chính xác;
   - và tốt nhất có email xác nhận của NCS rằng video AI người que thuộc phạm vi được phép.

## Quy tắc bắt buộc

- Không tải nhạc từ video YouTube bằng công cụ rip audio.
- Không dùng bài của nghệ sĩ NCS nếu bài đó không phải bản phát hành chính thức của NCS.
- Không bỏ phần credit khi giấy phép yêu cầu.
- Không dùng cùng một bản nhạc cho quá nhiều video liên tiếp.
- Không để âm nhạc lấn át giọng nói; mục tiêu chính là chia sẻ kiến thức.
- Lưu `track_name`, `artist`, `source_url`, `license_checked_at`, `credit_text` trong Google Sheets.

## Mẫu credit

```text
Song: [Artist] - [Track] [NCS Release]
Music provided by NoCopyrightSounds
Free Download/Stream: [official NCS URL]
Watch: [official NCS/YouTube URL]
```

Không tự tạo credit bằng trí nhớ. Luôn sao chép từ trang chính thức của bài nhạc.

## Cơ chế fail-closed

Nếu không xác định được quyền sử dụng:

- không gắn bài nhạc đó;
- dùng giọng đọc + âm thanh an toàn;
- ghi trạng thái `audio_license_unverified`;
- không đăng tự động cho đến khi thay audio.
