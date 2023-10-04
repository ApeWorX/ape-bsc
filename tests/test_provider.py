def test_basic(account, second_account, networks, eth_tester_provider):
    receipt = account.transfer(second_account, 100)

    assert not receipt.failed
    assert receipt.value == 100
