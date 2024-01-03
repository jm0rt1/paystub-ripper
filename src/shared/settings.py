

from pathlib import Path


class GlobalSettings():
    ##
    # Paths ---------
    APP_DIR = Path("./").resolve()

    # I/O Directories
    OUTPUT_DIR = APP_DIR/"output"
    INPUT_DIR = APP_DIR/"input"
    # Logging Related Paths
    LOGS_DIR = OUTPUT_DIR/"logs"
    GLOBAL_LOGS_DIR = LOGS_DIR/"global"
    UI_LOGS_DIR = LOGS_DIR/"ui"
    # Paths ---------

    ##

    class LoggingParams():
        BACKUP_COUNT = 10
        GLOBAL_FILE_NAME = "global.log"

    # Operations
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    LOGS_DIR.mkdir(exist_ok=True, parents=True)
    GLOBAL_LOGS_DIR.mkdir(exist_ok=True, parents=True)
    UI_LOGS_DIR.mkdir(exist_ok=True, parents=True)
