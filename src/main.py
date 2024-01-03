import logging
import logging.handlers
from pathlib import Path
from src.shared.settings import GlobalSettings
from src.ripper.ripper import PDFSplitter
import os


def initialize_logging():

    file_handler = logging.handlers.RotatingFileHandler(
        GlobalSettings.GLOBAL_LOGS_DIR/GlobalSettings.LoggingParams.GLOBAL_FILE_NAME,
        backupCount=GlobalSettings.LoggingParams.BACKUP_COUNT)

    logging.getLogger().addHandler(file_handler)
    file_handler.doRollover()
    logging.info("Global Logging Started")


def main():
    """run a console menu that has two options, runs in a while loop so multiple options can be selected"""

    initialize_logging()
    # Usage
    input_foler_path = Path("./input")
    for file_name in os.listdir(input_foler_path):
        if file_name.endswith(".pdf"):
            pdf_splitter = PDFSplitter(
                GlobalSettings.INPUT_DIR/file_name, GlobalSettings.OUTPUT_DIR)
            pdf_splitter.split()
