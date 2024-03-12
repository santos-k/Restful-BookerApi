import os
import logging


class GenerateLog:
    @staticmethod
    def generate_log():
        logger = logging.getLogger()
        logger.handlers.clear()

        file_path = "./././Results/Logs/api.log"
        if not os.path.exists(file_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create directory if it doesn't exist
        file_handler = logging.FileHandler(filename=file_path, mode='a')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(pathname)s::%(lineno)d - %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger
