import logging
from logging.handlers import RotatingFileHandler
import os

class ColoredFormatter(logging.Formatter):
    COLORS: dict[str, str] = {
        'DEBUG': '\033[94m',    # Blue
        'INFO': '\033[92m',     # Green
        'WARNING': '\033[93m',  # Yellow
        'ERROR': '\033[91m',    # Red
        'CRITICAL': '\033[95m', # Magenta
        'RESET': '\033[0m'      # Reset to default
    }

    def format(self, record):
        color: str = self.COLORS.get(record.levelname, self.COLORS['RESET'])
        reset: str = self.COLORS['RESET']
        formatted_record: str = f"{color}[{record.levelname}] {reset} - {record.getMessage()}"
        return formatted_record

def setup_logger(name: str, log_file: str) -> logging.Logger:
    '''
    Set up a logger with the specified name and log file, directing the log file to the logs/ directory.

    Args:
        name (str): The name of the logger.
        log_file (str): The file name to which the log will be written (inside logs/ directory).

    Returns:
        logging.Logger: Configured logger instance.
    '''

    # Ensure the logs directory exists
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Full path for the log file
    log_file_path: str = os.path.join(logs_dir, log_file)

    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Console handler with color
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = ColoredFormatter()
    console_handler.setFormatter(console_formatter)

    # File handler without color
    file_handler = RotatingFileHandler(log_file_path, maxBytes=1_000_000, backupCount=4)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    # Add both handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
