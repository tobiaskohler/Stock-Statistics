import yfinance as yf
import numpy as np
import pandas as pd
import math
import os
import traceback
from maximumDrawdown import calculate_max_drawdown


def calculate_stats(symbols, start=None, end=None, picture=False, markdown=True) -> None:
    
    try: 
        
        stats = []
        
        for symbol in symbols:
            
            ticker = yf.Ticker(symbol)
            
            if start and end:
                df = ticker.history(start=start, end=end)
                
            else:
                df = ticker.history(period="max")
                        
            df.dropna(inplace=True)

            df["log_returns"] = np.log(df["Close"]) - np.log(df["Close"].shift(1))
            df["trading_range"] = (df["High"] - df["Low"]) / df["Open"]
            
            first_date = df.index[0].strftime("%Y-%m-%d")
            end = df.index[-1].strftime("%Y-%m-%d")
            
            ## Descripitve statistics
            
            mean = df["log_returns"].mean()
            volatility = df["log_returns"].std()
            
            #semi_volatility
            negative_returns = df[df["log_returns"] < mean]
            semi_volatility = negative_returns["log_returns"].std()
            
            annualized_mean = round(mean * 252 * 100, 2)
            annualized_volatility = round(volatility * math.sqrt(252) * 100, 2)
            annualized_semi_volatility = round(semi_volatility * math.sqrt(252) * 100, 2)

            
            min_ret = df["log_returns"].min()
            min_ret_date = df[df['log_returns'] == min_ret].index[0].strftime("%Y-%m-%d")
            
            max_ret = df["log_returns"].max()
            max_ret_date = df[df['log_returns'] == max_ret].index[0].strftime("%Y-%m-%d")
            
            min_trading_range = df["trading_range"].min()
            min_trading_range_date = df[df['trading_range'] == min_trading_range].index[0].strftime("%Y-%m-%d")
            
            max_trading_range = df["trading_range"].max()
            max_trading_range_date = df[df['trading_range'] == max_trading_range].index[0].strftime("%Y-%m-%d")
            
            kurtosis = round(df["log_returns"].kurtosis(), 2)
            skewness = round(df["log_returns"].skew(), 2)

            
            ## Value-at-Risk calculations
            
            # Calculate the Value at Risk at the xth quantile
            quantiles = [0.001, 0.01, 0.05] 
            
            var_dict = {}
            
            for q in quantiles:
                var = df['log_returns'].quantile(q)
                print(var)
                var_dict[q] = f"{round(var * 100, 2)}"
                
            print("#########")
            print(df['log_returns'].quantile(0.05))
            # Calculate the Conditional Value at Risk at the xth quantile
            cvar_dict = {}
            
            for q in quantiles:
                cvar = df[df['log_returns'] <= df['log_returns'].quantile(q)]['log_returns'].mean()
                cvar_dict[q] = f"{round(cvar * 100, 2)}"
                
            ### Maximum drawdown (daily)
            max_drawdown = calculate_max_drawdown(symbol, first_date, end, df, picture)
            
            stats.append({
                'Symbol': symbol,
                'Period': f'{first_date} - {end}',
                'Annual mean return (in %)': annualized_mean,
                'Annual volatility (in %)': annualized_volatility,
                'Annual semi volatility (in %)': annualized_semi_volatility,
                'Minimum return (in %)': round(min_ret*100,2),
                'Date of minimum return': min_ret_date,
                'Maximum return (in %)': round(max_ret*100,2),
                'Date of maximum return': max_ret_date,
                'INTRADAY TRADING RANGES': '',
                'Minimum trading range (in %)': round(min_trading_range * 100, 2),
                'Date of Min. trading range': min_trading_range_date,
                'Maximum trading range (in %)': round(max_trading_range * 100, 2),
                'Date of Max. trading range': max_trading_range_date,
                'Kurtosis': kurtosis,
                'Skewness': skewness,
                'Maximum drawdown (daily, in %)': round(max_drawdown*100,2),
                'RISK OF LOSS (daily, in %)': '',
                'VaR(95.0)': var_dict[0.05],
                'VaR(99.0)': var_dict[0.01],
                'VaR(99.9)': var_dict[0.001],
                'EXPECTED SHORTFALL (daily, in %)': '',
                'Conditional VaR(95.0)': cvar_dict[0.05],
                'Conditional VaR(99.0)': cvar_dict[0.01],
                'Conditional VaR(99.9)': cvar_dict[0.001]
            })
            
        df = pd.DataFrame(stats)
        df = df.set_index('Symbol')
        df = df.transpose()
        print(df.to_markdown(tablefmt="grid"))
        save = input("Save output to the current folder? (y/n)")

        if save.lower() == 'y':
            
            folder_name = "output"
            save_dir = os.path.isdir(folder_name)
            current_dir = os.getcwd()

            if not save_dir:
                os.makedirs(folder_name)
                
            with open(f"{current_dir}/{folder_name}/{symbol}_statistics_{first_date}-{end}_{picture}.txt", "w") as f:
                if markdown:
                    f.write(df.to_markdown())
                else:
                    f.write(df.to_markdown(tablefmt="grid"))

            print(f"Text file saved to {current_dir}/{folder_name}.")


    except Exception as e:
        error_msg = f"Unexpected Error: {e}\nTraceback: {traceback.format_exc()}"
        print(error_msg)
        
        return error_msg
    
if __name__ == '__main__':
    
    calculate_stats(["ADS.DE", "GOOG"], "2008-01-01", "2017-12-31")
