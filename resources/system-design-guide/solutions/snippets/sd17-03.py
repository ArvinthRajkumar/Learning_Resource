class VendingMachine:
    def __init__(self, stock):
        self.stock, self.balance, self.state = dict(stock), 0, "idle"
    def insert(self, cents):
        if self.state == "dispensing":
            raise RuntimeError("busy")
        self.balance += cents
        self.state = "has_money"
    def select(self, item):
        if self.state != "has_money":
            return "insert money first"
        price, qty = self.stock[item]
        if qty == 0:
            return "sold out"
        if self.balance < price:
            return "need %d more" % (price - self.balance)
        self.state = "dispensing"
        self.stock[item] = (price, qty - 1)
        change, self.balance, self.state = self.balance - price, 0, "idle"
        return "dispensed %s, change %d" % (item, change)
    def cancel(self):
        refund, self.balance, self.state = self.balance, 0, "idle"
        return refund

vm = VendingMachine({"cola": (150, 1)})
print(vm.select("cola"))
vm.insert(100); print(vm.select("cola"))
vm.insert(100); print(vm.select("cola"))
vm.insert(200); print(vm.select("cola"), vm.cancel())
