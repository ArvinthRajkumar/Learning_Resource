from dataclasses import dataclass, field

SIZES = {"moto": 1, "car": 2, "large": 3}

@dataclass
class Spot:
    id: str
    size: int
    vehicle: str = None
    def fits(self, kind): return self.vehicle is None and self.size >= SIZES[kind]

@dataclass
class Ticket:
    id: int
    spot: Spot
    vehicle: str
    entry: float

class ParkingLot:
    def __init__(self, spots, rate_per_hour=5):
        self.spots, self.rate, self.tickets, self.next_id = spots, rate_per_hour, {}, 1
    def park(self, vehicle, kind, now):
        # best fit: smallest free spot that fits (keeps big spots for big vehicles)
        cands = [s for s in self.spots if s.fits(kind)]
        if not cands:
            raise RuntimeError("lot full for " + kind)
        spot = min(cands, key=lambda s: s.size)
        spot.vehicle = vehicle
        t = Ticket(self.next_id, spot, vehicle, now)
        self.tickets[t.id] = t
        self.next_id += 1
        return t
    def leave(self, ticket_id, now):
        t = self.tickets.pop(ticket_id)
        t.spot.vehicle = None
        hours = max(1, -(-int(now - t.entry) // 3600))       # round up to whole hours
        return hours * self.rate

lot = ParkingLot([Spot("A1", 1), Spot("A2", 2), Spot("A3", 3)])
t1 = lot.park("bike", "moto", 0)
t2 = lot.park("sedan", "car", 0)
print(t1.spot.id, t2.spot.id)
print("fee:", lot.leave(t2.id, 2 * 3600 + 1))
print("free for large:", [s.id for s in lot.spots if s.fits("large")])
