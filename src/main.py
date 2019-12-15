import config.config as config
from service.robinhood import RobinhoodService
from service.data_processor import DataProcessor
import os
from datetime import datetime

mainDirectory = str(os.path.abspath(os.path.dirname(__file__)))

def main():
    #robinhood stuff
    # robinhoodService = RobinhoodService(config.USERNAME, config.PASSWORD, logDirectory)
    # robinhoodService.login()
    # robinhoodService.listStocksInAccount()

    #data extraction stuff
    dataProcessor = DataProcessor(mainDirectory)
    dataProcessor.extractStockHistoricalData(['TSLA', 'AAPL'], datetime(2019, 12, 13), 90)

if __name__ == '__main__':
    main()
