import ssl
import socket
from interface.CertReader import CertReader
from cryptography.x509 import load_pem_x509_certificate

class SSLCertReader(CertReader):

    def getCertExpiration(self, hostname: str, port=443):
        context = ssl.create_default_context()
        context.check_hostname = False #required to set to false for verify_mode
        context.verify_mode = ssl.CERT_NONE #don't check if CA is verified

        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                pem_data = ssl.DER_cert_to_PEM_cert(ssock.getpeercert(binary_form=True))
                cert = load_pem_x509_certificate(bytes(pem_data, 'utf-8'))
                expiration_date = cert.not_valid_after
                return expiration_date