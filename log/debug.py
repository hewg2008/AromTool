import logging


class Logger:

    @staticmethod
    def set_log(log_path, logger_name):
        logger = logging.getLogger(logger_name)
        handler1 = logging.StreamHandler()
        handler2 = logging.FileHandler(filename=log_path)

        logger.setLevel(logging.DEBUG)
        handler1.setLevel(logging.DEBUG)
        handler2.setLevel(logging.DEBUG)

        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
        handler1.setFormatter(formatter)
        handler2.setFormatter(formatter)

        logger.addHandler(handler1)
        logger.addHandler(handler2)

        return logger

    @staticmethod
    def log(msg):
        logging.info(msg)

    @staticmethod
    def error(msg):
        logging.error(msg)
