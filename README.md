# craw_subdomain

### Download 

```
apt install -y git nmap 
cd /opt
git clone https://github.com/hungviet99/craw_subdomain.git
apt install mysql-server
```

Thiết lập secure cho mysql 

```
mysql_secure_installation
```

Sau đó, hãy đăng nhập vào mysql và thực hiện tạo csdl để lưu domain

### Tạo cơ sở dữ liệu 

Đăng nhập vào cơ sở dữ liệu và thực hiện tạo csdl như sau: 

```
creat database craw_domain;
```
```
use craw_domain;
```
```
CREATE TABLE `subdomain` (
  domain varchar(255) NULL,
  subdomain json DEFAULT NULL
)
```
```
grant all privileges on craw_domain.* to "subuser"@"localhost" identified by 'Subdomain2020@';
```
```
FLUSH PRIVILEGES;
exit;
```
### Tạo tài khoản Virustotal 

Truy cập virustotal và kích vào tạo tài khoản. 

![](./image/vt1.png)

Sau khi đã có tài khoản đăng nhập virustotal, truy cập vào API key để lấy key API. 

![](./image/vt2.png)

![](./image/vt3.png)

Chỉnh sửa file config. 

```
sed -i 's/api_vt =/api_vt= "17cd6d28652ea7dd99a0ea9abbfe07c68ecf8ath01e950fgdf2365af80b05967"/' /opt/craw_subdomain/config.py
```
>Lưu ý: Thay `17cd6d28652ea7dd99a0ea9abbfe07c68ecf8ath01e950fgdf2365af80b05967` bầng api của bạn.

### Chạy chương trình 

- Cài đặt môi trường ảo python

```
cd /opt/craw_subdomain
pip3 install virtualenv
virtualenv env -p python3.6
source env/bin/activate
```

- Cài đặt các thư viện 

```
pip3 install -r requirements.txt
```

```
python3 main.py
```

