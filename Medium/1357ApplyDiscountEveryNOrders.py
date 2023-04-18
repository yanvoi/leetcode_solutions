class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.discount = discount
        self.n = n
        self.customer_count = 0
        self.id_to_price = dict(zip(products, prices))

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_count += 1
        subtotal = sum(self.id_to_price[p] * a for p, a in zip(product, amount))
        
        if self.customer_count % self.n != 0:
            return subtotal

        return subtotal * ((100 - self.discount) / 100)

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
