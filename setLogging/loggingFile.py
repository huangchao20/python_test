import logging

logging.basicConfig(level=logging.DEBUG, filename="test.log", format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',datefmt='%Y-%m-%d')
logging.debug("debug Message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")

