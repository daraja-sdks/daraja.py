from .api.b2c import BusinessToCustomer
from .api.c2b import CustomerToBusiness


class Mpesa:
    def __init__(self, key=None, secret=None, environment="SANDBOX", cert_path=None, password=None) -> None:
        self.consumer_key = key
        self.consumer_secret = secret
        self.environment = environment
        self.certificate_path = cert_path
        self.initiator_password = password


    def __get_auth_token(self) -> str:
        return ""

    def __generate_credential(self) -> str:
        return ""

    def c2b(self):
        return CustomerToBusiness()

    def b2c(self):
        return BusinessToCustomer()