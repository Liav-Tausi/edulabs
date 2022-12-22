import requests


class InvalidParameter(Exception):
    pass


class RequestFailed(Exception):
    pass


class TriviaBattle:
    def __init__(self, api_path: str, amount: int):
        if not isinstance(api_path, str) or not isinstance(amount, int):
            raise InvalidParameter("invalid parameters.")
        self.__amount: int = amount
        self.__api_path: str = api_path
        self.__api = requests.get(api_path, params={"amount": amount})
        if self.__api.status_code > 400:
            raise RequestFailed("Unable to fulfill request.")
        self.__question_index: int = 0
        self.__question: dict = self.__api.json()["results"][self.__question_index]

    @property
    def api_path(self):
        return self.__api_path

    @property
    def amount(self):
        return self.__amount

    @property
    def display_content(self):
        return self.__api.json()


    def get_question_index(self):
        return self.__question_index

    def set_question_index(self):
        self.__question_index += 1


    def __iter__(self):
        self.counter = 0
        self.start = self.__api.json()["results"]
        return self

    def __next__(self):
        if len(self.start) > self.counter:
            self.counter += 1
        else:
            raise StopIteration
        return self.__api.json()["results"][self.counter - 1]


class Battle(TriviaBattle):
    def __init__(self, player_one: str, player_two: str, trivia_battle: TriviaBattle, best_of: int):
        super().__init__(trivia_battle.api_path, trivia_battle.amount)
        self.__best_of: int = best_of
        self.__player_one: str = player_one
        self.__player_two: str = player_two
        self.__win_counter: dict = {player_one: 0, player_two: 0}
        self.__questions = super().display_content["results"]

    @property
    def win_counter(self):
        return self.__win_counter

    @property
    def best_of(self):
        return self.__best_of

    @property
    def player_one(self):
        return self.__player_one

    @property
    def player_two(self):
        return self.__player_two

    def display_score(self):
        return f"{self.__player_one}: {self.__win_counter[self.__player_one]} | {self.__player_two}: {self.__win_counter[self.__player_two]}"

    def is_win(self):
        if self.__win_counter[self.__player_one] > (self.__best_of / 2):
            return f"{self.__player_one} won!"
        elif self.__win_counter[self.__player_two] > (self.__best_of / 2):
            return f"{self.__player_two} won!"
        else:
            return False

    def prompt_for_answer(self, player: str):
        question = self.__questions[self.get_question_index()]
        print(f"{player}, here is your question:")
        print(f"{question['question']}\n")
        options = question['incorrect_answers'] + [question['correct_answer']]
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")
        answer = input("Insert the option name: ")
        if answer.isdigit() and int(answer) - 1 < len(options):
            answer = options[int(answer) - 1]
            if answer in question['correct_answer']:
                self.__win_counter[player] += 1
                print("Correct answer!\n")
            else:
                print("Incorect answer!\n")
        else:
            print("Invalid option. Please try again.\n")
        self.set_question_index()






