import base64
import copy
import json

import gacjie


def replace_domain2ip(link: str, ipv4=True, ipv6=True) -> list[str]:
    protol, base64_string = link.split("://")
    try:
        padded_encoded_string = base64_string + "=" * ((4 - len(base64_string) % 4) % 4)
        decoded_string = base64.b64decode(padded_encoded_string).decode("utf-8")
        json_data = json.loads(decoded_string)
        # print("json_data = " + str(json_data))
    except Exception as e:
        return [link]

    if "cloudflare" in json_data["ps"]:
        cdn = "cloudflare"
    elif "cloudfront" in json_data["ps"]:
        cdn = "cloudfront"
    elif "gcore" in json_data["ps"]:
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
        new_string = json.dumps(new_json_data)
        # print("new_string = " + str(new_string))
        new_base64_string = base64.b64encode(new_string.encode("utf-8")).decode("utf-8")
        output_string = "{}://{}".format(protol, new_base64_string)
        # print("output str = " + str(output_string))
        links.append(output_string)

    return links


if __name__ == "__main__":
    pass
