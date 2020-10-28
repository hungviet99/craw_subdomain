import nmap3 
from pysecuritytrails import SecurityTrails, SecurityTrailsError
import socket
from virus_total_apis import PublicApi as VirusTotalPublicApi
import config
import sys

domain = input("Nhap vao domain: ")
# Connect to nmap api
nmap = nmap3.Nmap()
sub_nmap = nmap.nmap_dns_brute_script(domain)

#st = SecurityTrails(config.api_st)
#sub_st = st.domain_subdomains(domain)
#sudomain_st = sub_st['subdomains']

#Connect to virustotal API
vt = VirusTotalPublicApi(config.api_vt)
sub_vt = vt.get_domain_report(domain)
subdomain_vt = sub_vt['results']['subdomains']

def nmap_scan(sub_nmap):
    """Xử lý dữ liệu của nmap
    """
    list_nmap = []
    for dist in sub_nmap:
        apsub = dist['hostname']
        list_nmap.append(apsub)
    return list_nmap

def st_and_vt_scan(list_nmap, subdomain_vt):
    """Xử lý dữ liệu của securityTrails và Virustotal
    Xử lý các kết quả trùng nhau
    """
    list_st = []
#    for element in sudomain_st:
#        subdm = element+'.'+domain
#        list_st.append(subdm)
    for element in list_nmap:
        if element not in list_st:
            list_st.append(element)

    for element in subdomain_vt:
        if element not in list_st:
            list_st.append(element)
    return list_st

# Kiểm tra và loại bỏ các domain cũ
def check_subdomain(list_st):
    """Kiểm tra các bản ghi của domain, loại bỏ domain cũ
    """
    sub_all = {}
    for ele in list_st:
        try:
            addr1 = socket.gethostbyname(ele)
            sub_all[ele] = addr1
        except Exception as ex:
            resul = str(ex)
    return sub_all

def main():
    """Lấy dữ liệu về các domain, ghi vào sub_all
    """
    list_nmap = nmap_scan(sub_nmap)
    list_st_vt = st_and_vt_scan(list_nmap, subdomain_vt)
    sub_all = check_subdomain(list_st_vt)
    return sub_all
