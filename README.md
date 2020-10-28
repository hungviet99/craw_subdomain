# craw_subdomain

### Download 

```
apt install -y git nmap 
cd
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
### Chạy chương trình 
- Cài đặt môi trường ảo python

```
cd /root/craw_subdomain
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

