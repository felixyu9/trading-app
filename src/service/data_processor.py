from util.logger import Logger
import config.config as config
import os
import pandas as pd
from datetime import datetime, timedelta
from iexfinance.stocks import get_historical_intraday
import numpy

class DataProcessor:

    def __init__(self, mainDirectory):
        os.environ['IEX_TOKEN'] = config.IEX_TOKEN
        global logger
        logger = Logger(os.path.join(mainDirectory, 'logs'))
        global historicalDataDirectory
        historicalDataDirectory = os.path.join(mainDirectory, 'resources','historical_data')

    def extractStockHistoricalData(self, stocks, endDate, daysback):
        #extract minute stock data for a period of time. parameter stocks is a list of stock symbols
        try:
            for stock in stocks:
                date = endDate
                logger.logInfo('Getting data for: ' + stock)
                historicalData = pd.DataFrame()
                for i in range(daysback):
                    if i == 0:
                        historicalData = get_historical_intraday(stock, date, output_format='pandas')
                        date = date - timedelta(days=1)    
                        continue

                    tempData = get_historical_intraday(stock, date, output_format='pandas')
                    historicalData = historicalData.append(tempData)
                    date = date - timedelta(days=1)
                logger.logInfo('Saving data for: ' + stock)
                fileName = '%s\%s_%i_days_ended_on_%s.csv' %(historicalDataDirectory, stock, daysback, str(endDate.date()))
                historicalData.to_csv(fileName)
                # TODO: call the uploadDataToS3() method
                logger.logInfo('Data for ' + stock + ' is saved in ' + fileName)
        except Exception as ex:
            logger.logError('Error extracting stock data. Error: ' + ex)

    def uploadDataToS3(self):
        # TODO: update the data to aws s3 bucket
        pass

    #TODO: add method to analyze the data

    def getAllUpwardTrendStocks(self):
        #get all the stocks in the resources folder that are upward trended
        upwardStocks = []
        for path in os.listdir(historicalDataDirectory):
            fullPath = os.path.join(historicalDataDirectory, path)
            if os.path.isfile(fullPath):
                if self.stockTrendIsUpward(fullPath):
                    upwardStocks.append(path.split('_')[0])
        return upwardStocks

    def stockTrendIsUpward(self, fileName):
        #check if a stock in upward trended
        dataTable = pd.read_csv(fileName)
        averagePriceData = dataTable[['average']]
        for i in range(len(averagePriceData['average'])):
            if not averagePriceData['average'][i] > 0:
                if i == 0:
                    averagePriceData['average'][i] = self.getNextNonemptyValue(averagePriceData['average'])
                else:
                    averagePriceData['average'][i] = averagePriceData['average'][i - 1]
        slope = averagePriceData.apply(lambda x: numpy.polyfit(averagePriceData.index, x, 1)[0])
        return slope['average'] < 0

    def getNextNonemptyValue(self, dataArray):
        for i in dataArray:
            if i > 0:
                return i
        return 0