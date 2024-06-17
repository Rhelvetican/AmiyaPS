from utils.json import read_json, load_json, write_json
from server.const import (
    CONFIG_PATH,
    ACTIVITY_TABLE_URL,
    CHARM_TABLE_URL,
    SKIN_TABLE_URL,
    CHARACTER_TABLE_URL,
    BATTLEEQUIP_TABLE_URL,
    EQUIP_TABLE_URL,
    STORY_TABLE_URL,
    STAGE_TABLE_URL,
    RL_TABLE_URL,
    DM_TABLE_URL,
    RETRO_TABLE_URL,
    HANDBOOK_INFO_TABLE_URL,
    TOWER_TABLE_URL,
    BUILDING_TABLE_URL,
    SANDBOX_TABLE_URL,
    STORY_REVIEW_TABLE_URL,
    STORY_REVIEW_META_TABLE_URL,
    ENEMY_HANDBOOK_TABLE_URL,
    MEDAL_TABLE_URL,
    CHARWORD_TABLE_URL,
    GACHA_TABLE_URL,
    GAMEDATA_CONST_URL,
)

from base64 import b64decode
from requests import get

URL = "aHR0cHM6Ly9hay1jb25mLmh5cGVyZ3J5cGguY29tL2NvbmZpZy9wcm9kL29mZmljaWFsL"


def update_cfg() -> bool:
    excel_update_required = False
    config = read_json(CONFIG_PATH)
    old_res_ver = config["version"]["android"]["resVersion"]
    old_clt_ver = config["version"]["android"]["clientVersion"]
    old_fnc_ver = config["networkConfig"]["cn"]["content"]["funcVer"]
    new_res_cfg = get(b64decode(f"{URL}0FuZHJvaWQvdmVyc2lvbg==")).json()
    new_net_cfg = get(b64decode(f"{URL}25ldHdvcmtfY29uZmln")).json()
    if old_res_ver != new_res_cfg["resVersion"]:
        excel_update_required = True
        config["version"]["android"]["resVersion"] = new_res_cfg["resVersion"]
    if old_clt_ver != new_res_cfg["clientVersion"]:
        excel_update_required = True
        config["version"]["android"]["clientVersion"] = new_res_cfg["clientVersion"]

    content = load_json(new_net_cfg["content"])
    func_ver = content["funcVer"]

    if old_fnc_ver != func_ver:
        excel_update_required = True
        config["networkConfig"]["cn"]["content"]["funcVer"] = func_ver
        config["networkConfig"]["cn"]["content"]["configs"][str(func_ver)] = config["networkConfig"]["cn"]["content"]["configs"][str(old_fnc_ver)]
        del config["networkConfig"]["cn"]["content"]["configs"][str(old_fnc_ver)]

    write_json(config, CONFIG_PATH)

    return excel_update_required


def update_excel():
    for url in [
        ACTIVITY_TABLE_URL,
        CHARM_TABLE_URL,
        SKIN_TABLE_URL,
        CHARACTER_TABLE_URL,
        BATTLEEQUIP_TABLE_URL,
        EQUIP_TABLE_URL,
        STORY_TABLE_URL,
        STAGE_TABLE_URL,
        RL_TABLE_URL,
        DM_TABLE_URL,
        RETRO_TABLE_URL,
        HANDBOOK_INFO_TABLE_URL,
        TOWER_TABLE_URL,
        BUILDING_TABLE_URL,
        SANDBOX_TABLE_URL,
        STORY_REVIEW_TABLE_URL,
        STORY_REVIEW_META_TABLE_URL,
        ENEMY_HANDBOOK_TABLE_URL,
        MEDAL_TABLE_URL,
        CHARWORD_TABLE_URL,
        GACHA_TABLE_URL,
        GAMEDATA_CONST_URL,
    ]:
        data = get(url).json()
        local_path = url.replace("https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata", "data")
        write_json(data, local_path)
        print(f"Updated: {local_path}")
