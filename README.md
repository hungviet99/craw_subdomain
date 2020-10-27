# craw_subdomain

### Download 

```
apt install -y git wget nmap 
cd
git clone https://github.com/hungviet99/craw_subdomain.git
```

```
cd craw_subdomain
pip3 install -r requirements.txt
```

### Chạy chương trình 

```
python3 main.py
```

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
  subdomain json DEFAULT NULL,
)
```