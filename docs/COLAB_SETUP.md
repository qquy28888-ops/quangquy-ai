# Thiết lập Colab Secrets

Trong notebook Colab, mở biểu tượng **chìa khóa/Secrets** và tạo:

- `GEMINI_API_KEY`: lấy từ Google AI Studio.
- `GITHUB_TOKEN`: fine-grained token chỉ cấp quyền cho repository `quangquy-ai`.

Bật quyền notebook truy cập từng secret. Không ghi giá trị secret vào cell.

## Quy trình sử dụng

1. Mount Drive.
2. Clone hoặc pull repository.
3. Nhập tác vụ và file mục tiêu.
4. Tạo plan.
5. Đọc plan và mức rủi ro.
6. Bật `APPROVE = True` nếu chấp nhận.
7. Chạy test/build.
8. Commit trên branch `ai/...`.
9. Push và tạo pull request.
