
class EfiveExeptions(Exception):
    pass


class UnExceptableFile(EfiveExeptions):
    def __init__(self, msg: str):
        super().__init__(f"{msg} file is not csv ")
