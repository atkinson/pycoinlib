import os
from urllib.parse import urljoin
import requests

# endpoints
COINLIST = "coinlist"
COIN = "coin"
GLOBAL = "global"

# params
RANK_ASC = "rank_asc"
RANK_DESC = "rank_desc"
VOLUME_ASC = "volume_asc"
VOLUME_DESC = "volume_desc"
PRICE_ASC = "price_asc"
PRICE_DESC = "price_desc"
DATE_INSERTED_ASC = "date_inserted_asc"
DATE_INSERTED_DESC = "date_inserted_desc"

# misc
BASE_URL = "https://coinlib.io/api/v1/"
COINLIB_API_KEY = os.getenv("COINLIB_API_KEY")


def api(endpoint, **params):
    return requests.get(
        urljoin(BASE_URL, endpoint),
        params | {"key": COINLIB_API_KEY},
    ).json()
