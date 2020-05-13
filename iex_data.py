import requests
import json
import time


token = "pk_b363f46b9c744471a5a0e1067e17ff88"
ticker = "T"

url1 = "https://cloud.iexapis.com/stable/stock/AAPL/quote?token="+token
url2 = "https://cloud.iexapis.com/stable/stock/AAPL/company?token="+token
url3 = "https://cloud.iexapis.com/stable/stock/AAPL/news/last/1?token="+token
url4 = "https://cloud.iexapis.com/stable/stock/AAPL/advanced-stats?token="+token
url5 = "https://cloud.iexapis.com/stable/stock/AAPL/price?token="+token

# response = requests.get(url4)

# data = json.loads(response.text)



# quote: inforamtion of the current trading day and 
def quote(token, ticker):
    
    url = "https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token="+token
    response = requests.get(url)
    data = json.loads(response.text)

    data = {
                'open': data['open'],
                'close': data['close'],
                'high': data['high'],
                'low': data['low'],
                'latestPrice': data['latestPrice'],
                'latestVolume': data['latestVolume'],
                'extendedPrice': data['extendedPrice'],
                'extendedChange': data['extendedChange'],
                'extendedChangePercent': data['extendedChangePercent'],
                'previousClose': data['previousClose'],
                'valueChange': data['change'],
                'changePercent': data['changePercent'],
                'avgTotalVolume': data['avgTotalVolume'],
                'marketCap': data['marketCap'],
                'peRatio': data['peRatio'],
                'week52High': data['week52High'],
                'week52Low': data['week52Low'],
                'ytdChange': data['ytdChange'],
                'isUSMarketOpen': data['isUSMarketOpen']
            }

    return data
    
    


# company: company information
def company(token,ticker):
    
    url = "https://cloud.iexapis.com/stable/stock/"+ticker+"/company?token="+token
    response = requests.get(url)
    data = json.loads(response.text)

    data = {
                'symbol': data['symbol'],
                'securityName': data['securityName'],
                'exchange': data['exchange'],
                'industry': data['industry'],
                'sector': data['sector'],
                'description': data['description'],
                'CEO': data['CEO'],
                'employees': data['employees'],
                'tags': data['tags'],
                'state': data['state'],
                'country': data['country']
            }

    return data
    

# advancedStates: stats regarding the performance and current position of the stock
def advancedStats(token,ticker):
    
    url = "https://cloud.iexapis.com/stable/stock/"+ticker+"/advanced-stats?token="+token
    response = requests.get(url)
    data = json.loads(response.text)

    data = {
                'float': data['float'],
                'avg10Volume': data['avg10Volume'],
                'avg30Volume': data['avg30Volume'],
                'ttmEPS': data['ttmEPS'],
                'sharesOutstanding': data['sharesOutstanding'],
                'nextDividendDate': data['nextDividendDate'],
                'dividendYield': data['dividendYield'],
                'nextEarningsDate': data['nextEarningsDate'],
                'exDividendDate': data['exDividendDate'],
                'beta': data['beta'],
                'EBITDA': data['EBITDA'],                                      # for income statment stats
                'revenuePerShare': data['revenuePerShare'],                    # for income statment stats
                'debtToEquity': data['debtToEquity'],                          # for balance sheet
                'profitMargin': data['profitMargin'],                          # for income statment stats
                'enterpriseValue': data['enterpriseValue'],
                'enterpriseValueToRevenue': data['enterpriseValueToRevenue'],
                'priceToSales': data['priceToSales'],
                'priceToBook': data['priceToBook'],
                'forwardPERatio': data['forwardPERatio'],
                'pegRatio': data['pegRatio'],
                'peHigh': data['peHigh'], #52 week
                'peLow': data['peLow'], #52 week
            }

    return data


# Cash Flow information
def CashFlow(token,ticker):
    
    url = "https://cloud.iexapis.com/stable/stock/"+ticker+"/cash-flow?period=annual&token="+token
    response = requests.get(url)
    data = json.loads(response.text)
    data = data['cashflow'][0]
    data = {
        "cashFlow": data["cashFlow"],
        "totalInvestingCashFlows": data["totalInvestingCashFlows"],
        "cashFlowFinancing": data["cashFlowFinancing"],
        "cashChange": data["cashChange"],
        "freeCashFlow": data["cashFlow"]+data["capitalExpenditures"]         
        }

    return data


# Balance Sheet information
def BalanceSheet(token,ticker):
    
    url = "https://cloud.iexapis.com/stable/stock/"+ticker+"/balance-sheet?period=annual&token="+token
    response = requests.get(url)
    data = json.loads(response.text)
    data = {'currentRatio': data['totalCurrentLiabilities']}
    return data



# news: news article involving the selected ticker
def news(token,ticker):
    
    url = "https://cloud.iexapis.com/stable/stock/"+ticker+"/news/last/5?token="+token
    response = requests.get(url)
    data = json.loads(response.text)
    
    urls = []
    for i in range(0,len(data)):
        urls.append(data[i]['url'])
    
    newsUrls = {'urls':urls}


    return newsUrls



# analystrecommendations: news article involving the selected ticker
def AR(token,ticker):
    
    url = "https://cloud.iexapis.com/stable/stock/"+ticker+"/recommendation-trends?token="+token
    response = requests.get(url)
    data = json.loads(response.text)

    return data




def keyStats(token,ticker):
    
    url = "https://cloud.iexapis.com/stable/stock/"+ticker+"/stats?token="+token
    response = requests.get(url)
    data = json.loads(response.text)
    
    data = {
                'sharesOutstanding': data['sharesOutstanding'],
                'ttmEPS': data['ttmEPS'],
                'ttmDividendRate': data['ttmDividendRate'],
                'nextEarningsDate': data['nextEarningsDate']        
        }

    return data



def financials(token, ticker):
    url = "https://cloud.iexapis.com/stable/stock/"+ticker+"/financials?period=annual&token="+token
    response = requests.get(url)
    data = json.loads(response.text)
    
    data = data['financials'][0]
    
    IS = {
            'totalRevenue': data['totalRevenue'],
            'grossProfit': data['grossProfit'],
            'operatingIncome': data['operatingIncome'],
            'netIncome': data['netIncome'],
            'operatingMargin': (data['operatingIncome']/data['totalRevenue'])*100,
            'grossProfitMargin': (data['grossProfit']/data['totalRevenue'])*100,
        }
    
    BS = {
            'currentRatio': data["currentAssets"]/data["currentDebt"],
            "totalCash": data["totalCash"],
            "totalDebt": data["totalDebt"],
            "shareholderEquity": data["shareholderEquity"]
        }
    
    return IS, BS






# symbols: symbols supported by IEX
def symbols(token):
    
    url = "https://cloud.iexapis.com/stable/ref-data/symbols?token="+token
    response = requests.get(url)
    data = json.loads(response.text)
    
    stocks = []
    for i in range(0,len(data)):
        if data[i]['type'] == 'cs':
            stocks.append([data[i]['symbol'],data[i]['name'],data[i]['exchange']])
    
    return stocks




# symbols: symbols supported by IEX
def internationalExchanges(token):
    
    url = "https://cloud.iexapis.com/stable/ref-data/exchanges?token="+token
    response = requests.get(url)
    data = json.loads(response.text)
    
    # stocks = []
    # for i in range(0,len(data)):
    #     if data[i]['type'] == 'cs':
    #         stocks.append([data[i]['symbol'],data[i]['name'],data[i]['exchange']])
    return data




# symbols: symbols supported by IEX
def internationalSymbols(token, region):
    
    url = "https://cloud.iexapis.com/stable/ref-data/region/"+region+"/symbols?token="+token
    response = requests.get(url)
    data = json.loads(response.text)
    
    # stocks = []
    # for i in range(0,len(data)):
    #     if data[i]['type'] == 'cs':
    #         stocks.append([data[i]['symbol'],data[i]['name'],data[i]['exchange']])
    return data



def intradayPrices(token, ticker):
    
    url = "https://cloud.iexapis.com/stable/stock/"+ticker+"/intraday-prices?token="+token
    response = requests.get(url)
    data = json.loads(response.text)
    
    # stocks = []
    # for i in range(0,len(data)):
    #     if data[i]['type'] == 'cs':
    #         stocks.append([data[i]['symbol'],data[i]['name'],data[i]['exchange']])
    return data

def historicalPrices(token, ticker):
    
    url = "https://cloud.iexapis.com/stable/stock/"+ticker+"/chart/5dm?token="+token
    response = requests.get(url)
    data = json.loads(response.text)
    
    # stocks = []
    # for i in range(0,len(data)):
    #     if data[i]['type'] == 'cs':
    #         stocks.append([data[i]['symbol'],data[i]['name'],data[i]['exchange']])
    return data

# data = company(token,ticker)
# data = advancedStats(token, ticker)    
# time1 = time.time()
# data = quote(token, ticker)  
# time2 = time.time() 
# print(time2-time1)
# data = news(token, ticker) 
# data = symbols(token)    
# data = internationalExchanges(token)
# data = internationalSymbols(token, 'BE')
# data = AR(token, ticker)
# data = CashFlow(token, ticker)
# data = keyStats(token, ticker)
# data = financials(token, ticker)
# data = CashFlow(token, ticker)
# data = BalanceSheet(token, ticker)
time1 = time.time()
data = historicalPrices(token, ticker)
time2 = time.time() 
print(time2-time1)
# print(data)

# for i in data:
#     print()
#     print(i)

    
    
    