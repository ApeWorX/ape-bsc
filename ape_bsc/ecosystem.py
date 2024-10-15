from typing import ClassVar, cast

from ape_ethereum.ecosystem import (
    BaseEthereumConfig,
    Ethereum,
    NetworkConfig,
    create_network_config,
)
from ape_ethereum.transactions import TransactionType

NETWORKS = {
    # chain_id, network_id
    "mainnet": (56, 56),
    "testnet": (97, 97),
    "opbnb": (204, 204),
    "opbnb-testnet": (5611, 5611),
}


def _create_config(block_time: int = 3) -> NetworkConfig:
    return create_network_config(
        block_time=block_time, default_transaction_type=TransactionType.STATIC
    )


class BSCConfig(BaseEthereumConfig):
    DEFAULT_TRANSACTION_TYPE: ClassVar[int] = TransactionType.STATIC.value
    NETWORKS: ClassVar[dict[str, tuple[int, int]]] = NETWORKS
    mainnet: NetworkConfig = _create_config()
    testnet: NetworkConfig = _create_config()

    # opBNB is really fast, hence the low block time.
    opbnb: NetworkConfig = _create_config(block_time=1)
    opbnb_testnet: NetworkConfig = _create_config(block_time=1)


class BSC(Ethereum):
    fee_token_symbol: str = "BNB"

    @property
    def config(self) -> BSCConfig:  # type: ignore[override]
        return cast(BSCConfig, self.config_manager.get_config("bsc"))
