import config.config as config
from service.robinhood import RobinhoodService
from service.data_processor import DataProcessor
import os
from datetime import datetime

mainDirectory = str(os.path.abspath(os.path.dirname(__file__)))

def main():
    # testRobinhoodStuff()
    testDataExtractionStuff()
    # testTrendStuff()
    
def testRobinhoodStuff():
    robinhoodService = RobinhoodService(config.USERNAME, config.PASSWORD, mainDirectory)
    robinhoodService.login()
    robinhoodService.listStocksInAccount()

def testDataExtractionStuff():
    dataProcessor = DataProcessor(mainDirectory)
    dataProcessor.extractStockHistoricalData(['TSLA', 'AAPL'], datetime.now(), 90)

def testTrendStuff():
    dataProcessor = DataProcessor(mainDirectory)
    print(dataProcessor.getAllUpwardTrendStocks())

if __name__ == '__main__':
    main()
