import matplotlib.pyplot as plt

class InventoryAgent:
    def __init__(self, avg_price, discount_threshold=0.2, critical_stock_level=10, min_order_qty=10):
        self.avg_price = avg_price  # Average price of the smartphone
        self.discount_threshold = discount_threshold  # 20% discount threshold
        self.critical_stock_level = critical_stock_level  # Critical stock level (e.g., 10 units)
        self.min_order_qty = min_order_qty  # Minimum order quantity (e.g., 10 units)
        self.price_history = []  # To store price data for graphing
        self.stock_history = []  # To store stock level data for graphing
        self.order_history = []  # To store order data for graphing

    def check_price(self, current_price):
        # Check if current price is below the threshold (20% below average price)
        return current_price < (1 - self.discount_threshold) * self.avg_price

    def check_stock_level(self, current_stock):
        # Check if stock level is below critical stock level
        return current_stock < self.critical_stock_level

    def decide_order(self, current_price, current_stock):
        # Determine the quantity to order based on price and stock conditions
        if self.check_stock_level(current_stock):
            # If stock level is critical, order minimum quantity
            tobuy = self.min_order_qty
        elif self.check_price(current_price):
            # If price is significantly below average, order additional units
            tobuy = 15
        else:
            # Otherwise, no order
            tobuy = 0
        return tobuy

    def process(self, current_price, current_stock):
        # Record current state
        self.price_history.append(current_price)
        self.stock_history.append(current_stock)
        # Decide on order quantity
        tobuy = self.decide_order(current_price, current_stock)
        self.order_history.append(tobuy)
        # Simulate stock update
        current_stock += tobuy
        return tobuy, current_stock

    def plot_graphs(self):
        # Plot price, stock levels, and order decisions over time
        plt.figure(figsize=(12, 8))

        plt.subplot(3, 1, 1)
        plt.plot(self.price_history, label='Price', color='blue')
        plt.axhline(y=(1 - self.discount_threshold) * self.avg_price, color='red', linestyle='--', label='Discount Threshold')
        plt.ylabel('Price')
        plt.legend()

        plt.subplot(3, 1, 2)
        plt.plot(self.stock_history, label='Stock Level', color='green')
        plt.axhline(y=self.critical_stock_level, color='red', linestyle='--', label='Critical Stock Level')
        plt.ylabel('Stock Level')
        plt.legend()

        plt.subplot(3, 1, 3)
        plt.plot(self.order_history, label='Order Quantity', color='purple')
        plt.ylabel('Order Quantity')
        plt.xlabel('Time')
        plt.legend()

        plt.tight_layout()
        plt.show()


# Example Usage
avg_price = 600  # Example average price
agent = InventoryAgent(avg_price=avg_price)

# Simulate a time series of price and stock levels
prices = [600, 580, 550, 520, 500, 510, 530, 570, 590, 600, 590]
stocks = [20, 18, 15, 12, 9, 8, 15, 13, 11, 10, 9]

# Run the agent through each time step
for current_price, current_stock in zip(prices, stocks):
    tobuy, updated_stock = agent.process(current_price, current_stock)
    print(f"Current Price: {current_price}, Current Stock: {current_stock}, Ordered: {tobuy}, New Stock: {updated_stock}")

# Plot the results
agent.plot_graphs()
