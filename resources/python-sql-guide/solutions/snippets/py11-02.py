from unittest import mock
import datetime
class PaymentGateway:
    def charge(self, amount): raise RuntimeError("real network call")
def checkout(cart_total, gateway, notify, now=datetime.datetime.now):
    if cart_total <= 0: return "empty cart"
    receipt = gateway.charge(cart_total)
    notify(f"paid {cart_total} at {now().year}")
    return receipt
gateway = mock.Mock()
gateway.charge.return_value = "receipt-42"                            # stub the answer
notify = mock.Mock()                                                    # mock the side effect
result = checkout(250, gateway, notify, now=lambda: datetime.datetime(2030, 1, 1))     # inject the clock
print(result)
gateway.charge.assert_called_once_with(250)                              # verify the interaction
notify.assert_called_once_with("paid 250 at 2030")
print("interactions verified; the empty-cart branch does not touch the gateway:", checkout(0, gateway, notify), gateway.charge.call_count)
