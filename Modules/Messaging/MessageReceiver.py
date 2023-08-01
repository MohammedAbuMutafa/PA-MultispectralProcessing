import pika
import logging
import os


class MessageReceiver():

    def __init__(self, callback):
        self.__init_logger__()        
        connection_result = self.__connect__()
        if (connection_result == True):
            self.start(callback=callback)

        raise ConnectionError("Unable to connect to messaging queue")

    def __init_logger__(self):
        logging.getLogger("pika").setLevel(logging.FATAL)
        self.logger = logging.getLogger('Main.Message_Receiver')
        self.logger.setLevel(logging.DEBUG)

    def __connect__(self):
        retry = 0
        max_retry = 5
        while (retry < max_retry):
            try:
                if (retry == max_retry):
                    return False

                connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host=os.getenv('RMQ_HOST')))
                self.channel = connection.channel()
                self.channel.queue_declare(
                    queue=os.getenv('RMQ_INCOMING_NAME'))

                return True

            except Exception:
                retry += 1
                self.logger.warn(
                    f"Unable to connect to message broker, retrying... {retry}")

    def start(self, callback):
        try:
            self.channel.basic_consume(
                queue=os.getenv('RMQ_INCOMING_NAME'), on_message_callback=callback, auto_ack=True)
            self.logger.info('Listening for messages')
            self.channel.start_consuming()
        except Exception:
            self.logger.fatal(
                f"Message broker lost, unable to communicate")
