class TableExeptions(Exception):
    pass

class TableNotAvailableError(TableExeptions):
    def __init__(self):
        super().__init__("Table not available.")


class TableAlreadyAvailableError(TableExeptions):
    def __init__(self):
        super().__init__("Table already available.")


class NotEnoughSeatsError(TableExeptions):
    def __init__(self):
        super().__init__("Not enough seats.")


class TableDoesNotExistError(TableExeptions):
    def __init__(self):
        super().__init__("Table does not exist.")