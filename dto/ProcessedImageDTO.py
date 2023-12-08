class ProcessedImageDTO():

    def __init__(self, id, session_id, fileName, indices, session_dir):
        self.id = id
        self.fileName = fileName
        self.indices = indices
        self.session_dir = session_dir
        self.session_id = session_id

    def get_json(self):
        return {
            "id": self.id,
            "session_id": self.session_id,
            "fileName": self.fileName,
            "indices": self.indices,
            "session_dir": self.session_dir,
        }
