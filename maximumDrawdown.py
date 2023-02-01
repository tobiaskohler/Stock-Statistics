import plotly.express as px
import plotly.graph_objects as go 
import os
import traceback

def calculate_max_drawdown(symbol, first_date, end, df, picture=False) -> float:
    
    try: 
        window = 252

        Roll_Max = df['Close'].rolling(window, min_periods=1).max()
        Daily_Drawdown = df['Close']/Roll_Max - 1.0
        Max_Daily_Drawdown = Daily_Drawdown.rolling(window, min_periods=1).min()

        fig = px.line(x=df.index, y=df['Close'], title=f'{symbol} ({first_date}/{end})', labels={'x': 'Date', 'y': 'Close Price'})
        fig.add_scatter(x=df.index, y=Max_Daily_Drawdown, mode='lines', name='Max. Drawdown', yaxis='y2')
        fig.update_layout(yaxis2=dict(title='Max Drawdown', overlaying='y', side='right'), template='plotly_white', width=600, height=600, title_x=0.5, hovermode="x unified")
        
        fig.update_layout(
            title=go.layout.Title(
                text=f"<b>{symbol} Max. Drawdown (252 window)</b><br><sup>{first_date}/{end}</sup>",
                xref="paper",
                x=0.5
            ),
            yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text='Price'
                )
            ),
            xaxis=go.layout.XAxis(
            title=go.layout.xaxis.Title(
                text='Period'
                )
            )
        )

        if picture:
            fig.show()
            
            save = input("Save graphics to the current folder? (y/n)")

            if save.lower() == 'y':
                
                folder_name = "output"
                save_dir = os.path.isdir(folder_name)
                current_dir = os.getcwd()

                if not save_dir:
                    os.makedirs(folder_name)
                    
                fig.write_image(f"{current_dir}/{folder_name}/{symbol}_statistics_{first_date}-{end}_{picture}.png")
                fig.write_html(f"{current_dir}/{folder_name}/{symbol}_statistics_{first_date}-{end}_{picture}.html")
                print(f"Image saved to {current_dir}/{folder_name}.")

        return Max_Daily_Drawdown.min()

    except Exception as e:
        error_msg = f"Unexpected Error: {e}\nTraceback: {traceback.format_exc()}"
        print(error_msg)
        
        return error_msg