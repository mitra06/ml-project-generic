import logging
import os
from datetime import datetime

log = f"{datetime.now().strftime('%m_%D_%Y_%H_%M_%S')}"
log_path = os.path.join(os.getcwd(),"logs",log)
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, log)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
    level= logging.INFO,
) 