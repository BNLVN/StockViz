import datetime as dt
from matplotlib import colors
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc
# customizations
import colorama
from colorama import Fore
from colorama import Style

#time interval (start_date-end_date)
company = input('enter the company symbol(eg: TSLA) : ')
print("Enter time in this format yyyy-mm-dd")

years = input('%s enter the year to start:%s '%(Fore.BLUE,Style.RESET_ALL))
months = input('%s enter the month:%s '%(Fore.BLUE,Style.RESET_ALL))
days = input('%s enter the year to start:%s '%(Fore.BLUE,Style.RESET_ALL))

start_date = dt.datetime(int(years),int(months),int(days))
end_date = dt.datetime.now()


providers = ['yahoo','quandl','fred']

for index,provider in enumerate(providers):
    index +=1
    print('%s %s %s %s'%(Fore.GREEN,index,provider,Style.RESET_ALL))

provider_input = int(input('%s choose a provider (1-3) rec[1]:%s'%(Fore.BLUE,Style.RESET_ALL)))
if provider_input < 4:
    if provider_input == 1:
            provider_api = providers[0]
    elif provider_input == 2:
            provider_api = providers[1]
    elif provider_input == 3:
            provider_api = providers[2]
else:
        print('%s plz choose a valid provider%s'%(Fore.RED,Style.RESET_ALL))
        
print('%s the data are currently provided by the %s api%s'%(Fore.YELLOW,provider_api, Style.RESET_ALL))

#Getting data

data = pdr.DataReader(company,provider_api,start_date, end_date)

#Restructuring data gotten from the api
data = data[['Open','High','Low','Close']]
data.reset_index(inplace=True)

data['Date'] = data['Date'].map(mdates.date2num)

#data plotting

ax = plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_facecolor('Black')
ax.set_title('%s share Price'%company, color = '#3C3C3C')
ax.tick_params(axis='x', colors='#1B83D0')
ax.tick_params(axis='y', colors='#1B83D0')
ax.xaxis_date()

candlestick_ohlc(ax, data.values, width=0.7, colorup='#00C642', colordown='#F53217')
plt.show()