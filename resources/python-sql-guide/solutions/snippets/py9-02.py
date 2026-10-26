from typing import Protocol
class Notifier(Protocol):
    def send(self, to: str, message: str) -> None: ...
class EmailNotifier:
    def send(self, to, message): print(f"email to {to}: {message}")
class FakeNotifier:                                  # a test double, no inheritance needed
    def __init__(self): self.sent = []
    def send(self, to, message): self.sent.append((to, message))
class SignupService:
    def __init__(self, notifier: Notifier): self.notifier = notifier      # dependency injection
    def register(self, email):
        self.notifier.send(email, "Welcome!")
        return {"email": email}
SignupService(EmailNotifier()).register("a@x.com")
fake = FakeNotifier(); SignupService(fake).register("b@x.com")
print("test double recorded:", fake.sent)
