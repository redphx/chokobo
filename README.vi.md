# Chokobo
Tiện ích bán tự động chuyển đổi sách `epub` sang `kepub` trên Dropbox cho máy đọc sách Kobo (bởi vậy nên có tên là `Chokobo`).  

Gọi là "bán tự động" vì sau khi upload sách lên Dropbox bạn phải tự nhấn chạy tiện ích để bắt đầu quá trình chuyển đổi, chứ không thể làm tự động hoàn toàn.

## ✨ Tính năng
Sử dụng GitHub Action để chuyển đổi các file sách `epub` trên Dropbox thành chuẩn `kepub`, sau đó upload ngược lại lên Dropbox.  

**Ưu điểm so với các cách làm khác:**  
- Không cần sử dụng Calibre rườm rà
- Không cần kết nối Kobo với máy tính để chép sách
- Sách được lưu trên Dropbox nên có thể tải về trên Kobo lúc nào cũng được
- Có thể kích hoạt trên mọi thiết bị: máy tính, điện thoại...
- Hỗ trợ convert nhiều sách cùng lúc (tiện hơn ([send.djazz.se](https://send.djazz.se/))
- Riêng tư 100%, không như sendtokindle :v

**Nhược điểm:**  
- Việc cài đặt và cấu hình gồm nhiều bước, có thể hơi ngợp nếu bạn không rành về công nghệ. Mình sẽ cố gắng hướng dẫn ngắn gọn và dễ hiểu nhất có thể.
- Tổng thời gian chạy GitHub Action miễn phí mỗi tháng là 2000 phút
  - Mỗi lần chạy tool chỉ mất khoảng 1 phút (hoặc nhiều hơn nếu có nhiều sách), nên bạn không phải lo việc vượt giới hạn, trừ khi bạn chép *rất-rất-nhiều* sách
  - Convert nhiều sách cùng một lúc tiết kiệm thời gian hơn là chạy riêng từng lần cho mỗi sách
  - [Vào đây](../..//actions/metrics/usage) để xem thống kê số phút đã sử dụng

## I. Chuẩn bị

### Tài khoản
Tiện ích yêu cầu tài khoản của GitHub và Dropbox. Nếu chưa có tài khoản, bạn có thể dùng các link sau để tạo miễn phí:  
- [Tạo tài khoản GitHub](https://github.com/signup)
- [Tạo tài khoản Dropbox](https://www.dropbox.com/referrals/AAB_nRkqghEm94wvV6A8TNxakMs3Z6qMh3U) (link giới thiệu, sau khi tạo xong + cài đặt app trên pc/mobile mỗi tài khoản sẽ được tặng thêm 500MB miễn phí)

### Thiết bị
Nếu Kobo bạn đang dùng là Kobo Forma, Sage, Elipsa, Elipsa 2E hoặc Libra Colour thì không cần chuẩn bị bước này, vì máy đã có sẵn tính năng Dropbox.

Với các Kobo khác bạn phải cài đặt NickelMenu để có thể sử dụng tính năng Dropbox:
- [Hướng dẫn cài đặt NickelMenu](https://sachxy.com/nickelmenu)
- [Hướng dẫn kích hoạt Dropbox bằng NickelMenu](https://sachxy.com/nickelmenu-cloud)

## II. Cài đặt và cấu hình

> [!IMPORTANT]
> Trong hướng dẫn sẽ có nhắc đến từ khóa `Token` hoặc `AccessToken`. Hãy xem nó như mật khẩu, tuyệt đối không để lộ hoặc chia sẻ với bất kỳ ai. Nó được dùng để truy cập dữ liệu trong tài khoản của bạn mà không cần phải biết mật khẩu tài khoản.

1. Chắc chắn là Kobo đã liên kết tài khoản Dropbox thành công
2. Kết nối Kobo với máy tính
3. Mở file `.kobo/Kobo/Kobo eReader.conf` bằng Notepad (Windows) hoặc TextEdit (Mac)  
    > Nếu bạn dùng macOS và không thấy thư mục `.kobo`, nhấn tổ hợp phím `Cmd + Shift + .` để hiện thư mục ẩn trong Finder
4. Tìm mục `[DropboxSettings]`, sau đó copy giá trị của `AccessToken` và để tạm ở đâu đó (sẽ cần ở bước 8). Đóng file.
    <br><br>
    > ```ini
    > [DropboxSettings]
    > AccessToken=<COPY GIÁ TRỊ NÀY>
    > UserGuideId=...
    > Username=...
    > ```
5. Đăng nhập GitHub và [nhấn vào link này](https://github.com/new?template_name=chokobo&template_owner=redphx) để sao chép tool về tài khoản cá nhân
6. Thực hiện các bước như hướng dẫn trong hình. Lưu ý mục **Configuration** phải chọn **PRIVATE** để đảm bảo riêng tư, tránh người ngoài dòm ngó.
    <br><div align="center"><img width="789" height="485" alt="image" src="https://github.com/user-attachments/assets/75382660-bef4-4b0a-a1e2-5ed64c23b0df" /></div>
7. Trong trang của repo vừa tạo, vào `Settings > Security > Secrets and variables > Actions`, nhấn vào nút `New repository secret`
    <br><br><div align="center"><img width="796" height="570" alt="image" src="https://github.com/user-attachments/assets/d66d9899-59f5-4bc0-b92d-07ca2628ff06" /></div>
8. Nhập các giá trị sau và nhấn `Add secret` để lưu:
    - **Name**: `DROPBOX_ACCESS_TOKEN`
    - **Secret**: giá trị của `AccessToken` ở bước 4  
    <br><div align="center"><img width="792" height="426" alt="image" src="https://github.com/user-attachments/assets/686e7798-e003-4a1c-a739-3515b57d7d1c" /></div>

Sau khi thực hiện xong, ngắt kết nối Kobo và máy tính.

## III. Convert sách

1. Tải sách `epub` lên Dropbox, trong thư mục `Apps/Rakuten Kobo` (không để sách vào thư mục con của thư mục này):
    <br><div align="center"><img width="634" height="251" alt="image" src="https://github.com/user-attachments/assets/7caa7f8a-0b59-46da-9cbb-79fed62c5bb1" /></div>

2. Để chạy tool thực hiện việc convert sách, trong GitHub, hãy vào `Actions > Convert books`, nhấn nút `Run workflow`, và nhấn tiếp nút `Run workflow` màu xanh một lần nữa ([link trực tiếp](../../actions/workflows/convert.yml))
    <br><div align="center"><img width="812" height="615" alt="image" src="https://github.com/user-attachments/assets/8e70062a-7d15-40a6-ba34-1ee6624b24a6" /></div>

3. Tải lại trang để xem trạng thái. Sau khi tool đã chạy thành công, Dropbox của bạn sẽ có thêm thư mục `converted` (chứa sách đã convert) và `original` (chứa file sách gốc)
    <br><div align="center"><img width="634" height="251" alt="image" src="https://github.com/user-attachments/assets/fc2306e6-f4eb-43cd-94df-4fda03c93f2e" /></div>

4. Mở tính năng Dropbox trên Kobo và tải file kepub về
5. Xong

**Mẹo:** bạn có thể lưu (bookmark) [địa chỉ trang web](../../actions/workflows/convert.yml) ở bước 2 để tiện cho việc chạy tool sau này.

## IV. Kích hoạt tool bằng tính năng Shortcuts trên iOS  
*(...viết sau...)*
