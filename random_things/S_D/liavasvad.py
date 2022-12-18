import csv
from datetime import datetime


def aapl_filse(path):
    counter = 0
    vol = []
    high_price = []
    low_price = []
    line_in_csv = []
    with open(path) as csv_file:
        reader = csv.DictReader(csv_file)

        for item in reader:
            # Inserts the date of each row
            date = item['Date']
            date = datetime.strptime(date, "%d-%m-%Y")

            # enter the first year in variable
            if counter == 0:
                date_year = date.year

            if date.year == date_year:
                vol.append(float(item['Volume']))
                high_price.append(float(item['High']))
                low_price.append(float(item['Low']))
                counter = 1
            else:
                # When we come to a new year, we enter all the details and reset the variables for the next year
                line_in_csv.append({'Year': date_year,
                                    'Avg Price': (sum(high_price) + sum(low_price)) / (len(high_price) + len(low_price)),
                                    'Min Price': min(low_price), 'Max Price': max(high_price),
                                    'Avg Volume': sum(vol) / len(vol), 'Min Volume': min(vol), 'Max Volume': max(vol)})
                high_price = []
                low_price = []
                vol = []
                date_year = date.year

    with open('files\\PL.csv', "w") as csv_f:
        writer = csv.DictWriter(csv_f, ['Year',  'Avg Price', 'Min Price', 'Max Price', 'Avg Volume',
                                        'Min Volume', 'Max Volume'])
        writer.writeheader()
        for row in line_in_csv:
            writer.writerow(row)