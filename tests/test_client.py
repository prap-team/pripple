import pytest
from unittest.mock import patch, MagicMock
from pripple.client import XRPLClass
from xrpl.wallet import Wallet


@pytest.fixture
def xrpl_client():
    return XRPLClass("https://s.altnet.rippletest.net:51234/")


def test_get_account_new(xrpl_client):
    with patch("pripple.client.generate_faucet_wallet") as mock_faucet:
        mock_wallet = MagicMock(spec=Wallet)
        mock_wallet.address = "rTESTADDRESS"
        mock_wallet.seed = "sTESTSEED"
        mock_faucet.return_value = mock_wallet

        wallet = xrpl_client.get_account(seed="")
        assert wallet.address == "rTESTADDRESS"
        assert wallet.seed == "sTESTSEED"


def test_get_account_existing(xrpl_client):
    seed = "sEXISTINGSEED"
    wallet = xrpl_client.get_account(seed=seed)
    assert wallet.seed == seed
    assert wallet.address.startswith("r")


@patch("pripple.client.JsonRpcClient")
def test_get_account_info(mock_client_class, xrpl_client):
    mock_client = MagicMock()
    mock_client_class.return_value = mock_client
    mock_response = MagicMock()
    mock_response.result = {"account_data": {"Balance": "1000"}}
    mock_client.request.return_value = mock_response

    info = xrpl_client.get_account_info("rTESTACCOUNT")
    assert info["Balance"] == "1000"


@patch("pripple.client.submit_and_wait")
def test_send_xrp(mock_submit, xrpl_client):
    mock_submit.return_value = {"result": "success"}
    seed = "sTESTSEED"
    amount = 10
    destination = "rDESTADDR"

    result = xrpl_client.send_xrp(seed, amount, destination)
    assert result["result"] == "success"

