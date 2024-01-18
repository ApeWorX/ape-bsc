from typing import Optional, Type, cast

from ape.api.config import PluginConfig
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.utils import DEFAULT_LOCAL_TRANSACTION_ACCEPTANCE_TIMEOUT
from ape_ethereum.ecosystem import Ethereum, ForkedNetworkConfig, NetworkConfig
from ape_ethereum.transactions import TransactionType

NETWORKS = {
    # chain_id, network_id
    "mainnet": (56, 56),
    "testnet": (97, 97),
}


def _create_config(
    required_confirmations: int = 1, block_time: int = 3, cls: Type = NetworkConfig, **kwargs
) -> NetworkConfig:
    return cls(
        block_time=block_time,
        default_transaction_type=TransactionType.STATIC,
        required_confirmations=required_confirmations,
        **kwargs,
    )


def _create_local_config(default_provider: Optional[str] = None, use_fork: bool = False, **kwargs):
    return _create_config(
        block_time=0,
        default_provider=default_provider,
        gas_limit="max",
        required_confirmations=0,
        transaction_acceptance_timeout=DEFAULT_LOCAL_TRANSACTION_ACCEPTANCE_TIMEOUT,
        cls=ForkedNetworkConfig if use_fork else NetworkConfig,
        **kwargs,
    )


class BSCConfig(PluginConfig):
    mainnet: NetworkConfig = _create_config()
    mainnet_fork: ForkedNetworkConfig = _create_local_config(use_fork=True)
    testnet: NetworkConfig = _create_config()
    testnet_fork: ForkedNetworkConfig = _create_local_config(use_fork=True)
    local: NetworkConfig = _create_local_config(default_provider="test")
    default_network: str = LOCAL_NETWORK_NAME


class BSC(Ethereum):
    @property
    def config(self) -> BSCConfig:  # type: ignore[override]
        return cast(BSCConfig, self.config_manager.get_config("bsc"))
