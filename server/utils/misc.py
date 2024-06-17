from server.utils.json import read_json
from os import path as ospath, makedirs
from requests import get


def update_data(url):
    BASE_URL_LIST = [
        (
            "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata",
            "data",
        ),
        (
            "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/en_US/gamedata",
            "data-global",
        ),
        (
            "https://ak-conf.hypergryph.com/config/prod/announce_meta/Android",
            "data/announce",
        ),
        (
            "https://ark-us-static-online.yo-star.com/announce/Android",
            "data/announce",
        ),
    ]

    data = {}

    localPath = ""

    for index in BASE_URL_LIST:
        if index[0] in url:
            if not ospath.isdir(index[1]):
                makedirs(index[1])
            localPath = url.replace(index[0], index[1])
            break

    if not ospath.isdir("data/excel/"):
        makedirs("data/excel/")

    if "Android/version" in url:
        data = get(url).json()
        return data
    current_is_mod = False

    if not current_is_mod:
        try:
            raise Exception

        except Exception as e:
            print(e)
            data = read_json(localPath)
    else:
        data = read_json(localPath)

    return data
