# Quick Start

Ecosystem Plugin for Binance Smart Chain support in Ape.

## Dependencies

* [python3](https://www.python.org/downloads) version 3.8 or greater, python3-dev

## Installation

### via `ape`

You can install this plugin using `ape`:

```bash
ape plugins install bsc
```

or via config file:

```yaml
# ape-config.yaml
plugins:
  - name: bsc
```

### via `pip`

You can install the latest release via [`pip`](https://pypi.org/project/pip/):

```bash
pip install ape-bsc
```

### via `setuptools`

You can clone the repository and use [`setuptools`](https://github.com/pypa/setuptools) for the most up-to-date version:

```bash
git clone https://github.com/ApeWorX/ape-bsc.git
cd ape-bsc
python3 setup.py install
```

## Quick Usage

Installing this plugin adds support for the Binance Smart Chain ecosystem:

```bash
ape console --network bsc:mainnet
```

## Development

This project is in development and should be considered a beta.
Things might not be in their final state and breaking changes may occur.
Comments, questions, criticisms and pull requests are welcomed.
