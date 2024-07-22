import socket

domains_on_cloudflare = [
    "cloudflare.com",
    "4chan.org",
    "alejandracaiccedo.com",
    "csgo.com",
    "d-555.com",
    "digitalocean.com",
    "download.yunzhongzhuan.com",
    "fbi.gov",
    "gco.gov.qa",
    "glassdoor.com",
    "gov.se",
    "gov.ua",
    "gur.gov.ua",
    "hugedomains.com",
    "iakeys.com",
    "icook.hk",
    "icook.tw",
    "ip.sb",
    "ipaddress.my",
    "ipchicken.com",
    "ipget.net",
    "iplocation.io",
    "iplocation.net",
    "japan.com",
    "log.bpminecraft.com",
    "malaysia.com",
    "nc.gocada.co",
    "okcupid.com",
    "pcmag.com",
    "russia.com",
    "sean-now.com",
    "shopify.com",
    "singapore.com",
    "skk.moe",
    "time.cloudflare.com",
    "time.is",
    "udacity.com",
    "udemy.com",
    "visa.co.jp",
    "visa.com",
    "visa.com.hk",
    "visa.com.sg",
    "visa.com.tw",
    "visakorea.com",
    "whatismyip.com",
    "whatismyipaddress.com",
    "who.int",
    "whoer.net",
    "wto.org",
    "zsu.gov.ua",
]

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

def test_connection(domain):
    ip_address = get_ip_address(domain)
    if ip_address:
        try:
            socket.create_connection((ip_address, 80), timeout=5)
            return True
        except socket.error:
            return False
    else:
        return False



def tcp_ping(domain):
    ip_address = get_ip_address(domain)
    if ip_address:
        print(f"The IP address of {domain} is: {ip_address}")
        if test_connection(domain):
            print(f"Connection to {domain} successful!")
        else:
            print(f"Connection to {domain} failed.")
    else:
        print(f"Could not resolve the IP address for {domain}")


if __name__ == "__main__":
    tcp_ping("www.baidu.com")
    for domain in domains_on_cloudflare:
        tcp_ping(domain)
