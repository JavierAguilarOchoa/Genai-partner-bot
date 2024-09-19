import requests
from collections import namedtuple


Sec = namedtuple('Sec', ['name', 'ticker', 'cik_id'])

class SecEdgar:
    def __init__(self, fileurl) -> None:
        self.fileurl = fileurl
        self.name_dict = {}
        self.ticker_dict = {}
        self.cik_dict = {}

        headers = {'user-agent': 'MLT aguilarjaviii14@gmail.com'}
        response = requests.get(self.fileurl, headers = headers)

        self.filejson = response.json()
        self.cik_json_to_dict()

    def cik_json_to_dict(self):
        for _, value in self.filejson.items():
            cik_id = value["cik_str"]
            company_name = value["title"]
            ticker = value["ticker"]

            self.name_dict[company_name] = cik_id
            self.ticker_dict[ticker] = cik_id
            self.cik_dict[cik_id] = (company_name, ticker)


    def name_to_cik(self,name:str) -> list[tuple[str, int]]:
        if name not in self.name_dict:
            raise BaseException("Name was not found in dictionary")
        
        cik_id = self.name_dict[name]
        _, ticker = self.cik_dict[cik_id]

        return Sec(name=name, ticker=ticker, cik_id = cik_id)
        
    def ticker_to_cik(self, ticker) -> list[tuple[str, int]]:
        if ticker not in self.ticker_dict:
            raise BaseException("Ticker was not found in dictionary")
        
        cik_id = self.ticker_dict[ticker]
        company_name, _ = self.cik_dict[cik_id]
        
        return Sec(name=company_name, ticker=ticker, cik_id=cik_id)
        

if __name__ == "__main__":
    se = SecEdgar('https://www.sec.gov/files/company_tickers.json')

    print(se.name_to_cik('Apple Inc.'))

    print(se.ticker_to_cik('META'))


        