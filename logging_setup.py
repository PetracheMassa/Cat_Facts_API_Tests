import logging


def configure_logging():
    log_format = '%(asctime)s - [%(levelname)s] - %(message)s'
    logging.basicConfig(format=log_format, level=logging.INFO)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    # set a format for console
    formatter = logging.Formatter(log_format)
    console.setFormatter(formatter)

    # Uncomment this line to log all the messages
    logging.getLogger().setLevel(logging.INFO)

    # get the logger instance
    logger = logging.getLogger(__name__)
    logger.addHandler(console)

    return logger
