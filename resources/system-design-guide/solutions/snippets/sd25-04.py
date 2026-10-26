import heapq, itertools
class OrderBook:
    def __init__(self): self.bids, self.asks, self.seq, self.trades = [], [], itertools.count(), []
    def add(self, side, price, qty, oid):
        order = [qty, oid]
        if side == "buy":
            while order[0] and self.asks and self.asks[0][0] <= price:
                ap, _, ao = self.asks[0]
                fill = min(order[0], ao[0]); order[0] -= fill; ao[0] -= fill
                self.trades.append((oid, ao[1], ap, fill))
                if ao[0] == 0: heapq.heappop(self.asks)
            if order[0]: heapq.heappush(self.bids, (-price, next(self.seq), order))
        else:
            while order[0] and self.bids and -self.bids[0][0] >= price:
                bp, _, bo = self.bids[0]
                fill = min(order[0], bo[0]); order[0] -= fill; bo[0] -= fill
                self.trades.append((bo[1], oid, -bp, fill))
                if bo[0] == 0: heapq.heappop(self.bids)
            if order[0]: heapq.heappush(self.asks, (price, next(self.seq), order))
book = OrderBook()
book.add("sell", 101, 50, "S1"); book.add("sell", 100, 30, "S2"); book.add("sell", 100, 20, "S3")
book.add("buy", 99, 40, "B1")                # does not cross: rests in the book
book.add("buy", 101, 70, "B2")               # crosses: takes S2 (30) and S3 (20) at 100 (time priority), then 20 of S1 at 101
print("trades (buyer, seller, price, qty):", book.trades)
print("resting asks:", [(p, o[1], o[0]) for p, _, o in sorted(book.asks)], "| resting bids:", [(-p, o[1], o[0]) for p, _, o in sorted(book.bids)])
