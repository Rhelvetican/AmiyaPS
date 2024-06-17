from utils.excel import update_cfg, update_excel
from utils.gacha import update_gacha
from utils.json import read_json
from utils.fmt import fmt_cfg, fmt_excel
from server.const import CONFIG_PATH


def upgrade():
    config = read_json(CONFIG_PATH)
    update_required = update_cfg()

    if update_required or config["server"]["forceUpdateExcel"]:
        update_excel()
        update_gacha()
        fmt_excel()
        fmt_cfg()
