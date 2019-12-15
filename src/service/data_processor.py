from util.logger import Logger
import config.config as config
import os
import pandas as pd
from datetime import datetime, timedelta
from iexfinance.stocks import get_historical_intraday

class DataProcessor:

    def __init__(self, mainDirectory):
        os.environ['IEX_TOKEN'] = config.IEX_TOKEN
        global logger
        logger = Logger(mainDirectory + '\logs')
        global resourcesDirectory
        resourcesDirectory = mainDirectory + '\\resources\historical_data'

    def extractStockHistoricalData(self, stocks, endDate, daysback):
        #extract minute stock data for a period of time. parameter stocks is a list of stock symbols
        try:
            date = endDate
            for stock in stocks:
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
                fileName = '%s\%s_%i_days_ended_on_%s.csv' %(resourcesDirectory, stock, daysback, str(endDate.date()))
                historicalData.to_csv(fileName)
                # TODO: call the uploadDataToS3() method
                logger.logInfo('Data for ' + stock + ' is saved in ' + fileName)
        except Exception as ex:
            logger.logError('Error extracting stock data. Error: ' + ex)

    def uploadDataToS3(self):
        # TODO: update the data to aws s3 bucket
        pass

    #TODO: add method to analyze the data