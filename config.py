import os
API_ID = int(os.getenv("3817560"))
API_HASH = os.getenv("9a7e405618e748312a0eca579e1a776b")
BOT_TOKEN = os.getenv("1794885294:AAGtC333USNumGWHwqF4Ots9pgcG2-lVDEI")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("182670646", "").split()})
