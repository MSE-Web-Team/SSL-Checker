from abc import ABC, abstractmethod

class CertReader(ABC):
    @abstractmethod
    def getCertExpiration(self, hostname: str, port=443):
        pass