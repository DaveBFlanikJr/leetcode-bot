import logging

def setup_logging():
    logging.basicConfig(level=logging.DEBUG,  # Set logging level
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.StreamHandler(),  # Log to console
                            logging.FileHandler('app.log')  # Log to file
                        ])
