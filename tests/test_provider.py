def test_use_provider(account, provider):
    receipt = account.transfer(account, 100)
    assert not receipt.failed
    assert receipt.value == 100
    # Ensure uses type 0 by default.
    assert receipt.transaction.type == 0
