import base64
import copy
import json
import random

import gacjie

gcore_domains = [
    "gcore.com",
    "speedtest.gcore.com",
    "hk2-speedtest.tools.gcore.com",
    "la2-speedtest.tools.gcore.com",
    "jp1-speedtest.tools.gcore.com",
    "kal-speedtest.tools.gcore.com",
    "kx-speedtest.tools.gcore.com",
    "lgs-speedtest.tools.gcore.com",
    "min4-speedtest.tools.gcore.com",
    "ny2-speedtest.tools.gcore.com",
    "pa5-speedtest.tools.gcore.com",
    "pl1-speedtest.tools.gcore.com",
    "sg1-speedtest.tools.gcore.com",
    "sp3-speedtest.tools.gcore.com",
    "sy4-speedtest.tools.gcore.com",
    "teg-speedtest.tools.gcore.com",
    "ww-speedtest.tools.gcore.com"
]


def replace_domain2ip(link: str, ipv4=True, ipv6=True) -> list[str]:
    # print("str = " + link)
    protol, base64_string = link.split("://")
    # print("protol = " + protol + " base64 = " + base64_string)
    try:
        padded_encoded_string = base64_string + "=" * ((4 - len(base64_string) % 4) % 4)
        decoded_bytes = base64.b64decode(padded_encoded_string)
        decoded_string = decoded_bytes.decode('utf-8')
        json_data = json.loads(decoded_string)
        # print("json_data = " + str(json_data))
    except Exception as e:
        print(e)
        return [link]

    ps = str(json_data["ps"]).lower()
    if "cloudflare" in ps:
        cdn = "cloudflare"
    elif "cloudfront" in ps:
        cdn = "cloudfront"
    elif "gcore" in ps:
        cdn = "gcore"
    else:
        return [link]

    ips = []
    if ipv4:
        ips += gacjie.get_ips(gacjie.get_url(cdn, "ipv4"))
    if ipv6:
        ips += gacjie.get_ips(gacjie.get_url(cdn, "ipv6"))

    # print("ips = " + str(ips))
    links = [link]

    for i, ip in enumerate(ips):
        new_json_data = copy.copy(json_data)
        new_json_data["add"] = ip
        new_json_data["ps"] = new_json_data["ps"] + str(i + 1)
        if cdn == "gcore":
            chosen_domain = random.choice(gcore_domains)
            new_json_data["sni"] = chosen_domain
        new_string = json.dumps(new_json_data)
        # print("new_string = " + str(new_string))
        new_base64_string = base64.b64encode(new_string.encode("utf-8")).decode("utf-8")
        output_string = "{}://{}".format(protol, new_base64_string)
        # print("output str = " + str(output_string))
        links.append(output_string)

    return links


if __name__ == "__main__":
    pass
