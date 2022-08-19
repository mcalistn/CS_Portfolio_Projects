# ################################################################################################################ #
# Imports                                                                                                          #
# ################################################################################################################ #
import time
import yfinance
import pandas
import pandas_datareader
import datetime
import numpy
import matplotlib.pyplot
import csv
import json


# ################################################################################################################ #
# validateYN()                                                                                                     #
#                                                                                                                  #
# Description - Helper function that validates that a user's input is either a 'y' or 'n'                          #
# Params:                                                                                                          #
#       1) userInput - user's input to a y/n question                                                              #
# Returns - Returns 'True' if the response was a 'y' or 'n'; otherwise returns 'False                              #
# ################################################################################################################ #
def validateYN(userInput):
    if (userInput == 'y') or (userInput == 'n'):
        return True
    else:
        print("Please enter either 'y' or 'n'.")
        return False


# ################################################################################################################ #
# validateDate()                                                                                                   #
#                                                                                                                  #
# Description - Helper function that validates that a user's inputted date is in the correct format                #
# Params:                                                                                                          #
#       1) userDate - user's inputted date                                                                         #
# Returns - Returns 'True' if the date has the correct format; otherwise returns 'False                            #
# ################################################################################################################ #
def validateDate(userDate):
    try:
        datetime.datetime.strptime(userDate, "%m/%d/%Y")
        return True
    except ValueError:
        print("Incorrect date format. Please enter date as MM/DD/YYYY")
        return False


# ################################################################################################################ #
# stockSearch()                                                                                                    #
#                                                                                                                  #
# Description - Searches a CSV reference file for a company name and returns the associated stock ticker. If no    #
#               company name is found, the user will be presented with the option to add a custom stock ticker to  #
#               the CSV reference file.                                                                            #
# Returns - Returns the stock ticker associated with the company name                                              #
# ################################################################################################################ #
def stockSearch():
    companyValid = False
    choiceValid = False

    while not companyValid:
        companyName = input("Enter company name to search: ")
        # Search company name in the CSV reference document.
        csvFile = csv.reader(open('../reference/stock-ticker-lookup.csv', "r"), delimiter=",")
        count = 0
        stockArr = []
        for row in csvFile:
            if companyName.upper() in row[1].upper():
                stockArr.append(row)
                count += 1
        # If the searched company name returns more than 5 entries, the user's request is denied.
        if count > 5:
            print("Too many companies listed. Please narrow your search by "
                  "being more specific with the company name.")
        # If the searched company name returns multiple names, but less than 5 names, the user
        # will select the appropriate company from a list of companies.
        elif 5 >= count > 1:
            print("\nMultiple companies found... ")
            i = 0
            for element in stockArr:
                print("\t" + str(i + 1) + ") " + str(element))
                i += 1
            while not choiceValid:
                companyChoice = input("\nPlease choose the company you wish to analyze "
                                      "(Enter 1 - " + str(i) + "): ")
                if i + 1 >= int(companyChoice) > 0:
                    choiceValid = True
                    tickerSymbol = stockArr[int(companyChoice) - 1][0]
                else:
                    print("Please enter a number inside the query range.")
            companyValid = True
        # If there is only one return value for the searched company name.
        elif count == 1:
            companyChoice = 1
            tickerSymbol = stockArr[int(companyChoice) - 1][0]
            companyValid = True
        # If there are no company names returned from the search the user will be asked to create a custom
        # stock ticker.
        else:
            tickerSymbol = addNewStock()
            if tickerSymbol != "":
                companyValid = True
    print("Ticker symbol: " + tickerSymbol + "\n")

    return tickerSymbol


# ################################################################################################################ #
# addNewStock()                                                                                                    #
#                                                                                                                  #
# Description - The user's inputted company name is not found in the CSV reference file. The user is given an      #
#               opportunity to add a custom stock to the reference file that can be used to search for the company #
#               in the future.  User will have to find the company's stock ticker online one time during the       #
#               initial set-up of the stock ticker.                                                                #
# Returns - Returns the stock ticker associated with the newly created company name                                #
# ################################################################################################################ #
def addNewStock():
    companyAddValid = False
    addFilePath = "../inputs/add.csv"
    inputFilePath = "../inputs/inputs.txt"
    outputFilePath = "../outputs/output.json"
    archiveFilePath = "../reference/stock-ticker-lookup.csv"
    while not companyAddValid:
        companyAdd = input("Company not found. Would you like to add a custom stock? (y/n) ")
        companyAdd = companyAdd.lower()
        companyAddValid = validateYN(companyAdd)
    # Adds new company name and stock ticker to the CSV reference sheet.
    if companyAdd == 'y':
        print("You will need to provide the company name and stock ticker for the company you\n wish to add. "
              "You will not have to look-up these values again after they are added to the\n reference documentation.")
        companyNameAdd = input("Please enter the company name: ")
        companyStockTickerAdd = input("Please enter the companies stock ticker: ")
        open(addFilePath, 'w').close()
        open(addFilePath, 'w').writelines(["Symbol,Name\n", companyStockTickerAdd, ",", companyNameAdd])
        open(inputFilePath, 'w').close()
        open(inputFilePath, 'w').write("./inputs/add.csv")
        time.sleep(2)
        open(inputFilePath, 'w').close()
        JSONdata = json.load(open(outputFilePath))
        open(archiveFilePath, 'a').writelines(["\n", str(JSONdata[0]["Symbol"]), ",", str(JSONdata[0]["Name"])])
        return companyStockTickerAdd
    else:
        return ""


# ################################################################################################################ #
# getStockTicker()                                                                                                 #
#                                                                                                                  #
# Description - Asks user if the user wants to search for a company's stock ticker by entering a company's name    #
#               or by entering a company's stock ticker directly.                                                  #
# Returns - Returns the company's stock ticker                                                                     #
# ################################################################################################################ #
def getStockTicker():
    searchValid = False

    while not searchValid:
        stockSearchOpen = input("\nDo you want to search for a stock ticker? (y/n) ")
        stockSearchOpen = stockSearchOpen.lower()
        searchValid = validateYN(stockSearchOpen)
    # Search for the company by name
    if stockSearchOpen == 'y':
        tickerSymbol = stockSearch()
    # Search for the company by stock ticker
    else:
        tickerSymbol = input("Enter stock ticker: ")
        tickerSymbol = tickerSymbol.upper()

    return tickerSymbol


# ################################################################################################################ #
# getDateRange()                                                                                                   #
#                                                                                                                  #
# Description - Gathers the date range the user wishes to search for when looking up their stock information.      #
# Returns - The inputted date in an array [month, day, year]                                                       #
# ################################################################################################################ #
def getDateRange():
    dateValid = False

    while not dateValid:
        startDate = input("Please input the start date for the data retrieval. (MM/DD/YYYY): ")
        dateValid = validateDate(startDate)
    month = startDate[0:2:1]
    day = startDate[3:5:1]
    year = startDate[6:10:1]
    dateArr = [month, day, year]

    return dateArr


# ################################################################################################################ #
# getRawStockData()                                                                                                #
#                                                                                                                  #
# Description - Uses the yfinance API (yahoo financed based API) to gather all stock information (stock price,     #
#               etc.) on the user inputted stock                                                                   #
# Params:                                                                                                          #
#       1) tickerSymbol - The user inputted company's stock ticker symbol                                          #
#       2) dateArr - Date array that contains the user inputted date range [month, day, year]                      #
# Returns - Data array that contains all of the statistical data for the user inputted stock ticker and within the #
#           given data range                                                                                       #
# ################################################################################################################ #
def getRawStockData(tickerSymbol, dateArr):
    tickerData = yfinance.Ticker(tickerSymbol)
    tickerStatistics = tickerData.stats()
    print("\nCurrent stock price: '" + tickerSymbol + "' = " + str(
        tickerStatistics['price']['regularMarketPrice']))
    now = datetime.datetime.now()
    startDate = datetime.datetime(int(dateArr[2]), int(dateArr[0]), int(dateArr[1]))
    rawData = pandas_datareader.get_data_yahoo(tickerSymbol, startDate, now)

    return rawData


# ################################################################################################################ #
# updateColumns()                                                                                                  #
#                                                                                                                  #
# Description - Adds additional columns to the rawData array that will be used for the technical analysis          #
#               calculations                                                                                       #
# Params:                                                                                                          #
#       1) rawData - Data array that contains all of the statistical data for the user inputted stock ticker and   #
#                    within the given data range                                                                   #
# Returns - Updated data array that contains all additional columns necessary to perform technical analysis        #
#           of the stock                                                                                           #
# ################################################################################################################ #
def updateColumns(rawData):
    rawData['Uptick'] = numpy.nan
    rawData['Downtick'] = numpy.nan
    rawData['Average Uptick'] = numpy.nan
    rawData['Average Downtick'] = numpy.nan
    rawData['On-Balance Volume'] = numpy.nan
    rawData['RS'] = numpy.nan
    rawData['RSI'] = numpy.nan
    rawData['Short EMA'] = numpy.nan
    rawData['Long EMA'] = numpy.nan
    rawData['MACD'] = numpy.nan
    rawData['Signal'] = numpy.nan

    return rawData


# ################################################################################################################ #
# calculateUpDownTicks()                                                                                           #
#                                                                                                                  #
# Description - Calculates the up/down ticks (positive/negative price movement) for each day within the            #
#               rawData array.                                                                                     #
# Params:                                                                                                          #
#       1) rawData - Data array that contains all of the statistical data for the user inputted stock ticker and   #
#                    within the given data range                                                                   #
# Returns - Updated data array that contains all of the positive and negative price movement data for each day     #
# ################################################################################################################ #
def calculateUpDownTicks(rawData):
    for i in range(1, len(rawData)):
        rawData['Uptick'][i] = 0
        rawData['Downtick'][i] = 0
        if rawData['Adj Close'][i] > rawData['Adj Close'][i - 1]:
            rawData['Uptick'][i] = rawData['Adj Close'][i] - rawData['Adj Close'][i - 1]
        if rawData['Adj Close'][i] < rawData['Adj Close'][i - 1]:
            rawData['Downtick'][i] = abs(rawData['Adj Close'][i] - rawData['Adj Close'][i - 1])

    return rawData


# ################################################################################################################ #
# calculateOnBalanceVolume()                                                                                       #
#                                                                                                                  #
# Description - Calculates the on-balance volume (OBV) for each day within the rawData array.                      #
# Params:                                                                                                          #
#       1) rawData - Data array that contains all of the statistical data for the user inputted stock ticker and   #
#                    within the given data range                                                                   #
# Returns - Updated data array that contains all of the OBV data for each day                                      #
# ################################################################################################################ #
def calculateOnBalanceVolume(rawData):

    rawData['On-Balance Volume'][0] = 0
    for i in range(1, len(rawData)):
        if rawData['Open'][i] < rawData['Close'][i]:
            rawData['On-Balance Volume'][i] = rawData['On-Balance Volume'][i - 1] + rawData['Volume'][i]
        elif rawData['Open'][i] > rawData['Close'][i]:
            rawData['On-Balance Volume'][i] = rawData['On-Balance Volume'][i - 1] - rawData['Volume'][i]
        else:
            rawData['On-Balance Volume'][i] = rawData['On-Balance Volume'][i - 1]

    return rawData


# ################################################################################################################ #
# calculateRSI()                                                                                                   #
#                                                                                                                  #
# Description - Calculates the relative strength index (RSI) for each day within the rawData array.                #
# Params:                                                                                                          #
#       1) rawData - Data array that contains all of the statistical data for the user inputted stock ticker and   #
#                    within the given data range                                                                   #
# Returns - Updated data array that contains all of the RSI data for each day                                      #
# ################################################################################################################ #
def calculateRSI(rawData):

    rawData['Average Uptick'][14] = rawData['Uptick'][1:15].mean()
    rawData['Average Downtick'][14] = rawData['Downtick'][1:15].mean()
    rawData['RS'][14] = rawData['Average Uptick'][14] / rawData['Average Downtick'][14]
    rawData['RSI'][14] = 100 - (100 / (1 + rawData['RS'][14]))
    for i in range(15, len(rawData)):
        rawData['Average Uptick'][i] = ((13 * rawData['Average Uptick'][i - 1]) + (rawData['Uptick'][i])) / 14
        rawData['Average Downtick'][i] = ((13 * rawData['Average Downtick'][i - 1]) + (rawData['Downtick'][i])) / 14
        rawData['RS'][i] = rawData['Average Uptick'][i] / rawData['Average Downtick'][i]
        rawData['RSI'][i] = 100 - (100 / (1 + rawData['RS'][i]))

    return rawData


# ################################################################################################################ #
# calculateMACD()                                                                                                  #
#                                                                                                                  #
# Description - Calculates the Moving Average Convergence Divergence (MACD) for each day within the rawData array. #
# Params:                                                                                                          #
#       1) rawData - Data array that contains all of the statistical data for the user inputted stock ticker and   #
#                    within the given data range                                                                   #
# Returns - Updated data array that contains all of the MACD data for each day                                     #
# ################################################################################################################ #
def calculateMACD(rawData):

    rawData['Short EMA'] = rawData['Close'].ewm(span=12, adjust=False).mean()
    rawData['Long EMA'] = rawData['Close'].ewm(span=26, adjust=False).mean()
    rawData['MACD'] = rawData['Short EMA'] - rawData['Long EMA']
    rawData['Signal'] = rawData['MACD'].ewm(span=9, adjust=False).mean()

    return rawData


# ################################################################################################################ #
# giveOverallRecommendation()                                                                                      #
#                                                                                                                  #
# Description - Gives overall recommendation (BUY/HOLD/SELL) for the user inputted stock.                          #
# Params:                                                                                                          #
#       1) rawData - Data array that contains all of the statistical data for the user inputted stock ticker and   #
#                    within the given data range                                                                   #
# ################################################################################################################ #
def giveOverallRecommendation(rawData):
    overallRecommendation = 0

    if rawData['On-Balance Volume'][len(rawData) - 1] >= 0:
        overallRecommendation += 1
    else:
        overallRecommendation -= 1
    if rawData['RSI'][len(rawData) - 1] > 70:
        overallRecommendation -= 1
    elif rawData['RSI'][len(rawData) - 1] < 30:
        overallRecommendation += 1
    if rawData['MACD'][len(rawData) - 1] > rawData['Signal'][len(rawData) - 1]:
        overallRecommendation += 1
    else:
        overallRecommendation -= 1
    if overallRecommendation > 0:
        print("\nOverall Recommendation: BUY!!!")
    elif overallRecommendation < 0:
        print("\nOverall Recommendation: SELL!!!")
    else:
        print("\nOverall Recommendation: HOLD!!!")


# ################################################################################################################ #
# giveDetailedRecommendation()                                                                                     #
#                                                                                                                  #
# Description - Gives detailed recommendation (BUY/HOLD/SELL) for each technical indicator.                        #
# Params:                                                                                                          #
#       1) rawData - Data array that contains all of the statistical data for the user inputted stock ticker and   #
#                    within the given data range                                                                   #
# ################################################################################################################ #
def giveDetailedRecommendation(rawData):
    detailsValid = False

    while not detailsValid:
        detailsDisplay = input("\nDo you want to see the details of the recommendations? This will display "
                               "detailed technical information  (y/n) ")
        detailsDisplay = detailsDisplay.lower()
        detailsValid = validateYN(detailsDisplay)
    if detailsDisplay == 'y':
        # Get OBV recommendation
        if rawData['On-Balance Volume'][len(rawData) - 1] >= 0:
            OBV_Value = "Positive"
            OBV_recommendation = "BUY"
        else:
            OBV_Value = "Negative"
            OBV_recommendation = "SELL"
        RSI_Value = rawData['RSI'][len(rawData) - 1]
        MACD_Value = rawData['MACD'][len(rawData) - 1]
        Signal_Value = rawData['Signal'][len(rawData) - 1]
        # Get RSI recommendation
        if rawData['RSI'][len(rawData) - 1] > 70:
            RSI_recommendation = "SELL"
        elif rawData['RSI'][len(rawData) - 1] < 30:
            RSI_recommendation = "BUY"
        else:
            RSI_recommendation = "HOLD"
        # Get MACD recommendation
        if rawData['MACD'][len(rawData) - 1] > rawData['Signal'][len(rawData) - 1]:
            MACD_recommendation = "BUY"
        else:
            MACD_recommendation = "SELL"
        # Print a formatted table of recommendations
        print()
        print("---------------------------------------------------------")
        print("|\tIndicator\t|\t\tValue\t\t|\tRecommendation\t|")
        print("---------------------------------------------------------")
        if OBV_Value == "Positive":
            print("|\t\tOBV\t\t|\t" + OBV_Value + "\t\t|\t\t" + OBV_recommendation + "\t\t\t|")
        else:
            print("|\t\tOBV\t\t|\t" + OBV_Value + "\t\t|\t\t" + OBV_recommendation + "\t\t|")
        print("---------------------------------------------------------")
        print("|\t\tRSI\t\t|\t\t" + str(int(RSI_Value)) + "\t\t\t|\t\t" + RSI_recommendation + "\t\t|")
        print("---------------------------------------------------------")
        if len(str(int(MACD_Value))) + len(str(int(Signal_Value))) + 3 < 8:
            print("| MACD / Signal |\t" + str(int(MACD_Value)) + " / " + str(
                int(Signal_Value)) + "\t\t\t", end="")
        else:
            print("| MACD / Signal |\t" + str(int(MACD_Value)) + " / " + str(
                int(Signal_Value)) + "\t\t", end="")
        if MACD_recommendation == "BUY":
            print("|\t\t" + MACD_recommendation + "\t\t\t|")
        else:
            print("|\t\t" + MACD_recommendation + "\t\t|")

        print("---------------------------------------------------------")
        print()


# ################################################################################################################ #
# documentDetails()                                                                                                #
#                                                                                                                  #
# Description - Prints all technical analysis data in rawData data array to an output file.                        #
# Params:                                                                                                          #
#       1) rawData - Data array that contains all of the statistical data for the user inputted stock ticker and   #
#                    within the given data range                                                                   #
# ################################################################################################################ #
def documentDetails(rawData):
    detailsValid = False
    rawData_txt_FP = '../outputs/rawData.txt'

    while not detailsValid:
        detailDisplay = input(
            "Do you want to store the data in an output file? \nThis will save all of the data to\n'" +
            rawData_txt_FP + "' (y/n) ")
        detailDisplay = detailDisplay.lower()
        detailsValid = validateYN(detailDisplay)
    if detailDisplay == 'y':
        open(rawData_txt_FP, 'w').close()
        open(rawData_txt_FP, 'w').write(rawData.to_string())


# ################################################################################################################ #
# plotData()                                                                                                       #
#                                                                                                                  #
# Description - Plots all of the technical analysis indicator data on a single graph.                              #
# Params:                                                                                                          #
#       1) tickerSymbol - The user inputted company's stock ticker symbol                                          #
#       2) rawData - Data array that contains all of the statistical data for the user inputted stock ticker and   #
#                    within the given data range                                                                   #
# ################################################################################################################ #
def plotData(tickerSymbol, rawData):
    plotValid = False

    while not plotValid:
        plotDisplay = input("\nDo you want to display the data graphically?  (y/n) ")
        plotDisplay = plotDisplay.lower()
        plotValid = validateYN(plotDisplay)
    if plotDisplay == 'y':
        matplotlib.pyplot.style.use('default')
        figure, axis = matplotlib.pyplot.subplots(4, sharex='col', figsize=(12, 10))
        figure.suptitle(tickerSymbol + ' Technical Analysis Graphs')
        axis[0].plot(rawData['Adj Close'])
        axis[0].set_ylabel('Adj. Closing Price, $')
        axis[1].plot(rawData['On-Balance Volume'])
        axis[1].set_ylabel('On-Balance Volume')
        axis[2].plot(rawData['RSI'])
        axis[2].set_ylabel('RSI')
        axis[3].plot(rawData['MACD'], label='MACD')
        axis[3].plot(rawData['Signal'], label='Signal')
        axis[3].legend(loc='upper right')
        axis[3].set_ylabel('MACD')
        axis[0].grid(True)
        axis[1].grid(True)
        axis[2].grid(True)
        axis[3].grid(True)
        matplotlib.pyplot.show()

# ################################################################################################################ #
# Main                                                                                                             #
# ################################################################################################################ #
def main():
    # Set panda settings
    pandas.set_option('display.max_columns', None)
    pandas.set_option('display.max_rows', None)
    pandas.options.mode.chained_assignment = None

    # Get user input
    tickerSymbol = getStockTicker()
    dateArr = getDateRange()

    # Calculate stock technical analysis indicator data
    print("\nGathering data for '" + tickerSymbol + "' from '" + dateArr[0] + "/" + dateArr[1] + "/" + dateArr[2] +
          "' Please wait...")
    rawData = getRawStockData(tickerSymbol, dateArr)
    rawData = updateColumns(rawData)
    rawData = calculateUpDownTicks(rawData)
    rawData = calculateOnBalanceVolume(rawData)
    rawData = calculateRSI(rawData)
    rawData = calculateMACD(rawData)

    # Print/Plot the results of the technical analysis indicators
    giveOverallRecommendation(rawData)
    giveDetailedRecommendation(rawData)
    documentDetails(rawData)
    plotData(tickerSymbol, rawData)


if __name__ == '__main__':
    main()

# Citations
# Andersen, S. (2020, December 29). Momentum trading with MACD and RSI - yfinance &amp; python. Medium.
#       Retrieved April 25, 2022, from https://medium.com/analytics-vidhya/momentum-trading-with-macd-and-rsi-yfinance
#       -python-e5203d2e1a8a

# Shadmehry, C. (2021, August 11). How to calculate on-balance volume (OBV) using Python. Medium. Retrieved May 30,
#       2022, from https://medium.com/automated-trading/how-to-calculate-on-balance-volume-obv-using-python-
#       4f26fdc7969d
