# Kiến trúc Cloud-First cho QuangQuy AI

## Nguyên tắc

Hệ thống không phụ thuộc vào một máy tính cụ thể. Mọi thành phần quan trọng phải có thể truy cập từ điện thoại hoặc trình duyệt.

## Kiến trúc

```text
Điện thoại / Trình duyệt
        |
        v
ChatGPT / Gemini / Claude
        |
        v
GitHub — nguồn mã chuẩn
        |
        +--> Google Colab — chạy code, test, xử lý file
        |
        +--> Vercel / GitHub Pages — triển khai website
        |
        +--> Make / n8n — automation

Google Drive — tài liệu, ảnh, video, file đầu vào và file xuất
```

## Phân chia dữ liệu

### GitHub
Lưu:
- Code website.
- Script automation.
- Notebook không chứa secret.
- Prompt và tài liệu kỹ thuật.
- Cấu hình deploy.

Không lưu:
- `.env`.
- API key.
- Cookie.
- Mật khẩu.
- File cá nhân nhạy cảm.

### Google Drive
Lưu:
- Ảnh thương hiệu.
- Video.
- CV và tài liệu kinh doanh.
- File khách hàng.
- Bản sao lưu ZIP.
- File đầu ra từ Colab.

### Google Colab
Dùng để:
- Clone GitHub.
- Cài dependency.
- Chạy Python.
- Build và kiểm tra website.
- Xử lý ảnh/video.
- Tạo file rồi lưu vào Drive hoặc push lên GitHub.

Không dùng Colab làm nơi lưu duy nhất vì phiên có thể bị reset.

## Quy trình làm việc từ điện thoại

1. Giao yêu cầu qua ChatGPT.
2. ChatGPT cập nhật code hoặc tài liệu trên GitHub khi có quyền.
3. Khi cần chạy code, mở notebook Colab từ điện thoại.
4. Notebook clone repository và chạy tác vụ.
5. Kết quả lưu về Drive hoặc GitHub.
6. Vercel/GitHub Pages tự triển khai từ GitHub.

## Quy trình deploy

### Website tĩnh
GitHub → GitHub Pages.

### React, Vite, Next.js
GitHub → Vercel.

### Tác vụ Python
GitHub → Colab hoặc dịch vụ server khi cần chạy liên tục.

## Mức tự động hóa

### Tự động
- Tạo/sửa file an toàn.
- Chạy test và build.
- Tạo commit.
- Chuẩn bị deploy.
- Sinh nội dung và báo cáo.

### Cần duyệt
- Xóa file.
- Deploy production.
- Thay đổi domain/DNS.
- Phát sinh chi phí.
- Đăng bài hoặc gửi dữ liệu ra ngoài.
