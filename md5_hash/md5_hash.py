import hashlib
import os

from dotenv import load_dotenv

load_dotenv()


def calculate_md5(string, count: int = 0):
    if count == 0 or count < 0:
        count = int(os.getenv("MD_5_COUNT"))
    for i in range(0, count):
        md5_hash = hashlib.md5()
        md5_hash.update(string.encode('utf-8'))
        string = md5_hash.hexdigest()
    return string

