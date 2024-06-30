import re

from lxml import html

import url_cache

base_url = "https://monitor.gacjie.cn/page/"


def get_url(cdn_name, ip) -> str:
    return base_url + cdn_name + "/" + ip + ".html"


def get_ips(url: str) -> list[str]:
    content = url_cache.make_request(url)

    tree = html.fromstring(content)

    element = tree.xpath("/html/body/div[3]/div/div/div/div[2]/table/tbody")[0]

    tr_elements = element.xpath("tr")

    ips = []
    for tr in tr_elements:
        td_elements = tr.xpath("td")
        if len(td_elements) >= 2:
            second_td = td_elements[1]
            # do something with the second <td> element
            # print(second_td.text)
            ips.append(second_td.text)

    return ips


if __name__ == "__main__":
    print(get_ips("https://monitor.gacjie.cn/page/cloudflare/ipv6.html"))
