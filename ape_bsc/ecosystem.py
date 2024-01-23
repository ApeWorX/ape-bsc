from typing import ClassVar, cast, Dict, Tuple

from ape_ethereum.ecosystem import (
    BaseEthereumConfig,
    Ethereum,
    NetworkConfig,
    create_network_config, create_local_network_config,
)
from ape_ethereum.transactions import TransactionType

NETWORKS = {
    # chain_id, network_id
    "mainnet": (56, 56),
    "testnet": (97, 97),
}


def _create_config() -> NetworkConfig:
    return create_network_config(block_time=3, default_transaction_type=TransactionType.STATIC)


class BSCConfig(BaseEthereumConfig):
    DEFAULT_TRANSACTION_TYPE: ClassVar[int] = TransactionType.STATIC.value
    NETWORKS: ClassVar[Dict[str, Tuple[int, int]]] = NETWORKS
    mainnet: NetworkConfig = _create_config()
    testnet: NetworkConfig = _create_config()


class BSC(Ethereum):
    fee_token_symbol = "BNB"

    @property
    def config(self) -> BSCConfig:  # type: ignore[override]
        return cast(BSCConfig, self.config_manager.get_config("bsc"))
