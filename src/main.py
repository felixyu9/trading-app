import config.config as config
from service.robinhood import RobinhoodService

def main():
    robinhoodService = RobinhoodService(config.USERNAME, config.PASSWORD)
    robinhoodService.login()
    robinhoodService.listStocksInAccount()

if __name__ == '__main__':
    main()
