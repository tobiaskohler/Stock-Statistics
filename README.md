# Stock Statistics

This Python CLI calculates various descriptive statistics and risk measures for the given asset symbols. **See refer to example output below**. 

The tool leverages the [yfinance](https://pypi.org/project/yfinance/) library to obtain stock data.

## Features

- Annual mean return (in %)
- Annual volatility (in %)
- Annual semi volatility (in %)
- Minimum return (in %) and its date
- Maximum return (in %) and its date
- Minimum trading range and its date
- Maximum trading range and its date
- Kurtosis
- Skewness
- Value-at-Risk at different quantiles (0.001, 0.01, 0.05)
- Conditional Value-at-Risk at different quantiles (0.001, 0.01, 0.05)
- Maximum drawdown (daily)

## Parameters

- symbols: *List* of strings. Stock symbols for which statistics should be calculated. Could be one or more.
- start: *String* in YYYY-MM-DD format. Start date of the period for which statistics should to be calculated (**optional**)
- end: *String* in YYYY-MM-DD format. End date of the period for which statistics should to be calculated (**optional**)
- picture: *Boolean*. Whether or not to plot the maximum drawdown (optional, default is False)
- markdown: *Boolean*. Whether or not to output the statistics in markdown format (optional, default is True)


Utilize `-h` flag to get more infos on usage.

## Example

Show statistics for *AAPL*, *GOOG* and *TSLA* stock, use longest available data, .txt output is ready-to-use for embedding in Markdown files:

```Bash
> init.py -s AAPL GOOG TSLA -d True 
```

**Output**

.png and .html files are saved in *output/* subfolder:

![Example 1 - Output (.png and .html available)](/GOOG_statistics_2004-08-19-2023-01-31_True.png)



|                                  | AAPL                    | GOOG                    | TSLA                    |
|:---------------------------------|:------------------------|:------------------------|:------------------------|
| Period                           | 1980-12-12 - 2023-02-01 | 2004-08-19 - 2023-01-31 | 2010-06-29 - 2023-02-01 |
| Annual mean return (in %)        | 17.27                   | 20.01                   | 37.67                   |
| Annual volatility (in %)         | 45.54                   | 30.59                   | 57.22                   |
| Annual semi volatility (in %)    | 35.42                   | 22.04                   | 41.49                   |
| Minimum return (in %)            | -73.12                  | -12.34                  | -23.65                  |
| Date of minimum return           | 2000-09-29              | 2008-09-29              | 2020-09-08              |
| Maximum return (in %)            | 28.69                   | 18.23                   | 21.83                   |
| Date of maximum return           | 1997-08-06              | 2008-04-18              | 2013-05-09              |
| INTRADAY TRADING RANGES          |                         |                         |                         |
| Minimum trading range (in %)     | 0.0                     | 0.38                    | 0.85                    |
| Date of Min. trading range       | 1981-08-10              | 2016-08-12              | 2021-10-14              |
| Maximum trading range (in %)     | 32.94                   | 15.01                   | 39.26                   |
| Date of Max. trading range       | 1998-01-06              | 2006-02-28              | 2010-06-29              |
| Kurtosis                         | 46.77                   | 8.19                    | 5.02                    |
| Skewness                         | -1.74                   | 0.39                    | -0.04                   |
| Maximum drawdown (daily, in %)   | -80.58                  | -64.17                  | -72.97                  |
| RISK OF LOSS (daily, in %)       |                         |                         |                         |
| VaR(95.0)                        | -4.2                    | -2.86                   | -5.26                   |
| VaR(99.0)                        | -7.32                   | -5.25                   | -9.44                   |
| VaR(99.9)                        | -15.54                  | -9.21                   | -18.63                  |
| EXPECTED SHORTFALL (daily, in %) |                         |                         |                         |
| Conditional VaR(95.0)            | -6.44                   | -4.45                   | -8.31                   |
| Conditional VaR(99.0)            | -10.85                  | -7.1                    | -13.81                  |
| Conditional VaR(99.9)            | -26.19                  | -10.84                  | -21.13                  |



The maximum drawdown ("from peak to trough") is calculated based on daily log returns with a 252 days trailing window.


## Feedback & Contributions

I'd love to hear from you! 🙏 

If you have any feedback, ideas for improving the project or have found a bug , please just open an issue :)


