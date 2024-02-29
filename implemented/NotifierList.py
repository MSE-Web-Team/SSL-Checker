from interface.Notifier import Notifier

class NotifierList(Notifier):
    def __init__(self, observers):
        self.observers = observers

    def notify(self, hostname, day):
        for notifier in self.observers:
            notifier.notify(hostname, day)