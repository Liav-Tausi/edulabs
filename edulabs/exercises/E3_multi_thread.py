import time
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

    cou = requests.get(country_url + str(country_id).lower())
    country_dict = cou.json()

    # time_zones = country_dict[0]['timezones']
    # utc_time = datetime.utcnow()
    # for time_zone in time_zones:
    # local_time = utc_time.astimezone(timezone(time_zone.lower()))
    # formatted_time = local_time.strftime("%I:%M %p %Z on %B %d, %Y")
    # print(f"The current time in {time_zone} is: {formatted_time}")

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
