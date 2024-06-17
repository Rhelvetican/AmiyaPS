from utils.json import read_json, write_json
from server.const import USER_GACHA_PATH, CHARACTER_TABLE_URL
from misc import update_data

WELFARES = [
    "char_474_glady",
    "char_4042_lumen",
    "char_427_vigil",
    "char_1031_slent2",
    "char_4011_lessng",
    "char_4134_cetsyr",
]


def update_gacha():
    gacha = read_json(USER_GACHA_PATH)
    char_table = update_data(CHARACTER_TABLE_URL)

    preloaded_chars = gacha["advanced"]
    char_list = list()

    for char in char_table:
        if char_table[char]["rarity"] == "TIER_6" and char not in WELFARES and char not in preloaded_chars:
            char_list.append({"charId": char, "isNew": 1})
    gacha["advanced"] = char_list

    write_json(gacha, USER_GACHA_PATH)
