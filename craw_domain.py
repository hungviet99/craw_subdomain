import nmap3 
from pysecuritytrails import SecurityTrails, SecurityTrailsError
import socket
from virus_total_apis import PublicApi as VirusTotalPublicApi
import config
import sys

domain = input("Nhap vao domain: ")
nmap = nmap3.Nmap()
vt = VirusTotalPublicApi(config.api_vt)

sub_nmap = nmap.nmap_dns_brute_script(domain)

st = SecurityTrails(config.api_st)
sub_st = st.domain_subdomains(domain)
sudomain_st = sub_st['subdomains']
sub_vt = vt.get_domain_report(domaini)

subdomain_vt = sub_vt['results']['subdomains']


def nmap_scan(sub_nmap):
    list_nmap = []
    for dist in sub_nmap:
        apsub = dist['hostname']
        list_nmap.append(apsub)
    return list_nmap

def st_and_vt_scan(sudomain_st, list_nmap, subdomain_vt):

    list_st = []
    for element in sudomain_st:
        subdm = element+'.'+domain
        list_st.append(subdm)

    for element in list_nmap:
        if element not in list_st:
            list_st.append(element)

    for element in subdomain_vt:
        if element not in list_st:
            list_st.append(element)

    return list_st


# Kiam tra va loai bo cac domain cũ
def check_subdomain(list_st):
    sub_all = {}
    for x in list_st:
        try:
            addr1 = socket.gethostbyname(x)
            sub_all[x] = addr1
        except Exception as ex:
            resul = str(ex)
    return sub_all

def main():
    list_nmap = nmap_scan(sub_nmap)
    list_st = st_and_vt_scan(sudomain_st, list_nmap, subdomain_vt)
    sub_all = check_subdomain(list_st)
    return sub_all
