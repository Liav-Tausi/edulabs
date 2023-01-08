class VTAutomatorError(Exception):
    pass


class RequestFailed(VTAutomatorError):
    def __init__(self):
        super().__init__("Unable to fulfill request status over 400.")


class ApiKeyError(VTAutomatorError):
    def __init__(self):
        super().__init__("Invalid api key.")


class FileDescError(VTAutomatorError):
    def __init__(self):
        super().__init__("Invalid File Description.")


class UrlError(VTAutomatorError):
    def __init__(self):
        super().__init__("Invalid url.")


class FileError(VTAutomatorError):
    def __init__(self):
        super().__init__("Invalid path.")


class EmptyContentError(VTAutomatorError):
    def __init__(self):
        super().__init__("Empty return.")


