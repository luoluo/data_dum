import logging
class Logger:
    def __init__(self): 
        logging.basicConfig(filename="../log/log.all", level=logging.DEBUG)
        self.logger = logging.getLogger()
        wf = logging.FileHandler('../log/log.wf')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        wf.setFormatter(formatter)
        wf.setLevel(logging.WARNING)

        db = logging.FileHandler('../log/log.debug')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        db.setFormatter(formatter)
        db.setLevel(logging.DEBUG)

        info = logging.FileHandler('../log/log.info')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        info.setFormatter(formatter)
        info.setLevel(logging.INFO)

        self.logger.addHandler(info)
        self.logger.addHandler(wf)
        self.logger.addHandler(db)

    def get_logger(self):
        return self.logger
