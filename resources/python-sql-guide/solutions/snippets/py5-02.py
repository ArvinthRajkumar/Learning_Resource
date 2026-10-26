from unittest.mock import Mock, patch

def convert(amount, client):
    rate = client.get_rate("EUR", "USD")
    return round(amount * rate, 2)

client = Mock()
client.get_rate.return_value = 1.1
print(convert(100, client))
client.get_rate.assert_called_once_with("EUR", "USD")

import time
def now_label():
    return "t=%d" % int(time.time())
with patch("time.time", return_value=1000):
    print(now_label())
