I will add severeal python scripts to this repository. The purpose and functionality of the scripts range from simple conversion scripts
to scripts used for some stock analysis. I primarily use the pandas, matplotlib, sympy, and numpy libraries to accomplish the intent
of the script. 

You'll notice a lot of suppressed code in my .py files; this is a bad habit of mine but I have an irrational fear of deleting bits 
of code and needing to reference it later.




stockpandas.py uses the pandas and pandas_datareader.data.DataReader function to pull stock data from the Yahoo Finance API, more info 
in the following link http://pandas.pydata.org/pandas-docs/version/0.15.2/remote_data.html#remote-data-yahoo

DataReader pulls Open, High, Low, Close, Volume, and Adj Close, but I am using Adj Close and Volume for this project.

I used matplotlib to graph the volume and Adj Close values each day. I regress the Adj Close data to a 4th degree polynomial and 
output a best fit 4th degree polynomial line (this was meant to predict trends in the stock but proved to be unhelpful).

I compare the Adj Close value of the previous day to the average of the last 10 days to examine the general trend of the stock. 

This is about as far as I've gotten with this project as it is one I work on in spare time. Any and all comments are welcome.
