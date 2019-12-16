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
        
    def result(self, min, currentPrice, currentTime):
        if currentPrice < self.historyLow(min, currentTime).min():
            return 'buy'
        elif currentPrice > self.historyHigh(min, currentTime).max():
            return 'sell'
        else:
            return 'hold'
    
    def historyHigh(self, min, currentTime):
        # return min minutes of historyHigh given currentTime
        currentIndex = self.data[self.data.time == str(currentTime)].index.tolist()[0]
        return self.data['high'].iloc[currentIndex-min : currentIndex]
    
    def historyLow(self, min, currentTime):
        currentIndex = self.data[self.data.time == str(currentTime)].index.tolist()[0]
        return self.data['low'].iloc[currentIndex-min : currentIndex]
