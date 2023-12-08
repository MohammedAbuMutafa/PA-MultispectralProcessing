from Modules.Messaging.BaseQueueSender import BaseQueueSender
from dto.ProcessedImageDTO import ProcessedImageDTO
import os
import json


class ProcessedImageSender(BaseQueueSender):

    def __init__(self) -> None:
        rmq_host = os.getenv("RMQ_HOST")
        queue_name = os.getenv("RMQ_OUTGOING_NAME")
        name = __name__
        super().__init__(queue_name, rmq_host, name)

    def publish_new_image(self, message: ProcessedImageDTO):
        json_dto = message.get_json()
        self.logger.info(f"publishing new msg to queue:\n{json_dto}")
        json_dto: str = json.dumps(json_dto)
        self.send(message=json_dto)
