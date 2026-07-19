# Kiến trúc Cloud-first cho QuangQuy AI

```text
Điện thoại / trình duyệt
        |
        +--> ChatGPT: chiến lược, giao việc, review GitHub
        +--> Google Colab: chạy AI builder, test và tạo commit
        +--> Google Drive: inbox, assets, exports, backups
        |
        v
GitHub repository (nguồn code chính)
        |
        +--> Pull Request: kiểm tra và duyệt
        +--> Vercel/Netlify/GitHub Pages: deploy preview và production
        +--> Make/n8n: lịch chạy, webhook, Telegram, Google Sheets
```

## Nguyên tắc dữ liệu

- **GitHub:** chỉ code, cấu hình không nhạy cảm và tài liệu kỹ thuật.
- **Google Drive:** ảnh/video, tài liệu kinh doanh, file đầu vào và bản sao.
- **Colab:** môi trường tạm; khi phiên bị reset, code vẫn còn trên GitHub và dữ liệu vẫn còn trên Drive.
- **Điện thoại:** điều khiển, duyệt và kiểm tra; không phải nơi lưu duy nhất.

## Cơ chế phối hợp AI

1. Owner ghi tác vụ trong `tasks/INBOX.md` hoặc nhắn ChatGPT.
2. ChatGPT chuẩn hóa yêu cầu, chỉ định file và rủi ro.
3. Colab Control Center gọi Gemini để tạo kế hoạch JSON.
4. Thay đổi rủi ro thấp có thể được áp dụng; thay đổi khác phải duyệt.
5. Hệ thống chạy build/test và tạo branch.
6. Code được push lên GitHub, sau đó ChatGPT review pull request.
7. Sau khi owner duyệt, merge và deploy.
