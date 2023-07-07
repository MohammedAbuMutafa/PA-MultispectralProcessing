import pika
import logging
from dotenv import load_dotenv
import os

class MessageSender():

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.getenv('RMQ_HOST')))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=os.getenv('RMQ_OUTGOING_NAME'))

    def __init_logger__(self):
        logging.getLogger("pika").setLevel(logging.WARNING)
        self.logger = logging.getLogger('Main.Message_Sender')
        self.logger.setLevel(logging.DEBUG)       

    def kill(self):
        self.connection.close()

    def publish(self, message):     
        self.channel.basic_publish(exchange= os.getenv('RMQ_EXCHANGE'),
                            routing_key=os.getenv('RMQ_ROUTING_KEY'),
                            body=message)        
