import pandas as pd
import numpy as np

class StockAnalyzer:
    def __init__(self, data):
        self.data = data

    def calculate_signals(self):
        # Sample calculation of buy/sell signals
        self.data['Signal'] = np.where(self.data['Close'] > self.data['Open'], 'Buy', 'Sell')

    def get_top_picks(self, top_n=5):
        # Returns top N stocks based on some criteria (like highest closing price)
        return self.data.nlargest(top_n, 'Close')

# Example Usage
data = pd.DataFrame({
    'Stock': ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA'],
    'Open': [150, 250, 2000, 3000, 650],
    'Close': [155, 255, 1980, 3050, 630],
})

analyzer = StockAnalyzer(data)
analyzer.calculate_signals()
top_picks = analyzer.get_top_picks()
print(top_picks)