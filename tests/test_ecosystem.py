import pytest
from ape_ethereum.transactions import TransactionType
from ethpm_types import MethodABI


def test_gas_limit(bsc):
    assert bsc.config.local.gas_limit == "max"


@pytest.mark.parametrize("type", (None, 0, "0x0"))
def test_create_transaction(bsc, type, eth_tester_provider):
    tx = bsc.create_transaction(type=type)
    assert tx.type == TransactionType.STATIC.value
    assert tx.gas_limit == eth_tester_provider.max_gas


@pytest.mark.parametrize(
    "type_",
    (TransactionType.STATIC.value, TransactionType.DYNAMIC.value),
)
def test_encode_transaction(type_, bsc, eth_tester_provider):
    abi = MethodABI.parse_obj(
        {
            "type": "function",
            "name": "fooAndBar",
            "stateMutability": "nonpayable",
            "inputs": [],
            "outputs": [],
        }
    )
    address = "0x274b028b03A250cA03644E6c578D81f019eE1323"
    actual = bsc.encode_transaction(address, abi, sender=address, type=type_)
    assert actual.gas_limit == eth_tester_provider.max_gas
