# 5 SEC LEVELS OF LOGGING
# DEBUG
# INFO 
# WARNING
# ERROR
# CRITICAL 

# Standard Logging

import logging 

logging.basicConfig(level=logging.DEBUG)
logging.info("You have got 20 mails in our inbox!")
logging.critical("All components failed! ")


# Create Own Logger

logger = logging.getLogger("ZEN Logger")
logger.info("The best logger was just created!")
logger.log(logging.ERROR, "An error occured")

# Log into  Files 

logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("my_log.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s") # Format Log
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("This is a debug message!")
logger.info("This is important information")