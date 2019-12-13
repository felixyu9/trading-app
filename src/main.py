import config.config as config
from service.robinhood import RobinhoodService
import os

mainDirectory = str(os.path.abspath(os.path.dirname(__file__)))

def main():
    robinhoodService = RobinhoodService(config.USERNAME, config.PASSWORD, mainDirectory)
    robinhoodService.login()
    robinhoodService.listStocksInAccount()

if __name__ == '__main__':
    main()
