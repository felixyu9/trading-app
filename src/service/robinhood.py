# http://www.robin-stocks.com/en/latest/functions.html
import robin_stocks as robin
from util.logger import Logger

class RobinhoodService:

    def __init__(self, username, password, mainDirectory):
        self.username = username
        self.password = password
        self.isLogin = False
        global logger
        logger = Logger(mainDirectory + '\logs')

    def login(self):
        try:
            robin.login(self.username, self.password)
            self.isLogin = True
        except Exception as ex:
            logger.logError('Error logging into account: ' + self.username)
        else:
            logger.logInfo('Successfully logged into account: ' + self.username)

    def listStocksInAccount(self):
        if not self.isLogin:
            logger.logInfo('Please log in before listing stocks in the account.')
            return
        myStocks = robin.build_holdings()
        if len(myStocks.items()) == 0:
            logger.logInfo('This account hold 0 stocks.')
        else:
            logger.logInfo('Listing stocks:')
        for key, value in myStocks.items():
            logger.logInfo(str(key) + ':' + str(value))

    def marketBuy(self, stock, quantity):
        # submit a purchase order at market price
        try:
            response = robin.order_buy_market(stock, quantity)
            #TODO: look up what response contains and get the exact order price and log it out. same for other methods
        except Exception as ex:
            logger.logError('Unable to purchase %s with market buy. \nError: %s ' % (stock,  ex))
        else:
            logger.logInfo('Successfully purchased %i shares of %s with market buy' % (quantity, stock))

    def stopLimitBuy(self, stock, quantity, limitPrice, stopPrice):
        # submit a stop order to be turned into a limit order once a certain stop price is reached
        try:
            robin.order_buy_stop_limit(stock, quantity, limitPrice, stopPrice)
        except Exception as ex:
            logger.logError('Unable to purchase %s with stop limit buy. \nError: %s' % (stock, ex))
        else:
            logger.logInfo('Successfully purchased %i shares of %s with stop limit buy' % (quantity, stock))

    def stopLossBuy(self, stock, quantity, stopPrice):
        # submit a stop order to be turned into a market order once a certain stop price is reached.
        try:
            robin.order_buy_stop_loss(stock, quantity, stopPrice)
        except Exception as ex:
            logger.logError('Unable to purchase %s with stop loss buy. \nError: %s' % (stock, ex))
        else:
            logger.logInfo('Successfully purchased %i shares of %s with stop loss buy.' % (quantity, stock))

    def marketSell(self, stock, quantity):
        # submit a sell order at market price
        try:
            robin.order_sell_market(stock, quantity)
        except Exception as ex:
            logger.logError('Unable to sell %s with market sell. \nError: %s' % (stock, ex))
        else:
            logger.logInfo('Successfully purchased %i shares of %s with market sell' % (quantity, stock))

    def stopLimitSell(self, stock, quantity, limitPrice, stopPrice):
        # submit a stop sell order to be turned into a limit order once a certain stop price is reached
        try:
            robin.order_sell_stop_limit(stock, quantity, limitPrice, stopPrice)
        except Exception as ex:
            logger.logError('Unable to sell %s with stop limit sell. \nError: %s' % (stock, ex))
        else:
            logger.logError('Successfully sold %i shares of %s with stop limit sell.' % (quantity, stock))

    def stopLossSell(self, stock, quantity, stopPrice):
        # submit a stop sell order to be turned into a market order once a certain stop price is reached.
        try:
            robin.order_sell_stop_loss(stock, quantity, stopPrice)
        except Exception as ex:
            logger.logError('Unable to sell %s with stop loss sell. \nError: %s' % (stock, ex))
        else:
            logger.logInfo('Successfully sold %i shares of %s with stop loss sell.' % (quantity, stock))
