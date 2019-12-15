class simple:
    """
    given data from last n min
    market buy if current is lower than min of history
    market sell if current is high than max of history
    else hold
    """
    def __init__(self, data):
        self.data = data
        return
        
    def result(self, n, currentPrice, currentTime):
        if currentPrice < self.historyLow(n, currentTime).min():
            return 'buy'
        elif currentPrice > self.historyHigh(n, currentTime).max():
            return 'sell'
        else:
            return 'hold'
    
    def historyHigh(self, n, currentTime):
        # return n min of historyHigh given current time
        currentIndex = self.data[self.data.time == str(currentTime)].index.tolist()[0]
        return self.data['high'].iloc[currentIndex-10 : currentIndex]
    
    def historyLow(self, n, currentTime):
        currentIndex = self.data[self.data.time == str(currentTime)].index.tolist()[0]
        return self.data['low'].iloc[currentIndex-10 : currentIndex]
