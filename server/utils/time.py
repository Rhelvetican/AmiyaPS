from server.utils.json import read_json
from time import time as real_time
from server.const import CONFIG_PATH


def faketime():
    config = read_json(CONFIG_PATH)
    fakeTime = config["userConfig"]["fakeTime"]
    if fakeTime == -1:
        return real_time()
    return real_time() % (24 * 60 * 60) + fakeTime
