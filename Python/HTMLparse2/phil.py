#!/usr/bin/env python3
import urllib
from urllib.request import urlopen
from urllib.parse import quote, unquote
from urllib.error import URLError, HTTPError
import re
import sys

base_link = "http://ru.wikipedia.org/wiki/"


def get_content(name):
    try:
        page = (
            urllib.request.urlopen(base_link + quote(name))
            .read()
            .decode("utf8", "ignore")
        )
    except (HTTPError, URLError):
        return None
    page = str(
        urllib.request.urlopen(base_link + quote(name))
        .read()
        .decode("utf8", "ignore")
    )
    return page


def extract_content(page):
    return (
        page.find("ru.wikipedia.org/wiki/"),
        page.rfind("ru.wikipedia.org/wiki/") + 100
    )
    pass


def extract_links(page, begin=404, end=303):
    if page is None:
        return []
    if (begin == 404 and end == 303) or begin > end:
        borders = extract_content(page)
        page = page[borders[0]:borders[1]]
    else:
        page = page[begin:end]
    result = re.findall("[H,h]ref=[',\"]/wiki/([^:#]*?)[',\"]", page)
    result = list(map(unquote, result))
    return result
    pass


def find_chain(start, finish):
    if start == finish:
        return [start, finish]
    start_full_link = base_link + start
    finish_full_link = base_link + finish
    node = start
    visited = []
    queue = []
    cnt = 0
    visited.append(node)
    queue.append(node)
    dictionary = {}
    while queue:
        m = queue.pop(0)
        graph = extract_links(get_content(m))
        for itera in graph:
            if not (itera in dictionary):
                dictionary[itera] = m
            if itera not in visited:
                if unquote(itera) == finish:
                    i = itera
                    path = []
                    path.append(finish)
                    while dictionary.get(i, start) != start:
                        path.insert(0, unquote(dictionary[i]))
                        i = unquote(dictionary[i])
                    path.insert(0, start)
                    return path
                visited.append(itera)
                queue.append(itera)
        cnt += 1
        if cnt >= 150:
            return None
    return None
    pass


def main():
    pass


if __name__ == "__main__":
    main()
