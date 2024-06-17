from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from utils.json import load_json

LOG_TOKEN_KEY = "pM6Umv*^hVQuB6t&"


def decrypt_battle_data(data: str, login: int = 1672502400):
    try:
        battle_data = bytes.fromhex(data[: len(data) - 32])
        src = LOG_TOKEN_KEY + str(login)
        key = md5(src.encode()).digest()
        iv = bytes.fromhex(data[len(data) - 32 :])
        aes = AES.new(key, AES.MODE_CBC, iv)
        decrypt_data = unpad(aes.decrypt(battle_data), AES.block_size)
        return load_json(decrypt_data)
    except Exception as e:
        print(e)
        return {}
