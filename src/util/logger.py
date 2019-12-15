import logging

class Logger:

    def __init__(self, logFileFolder):
        self.initSetup(logFileFolder)
        self.logger = logging.getLogger(__name__)

    def initSetup(self, logFileFolder):
        # set up logging to file
        logging.basicConfig(
            filename=logFileFolder + '/trading-app.log',
            level=logging.INFO,
            format='%(asctime)s [%(pathname)s:%(lineno)d] [%(levelname)s] - %(message)s'
        )
        # set up logging to console
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s: [%(levelname)s] %(message)s')
        console.setFormatter(formatter)
        # add the handler to the root logger
        logging.getLogger('').addHandler(console)

    def logInfo(self, message):
        self.logger.info(message)

    def logDebug(self, message):
        self.logger.debug(message)

    def logError(self, message):
        self.logger.error(message)