class ConfigException(Exception):
    pass


class ParamsException(Exception):
    pass

class GenericError(Exception):
    def __init__(self, data):
        self.code = data.get("code")
        self.message = data.get("message")
        super().__init__(f"{self.code}: {self.message}")

    def __str__(self):
        return f"{self.code}: {self.message}"
