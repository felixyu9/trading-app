import robin_stocks as robin


class RobinhoodService:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.isLogin = False

    def login(self):
        try:
            robin.login(self.username, self.password)
            self.isLogin = True
        except Exception as ex:
            print('Error logging into account: ' + self.username)
        else:
            print('Successfully logged into account: ' + self.username)

    def listStocksInAccount(self):
        if not self.isLogin:
            print('Please log in before listing stocks in the account.')
            return
        myStocks = robin.build_holdings()
        if len(myStocks.items()) == 0:
            print('This account hold 0 stocks.')
        else:
            print('Listing stocks:')
        for key, value in myStocks.items():
            print(key, value)

    def buyMarket(self, stock, quantity):
        # submit a purchase order at market price
        try:
            robin.order_buy_market(stock, quantity)
        except Exception as ex:
            print('Unable to purchase %s with market buy. \nError: %s ' % (stock,  ex))
        else:
            print('Successfully purchased %i shares of %s with market buy' % (quantity, stock))

    def buyStopLimit(self, stock, quantity, limitPrice, stopPrice):
        # submit a stop order to be turned into a limit order once a certain stop price is reached
        try:
            robin.order_buy_stop_limit(stock, quantity, limitPrice, stopPrice)
        except Exception as ex:
            print('Unable to purchase %s with stop limit buy. \nError: %s' % (stock, ex))
        else:
            print('Successfully purchased %i shares of %s with stop limit buy' % (quantity, stock))

    def buyStopLoss(self, stock, quantity, stopPrice):
        # submit a stop order to be turned into a market order once a certain stop price is reached.
        try:
            robin.order_buy_stop_loss(stock, quantity, stopPrice)
        except Exception as ex:
            print('Unable to purchase %s with stop loss buy. \nError: %s' % (stock, ex))
        else:
            print('Successfully purchased %i shares of %s with stop loss buy.' % (quantity, stock))

    def sellMarket(self, stock, quantity):
        # submit a sell order at market price
        try:
            robin.order_sell_market(stock, quantity)
        except Exception as ex:
            print('Unable to sell %s with market sell. \nError: %s' % (stock, ex))
        else:
            print('Successfully purchased %i shares of %s with market sell' % (quantity, stock))

    def sellStopLimit(self, stock, quantity, limitPrice, stopPrice):
        # submit a stop sell order to be turned into a limit order once a certain stop price is reached
        try:
            robin.order_sell_stop_limit(stock, quantity, limitPrice, stopPrice)
        except Exception as ex:
            print('Unable to sell %s with stop limit sell. \nError: %s' % (stock, ex))
        else:
            print('Successfully sold %i shares of %s with stop limit sell.' % (quantity, stock))

    def sellStopLoss(self, stock, quantity, stopPrice):
        # submit a stop sell order to be turned into a market order once a certain stop price is reached.
        try:
            robin.order_sell_stop_loss(stock, quantity, stopPrice)
        except Exception as ex:
            print('Unable to sell %s with stop loss sell. \nError: %s' % (stock, ex))
        else:
            print('Successfully sold %i shares of %s with stop loss sell.' % (quantity, stock))
