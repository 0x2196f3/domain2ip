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


def tcp_ping(domain):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 1 second timeout
        result = sock.connect_ex((domain, 80))  # try to connect to port 80
        if result == 0:
            print(f"{domain}: UP")
        else:
            print(f"{domain}: DOWN")
    except socket.gaierror:
        print(f"{domain}: DNS resolution failed")
    except socket.error:
        print(f"{domain}: Connection failed")


if __name__ == "__main__":
    for domain in domains_on_cloudflare:
        tcp_ping(domain)
