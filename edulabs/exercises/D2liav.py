from datetime import datetime
from calendar import monthrange


# 1 Implement a simple class DateIterator that should be initialized with a date and implements iterator protocol
# (__iter__ and __next__ method)  that on every iteration returns the next date up until the end of the month.

class DateIterator:

    def __init__(self, date: str):
        self.date = datetime.strptime(date, "%d-%m-%Y").date()
        self.days_in_month = monthrange(self.date.year, self.date.month)[1]

    def __iter__(self):
        self.start = int(self.date.day)
        return self

    def __next__(self):
        if self.start < self.days_in_month:
            self.start += 1
        else:
            raise StopIteration
        return datetime(day=self.start, month=self.date.month, year=self.date.year).date()


if __name__ == "__main__":
    for i in DateIterator("10-04-2002"):
        print(i)

# 2  Add iterator protocol (__iter__ and __next__ method) to the existing implementation of the EBook class. The iterator should work as follows
#  - on each iteration it should return the content of the next book page, starting from the first page up until the last one.

import pprint

class EBook:

    def __init__(self, file: str, words_per_page: int):
        self.__file: str = file
        self.__pages: dict[int, str] = dict()
        self.__bookmarks: dict[str, int] = dict()

        with open(file, "r") as file_handler:
            content: list[str] = file_handler.read().split()

        page_num: int = 1
        for i in range(0, len(content), words_per_page):
            page_words: list[str] = content[i:i+words_per_page]
            self.__pages[page_num] = " ".join(page_words)
            page_num += 1

    def __iter__(self):
        self.page = 1
        return self

    def __next__(self):
        if self.page > self.get_total_pages():
            raise StopIteration
        else:
            page = self.__pages[self.page]
            self.page += 1
            return page

    def __repr__(self):
        return f"{self.__bookmarks}"

    def get_total_pages(self) -> int:
        return len(self.__pages)

    def display_all(self):
        return self.__pages


    def display_content_for_page(self, page_number: int) -> str :
        return self.__pages[page_number]

    def bookmark(self, page_number: int, bookmark_name: str) -> dict[str,int]:
        if (page_number in self.__pages.keys()) and (bookmark_name not in self.__bookmarks):
            self.__bookmarks[bookmark_name] = page_number
            return self.__bookmarks

    def del_bookmark_name(self, bookmark_name: str) -> int:
        if bookmark_name in self.__bookmarks:
            return self.__bookmarks.pop(bookmark_name)

    def del_bookmark_page(self, bookmark_page: int) -> bool:
        update_bookmarks: dict = dict()
        if bookmark_page in self.__bookmarks.values():
            for keys, values in self.__bookmarks.items():
                if values != bookmark_page:
                    update_bookmarks[keys] = values
            self.__bookmarks = update_bookmarks
            return True
        raise KeyError

    def display_bookmarks(self):
        print(self.__repr__())

    def display_bookmarked_page_by_name(self, bookmark_name: str):
        if bookmark_name in self.__bookmarks.keys():
            value = self.__bookmarks[bookmark_name]
            return self.__pages[value]


if __name__ == "__main__":
    e_book: EBook = EBook("../FileHandeler/FHfiles/alice_in_wonderland.txt", 1000)
    # e_book.get_total_pages()
    for i in e_book:
        print(i)

    # pprint.pprint(e_book.display_content_for_page(27))

    # print(e_book.display_all())

    # e_book.bookmark(27, "last page")
    # e_book.bookmark(1, "first page")
    # e_book.bookmark(1, "hello")
    #
    # pprint.pprint(e_book._EBook__bookmarks)
    # e_book.del_bookmark_page(1)
    #
    # pprint.pprint(e_book._EBook__bookmarks)
    # e_book.bookmark(1, "first")
    # pprint.pprint(e_book._EBook__bookmarks)
    #
    # e_book.display_bookmarks()
    #
    # print(e_book.display_bookmarked_page_by_name("first"))







