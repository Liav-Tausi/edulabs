import time

import pytz
import requests
import concurrent
from concurrent.futures import ThreadPoolExecutor, wait
from datetime import datetime
from pytz import timezone




def get_etnithity(*args):
    executor = ThreadPoolExecutor(max_workers=16)
    futures = []
    for name in args:
        futures.append(executor.submit(name_func, name))

    done, not_done = wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
    print(f"done: {len(done)}")
    print(f"not done: {len(not_done)}")


def name_func(name):
    ethnicity_url = "https://api.nationalize.io/"
    country_url = "https://restcountries.com/v3.1/alpha/"
    eth = requests.get(ethnicity_url, params={"name": name})
    eth_json = eth.json()

    ethnicity = sorted(eth_json['country'], key=lambda x: x["probability"], reverse=True)[0]
    country_id = eth_json['country'][0]['country_id']
    country_timezones = pytz.country_timezones[country_id]
    cou = requests.get(country_url + str(country_id).lower())
    country_dict = cou.json()

    for country_time in country_timezones:
        curr_time = pytz.utc.localize(datetime.utcnow(), is_dst=None).astimezone(timezone(country_time))
        print(f"> Timezone: {country_time}, Time: {curr_time.strftime('%H:%M')}")
    if (eth.status_code or cou.status_code) <= 400:
        print(
            f"status code: {eth.status_code}, {name} your ethnicity is most probably from "
            f"{country_dict[0]['name']['common']} in {(country_dict[0]['continents'])[0]} and you speak "
            f"{list(dict(country_dict[0]['languages']).values())}"
            f" at {ethnicity['probability'] * 100}% ")

    else:
        raise Exception()


if __name__ == "__main__":
    try:
        start = time.perf_counter()
        get_etnithity('liav', 'aviv', 'rotem', 'tomer', 'ido', 'vlad', 'rachel', 'roni', 'toni', 'alex')
        end = time.perf_counter()
        print(end - start)
    except Exception:
        print("Error")
