import os
import time
import pytz
import requests
import concurrent
from concurrent.futures import ThreadPoolExecutor, wait
from datetime import datetime
from pytz import timezone


# 1 - 2  rewrite the code using multithreading and ThreadPoolExecutor to improve the performance of your code.
# Log the run time and compare the results with previous version of your code when running it on 10 names
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
    curr_time = pytz.utc.localize(datetime.utcnow(), is_dst=None).astimezone(timezone(country_timezones[0]))

    if (eth.status_code or cou.status_code) <= 400:
        print(
            f"status code: {eth.status_code}, {name} your ethnicity is most probably from "
            f"{country_dict[0]['name']['common']} in {(country_dict[0]['continents'])[0]} and you speak "
            f"{list(dict(country_dict[0]['languages']).values())}"
            f" at {ethnicity['probability'] * 100}%\n "
            f"Timezone: {country_timezones[0]}, Time: {curr_time.strftime('%H:%M')}")

    else:
        raise Exception()


NAMES = ["Kenyon", "Deshawn", "Michaela", "Molly", "Barrett", "Steven", "Brisa", "Zackery", "Kamora", "Sara", "Jaycee",
         "Leland", "Danny", "Ashlee", "Royce", "Bryce", "Anabel", "Skyler", "Cristian", "Shannon", "Aditya", "Asher",
         "Quintin", "Hunter", "Rose", "Ronin", "Zion", "Rayne", "Nyasia", "Sanaa", "Dominic", "Tyshawn", "Gillian",
         "Clayton", "Easton", "Julio", "Coby", "Melany", "Bradyn", "Jazlene", "Myah", "Zayden", "Noemi", "Brooks",
         "Mckenzie", "Khalil", "Ruben", "Kristina", "Dixie", "Sawyer", "Ali", "Nasir", "Kaylynn", "Messiah", "Kevin",
         "Will", "Cordell", "Dereon", "Jamari", "Adrien", "Ashtyn", "Santos", "Isabela", "Lucas", "Harley", "Esteban",
         "Zain", "Alma", "Elliot", "Collin", "Alexa", "Magdalena", "Kristopher", "Kaya", "Jaydin", "Aimee", "June",
         "Ryland", "Belinda", "Kennedy", "Mohammed", "Kenna", "Kaia", "Ada", "Frida", "Valeria", "Noe", "Savannah",
         "Jorge", "Claire", "Abdullah", "Hillary", "Drake", "Kristen", "Amelia", "Marcus", "Liana", "Saniya", "Karissa",
         "Jasper"]


# 3 Create a txt file with 100 different names get the nationalities for the names and store the pairs of name and nationality in a new file
# Try running both versions of your code - single threaded and multithreaded. Compare run time. Tune the amount of executor workers such that
# the performance will be the best,
# and make sure you don't get blocked by the servers you are sending requests to because of too many simultaneous requests from the same ip

def get_etnithity_two(*args):
    if not os.path.exists('e3_files'):
        os.makedirs('e3_files')
    executor = ThreadPoolExecutor(max_workers=16)
    futures = []
    for name in args[0]:
        futures.append(executor.submit(get_nationality_for_name, name))
    wait(futures, return_when=concurrent.futures.ALL_COMPLETED)


def get_nationality_for_name(name):
    ethnicity_url = "https://api.nationalize.io/"
    country_url = "https://restcountries.com/v3.1/alpha/"
    eth = requests.get(ethnicity_url, params={"name": name})
    eth_json = eth.json()
    country_id = eth_json['country'][0]['country_id']

    cou = requests.get(country_url + str(country_id).lower())
    country_dict = cou.json()

    country_name = country_dict[0]['name']['common']

    if eth.status_code > 400 or cou.status_code > 400:
        raise Exception("over 400")
    else:
        with open(f"e3_files/files_{name}.txt", 'w') as fh:
            fh.write(f"{name}'s nationality is most probably from {country_name} ")


if __name__ == "__main__":

    # 1 - 2:
    # try:
    #     start = time.perf_counter()
    #     get_etnithity('liav', 'aviv', 'rotem', 'tomer', 'ido', 'vlad', 'rachel', 'roni', 'toni', 'alex')
    #     end = time.perf_counter()
    #     print(end - start)
    # except Exception:
    #     print("Error")

    # 3 :

    try:
        start = time.perf_counter()
        get_etnithity_two(NAMES)
        end = time.perf_counter()
        print(end - start)
    except Exception:
        print("Error")
