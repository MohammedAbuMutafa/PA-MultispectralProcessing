import pika
import logging
from dotenv import load_dotenv
import os


class MessageReceiver():

    def __init__(self):
        self.__init_logger__()
        load_dotenv()
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=os.getenv('RMQ_HOST')))
        self.channel = connection.channel()
        self.channel.queue_declare(queue=os.getenv('RMQ_INCOMING_NAME'))

    def __init_logger__(self):
        logging.getLogger("pika").setLevel(logging.WARNING)
        self.logger = logging.getLogger('Main.Message_Receiver')
        self.logger.setLevel(logging.DEBUG)

    def start(self, callback):
        self.channel.basic_consume(
            queue=os.getenv('RMQ_INCOMING_NAME'), on_message_callback=callback, auto_ack=True)

        self.logger.info('Listening for messages')
        self.channel.start_consuming()
