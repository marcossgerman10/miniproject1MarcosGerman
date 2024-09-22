### INF601 - Advanced Programming in Python
### Marcos German
### Mini Project 1

# Stock Price Charts

This project visualizes the closing prices of 5 popular stock tickers over the last 10 trading days.

## Description

This project utilizes the `yfinance` library to fetch historical stock data and `matplotlib` to generate line graphs of the closing prices for the last 10 days. The generated graphs are saved as PNG files in a `charts` directory. This allows users to quickly view and compare recent stock price trends for selected tickers.

## Getting Started

### Dependencies

* Python 3.x
* Libraries:
  * `matplotlib`
  * `numpy`
  * `yfinance`
* Ensure Python is installed on your system. (e.g., Windows 10, macOS, or Linux)

### Installing
1. Clone the repository:
    git clone https://github.com/marcossgerman10/miniproject1MarcosGerman.git
2. Navigate to the Project Directory:
    cd miniproject1MarcosGerman
3. Install the Required Packages:
    pip install -r requirements.txt

### Executing program
1. Ensure that all dependencies are installed and you are in the project directory
2. Run the Python script to fetch data and generate graphs:
    python stock_graphs.py

### Help
If you encounter issues, ensure the following:

* You have an active internet connection for fetching data.
* The stock tickers used are valid and correctly specified.
* You have the necessary permissions to create files and directories.

## Authors
Marcos German

## Version History

* 0.1
    * Initial release with basic functionality for fetching and plotting stock prices

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [yfinance](https://pypi.org/project/yfinance/)
* [matploblib](https://matplotlib.org/stable/tutorials/pyplot.html)
* [chatgpt](https://chatgpt.com/)