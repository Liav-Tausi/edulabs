from datetime import datetime
import csv


class FilesChecker:

    def __init__(self, main_directory):
        self.__main_directory: str = main_directory
        self.year: list = list()
        self.avg_list: list = list()
        self.vol: list = list()
        self.high_price: list = list()
        self.low_price: list = list()


    def avg_per_year(self, name: str):
        line_in_csv: list = list()
        counter: int = 0
        set_year: set = set()

        with open(f"{self.__main_directory}/{name}", "r") as file_handler:
            year_set = set()
            reader = csv.DictReader(file_handler)
            next(reader)

            self.year.append(set_year)
            self.year.sort()

            for row in reader:
                date = row['Date']
                dates = datetime.strptime(date, "%Y-%m-%d")
                set_year.add(dates.year)

                if counter == 0:
                    date_year = dates.year

                if dates.year == date_year:
                    self.vol.append(float(row['Volume']))
                    self.high_price.append(float(row['High']))
                    self.low_price.append(float(row['Low']))
                    counter = 1
                else:
                    line_in_csv.append({"Year": date_year,
                                        "Avg Price": (sum(self.high_price) + sum(self.low_price)) / (
                                                 len(self.high_price) + len(self.low_price)),
                                         "Min Price": min(self.low_price),
                                         "Max Price": max(self.high_price),
                                         "Avg Volume": sum(self.vol) / len(self.vol),
                                         "Min Volume": min(self.vol),
                                         "Max Volume": max(self.vol),
                                         })

                    date_year = dates.year
        with open(f"{self.__main_directory}/{'new_apple_stock.csv'}", mode="a") as fh:
            filed_names = ["Year", "Avg Price", "Min Price", "Max Price", "Avg Volume", "Min Volume", "Min Volume", "Max Volume"]
            writer = csv.DictWriter(f=fh, fieldnames=filed_names)
            writer.writeheader()
            for i in line_in_csv:
                writer.writerow(i)


if __name__ == "__main__":
    apple_file = FilesChecker("files_.ex")
    print(apple_file.avg_per_year("apple_stock.csv"))


