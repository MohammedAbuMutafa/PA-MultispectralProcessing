import json


class UpdateImageRequest():
    def __init__(self) -> None:
        self.is_processed = True
        self.is_analyzed = False

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)
