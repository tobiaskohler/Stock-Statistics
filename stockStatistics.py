import argparse
import ast
from statisticsModule import calculate_stats


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculates relevant descriptive statistics of given symbols. Set -d to true to visualize the drawdown.')
    parser.add_argument("-s", "--symbols", type=str, nargs='+', help="List of stock symbols to plot")    
    parser.add_argument('-b', '--begin', type=str, help='Start date in YYYY-MM-DD format', default=None)
    parser.add_argument('-e', '--end', type=str, help='End date in YYYY-MM-DD format', default=None)
    parser.add_argument('-md', '--markdown', type=str, help='Defines if .txt output should be saved in .md compatible format. Default is True.', default='True')
    parser.add_argument('-d', '--drawdown-picture', type=str, help='Visualizes the drawdown and allows to save exports as .png and .html', default='False')
    args = parser.parse_args()
    
    drawdown_picture = ast.literal_eval(args.drawdown_picture)
    markdown = ast.literal_eval(args.markdown)

    calculate_stats(args.symbols, args.begin, args.end, drawdown_picture, markdown)