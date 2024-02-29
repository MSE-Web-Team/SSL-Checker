from interface.Notifier import Notifier
from interface.CertReader import CertReader
from datetime import date, timedelta

class CertChecker:
    def __init__(self, mailer: Notifier, reader: CertReader, daysOffset=28):
        self.mailer = mailer
        self.reader = reader
        self.datetime_offset = date.today() + timedelta(days=daysOffset) #expires in 14 or so days

    def checkHostnames(self, hostnames):
        for hostname in hostnames:
            try:
                expires = self.reader.getCertExpiration(hostname).date()
                
                if self.datetime_offset < expires:
                    print(f"Status of {hostname}: Good ✔️")
                else:
                    print(f"Status of {hostname}: Bad 💩")
                    self.mailer.notify(hostname, expires)
            except Exception as e:
                print(f"An error occurred while polling {hostname}: {e}")