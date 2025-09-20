import xrpl
from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet, generate_faucet_wallet
from xrpl.models.requests.account_info import AccountInfo
from xrpl.models.transactions import Payment
from xrpl.transaction import submit_and_wait, XRPLReliableSubmissionException
from xrpl.utils import xrp_to_drops


class XRPLMeta(type):
    TESTNET_URI = "https://s.altnet.rippletest.net:51234/"

    def __call__(cls, *args, **kwargs):
        if "uri" not in kwargs:
            kwargs["uri"] = cls.TESTNET_URI
        return super().__call__(*args, **kwargs)


class XRPLClass(metaclass=XRPLMeta):
    def __init__(self, url: str):
        self.client = JsonRpcClient(url)

    def fetch_account_info(self, account_id: str) -> AccountInfo:
        return AccountInfo(account=account_id, ledger_index="validated")

    def get_account(self, seed: str = "") -> Wallet:
        if seed == "":
            return generate_faucet_wallet(self.client)
        return Wallet.from_seed(seed)

    def get_account_info(self, account_id: str) -> dict:
        acct_info = self.fetch_account_info(account_id)
        response = self.client.request(acct_info)
        return response.result.get("account_data", {})

    def get_account_result(self, account_id: str) -> str:
        acct_info = self.fetch_account_info(account_id)
        response = self.client.request(acct_info)
        if response.status == xrpl.models.response.ResponseStatus.ERROR:
            return "fail"
        return "success"

    def send_xrp(self, seed: str, amount: int, destination: str):
        sending_wallet = Wallet.from_seed(seed)
        payment = Payment(
            account=sending_wallet.address,
            amount=xrp_to_drops(int(amount)),
            destination=destination,
        )
        try:
            response = submit_and_wait(payment, self.client, sending_wallet)
        except XRPLReliableSubmissionException as e:
            response = {"error": f"Submit failed: {e}"}
        return response

