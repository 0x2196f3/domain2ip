import re
import urllib.parse


def get_links(url: str) -> list[str]:
    url = urllib.parse.unquote(url)
    start_index = url.find("url=") + len("url=")
    end_index = url.find("&", start_index)
    pattern = r"(\w+://[\w\.\/\-]+)"
    links = re.findall(pattern, url[start_index:end_index])
    return links


def build_url(old_url: str, links: list[str]) -> str:
    start_index = old_url.find("url=") + len("url=")
    end_index = old_url.find("&", start_index)

    new_url = old_url[:start_index]

    for i, link in enumerate(links):
        if i < len(links) - 1:
            new_url += urllib.parse.quote(link + "|")
        else:
            new_url += urllib.parse.quote(link)

    new_url += old_url[end_index:]
    return new_url


if __name__ == "__main__":
    get_links("http://192.168.2.2:9013/sub?target=clash&url=vmess%3A%2F%2FeyJhZGQiOiJuZXh0Y2xvdWQuMHgyMTk2ZjMudG9wIiwiYWlkIjoiMCIsImFscG4iOiIiLCJmcCI6IiIsImZyYWdtZW50IjoiIiwiZnJhZ21lbnRfdjEiOiIiLCJob3N0IjoiIiwiaWQiOiI3MjkxYWQ1Yi05NThiLTQ0YWYtZWM0NS05OGUzNDNjZDQxNzAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvY2xvdWRmbGFyZTM3MTc4IiwicG9ydCI6IjQ0MyIsInBzIjoiY2xvdWRmbGFyZSIsInNjeSI6ImF1dG8iLCJzbmkiOiIiLCJ0bHMiOiJ0bHMiLCJ0eXBlIjoiIiwidiI6IjIifQ%3D%3D%7Cvmess%3A%2F%2FeyJhZGQiOiJjbG91ZHJldmUuMHgyMTk2ZjMudG9wIiwiYWlkIjoiMCIsImFscG4iOiIiLCJmcCI6IiIsImZyYWdtZW50IjoiIiwiZnJhZ21lbnRfdjEiOiIiLCJob3N0IjoiIiwiaWQiOiJjZTQyMDczOS0yMTE3LTQ2M2EtOWFjMC0zYzY2MWZlNDY2Y2YiLCJuZXQiOiJ3cyIsInBhdGgiOiIvY2xvdWRmcm9udDM3MTc5IiwicG9ydCI6IjQ0MyIsInBzIjoiY2xvdWRmcm9udCIsInNjeSI6ImF1dG8iLCJzbmkiOiIiLCJ0bHMiOiJ0bHMiLCJ0eXBlIjoiIiwidiI6IjIifQ%3D%3D&config=https%3A%2F%2Fraw.githubusercontent.com%2FACL4SSR%2FACL4SSR%2Fmaster%2FClash%2Fconfig%2FACL4SSR_Online.ini")