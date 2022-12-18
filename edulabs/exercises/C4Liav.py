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

    def __repr__(self):
        return f"{self.__bookmarks}"


    def get_total_pages(self) -> int:
        return len(self.__pages)


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
    e_book.get_total_pages()

    # pprint.pprint(e_book.display_content_for_page(27))
    e_book.bookmark(27, "last page")
    e_book.bookmark(1, "first page")
    e_book.bookmark(1, "hello")

    pprint.pprint(e_book._EBook__bookmarks)
    e_book.del_bookmark_page(1)

    pprint.pprint(e_book._EBook__bookmarks)
    e_book.bookmark(1, "first")
    pprint.pprint(e_book._EBook__bookmarks)

    e_book.display_bookmarks()

    print(e_book.display_bookmarked_page_by_name("first"))






