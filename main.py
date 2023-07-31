import sys
import os
import logging
import datetime
from pyfiglet import Figlet
from Processors.NewImageProcessor import NewImageProcessor

version = '0.0.1'


def init_logger():

    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(FORMAT)

    date = datetime.datetime.now()
    t = date.strftime("%Y%d%m%H%M%S")
    log_file_name = f"log-"+t+".log"
    if not os.path.isdir('logs'):
        os.mkdir("logs")

    file = logging.FileHandler(filename='logs/'+log_file_name)
    file.setFormatter(formatter)
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)
    log = logging.getLogger()
    log.addHandler(file)
    log.setLevel(level=logging.DEBUG)


def startup_splash():

    f = Figlet(font='slant')
    print(f.renderText('Processing Service'))
    print(f"Version: {version}")
    print("-------------------------------------------------------")


def main():

    startup_splash()
    init_logger()

    _ = NewImageProcessor()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting, keyboard interupt")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except Exception:
        logging.error(f"Unhandled exception: {Exception}")
