import json


class UpdateSessionPathRequest():
    def __init__(self, path: str) -> None:
        self.sessionPath = path

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)
