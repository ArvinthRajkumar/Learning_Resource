from abc import ABC, abstractmethod

class Channel(ABC):
    @abstractmethod
    def send(self, user, msg): ...

class Email(Channel):
    def send(self, user, msg): return "email to %s: %s" % (user["name"], msg)
class Sms(Channel):
    def send(self, user, msg): return "sms to %s: %s" % (user["name"], msg)
class Push(Channel):
    def send(self, user, msg): return "push to %s: %s" % (user["name"], msg)

class ChannelFactory:
    _reg = {"email": Email, "sms": Sms, "push": Push}
    @classmethod
    def create(cls, name): return cls._reg[name]()

class NotificationHub:
    def notify(self, user, msg):
        return [ChannelFactory.create(c).send(user, msg) for c in user["prefs"]]

hub = NotificationHub()
print(hub.notify({"name": "Ada", "prefs": ["email", "push"]}, "Order shipped"))
