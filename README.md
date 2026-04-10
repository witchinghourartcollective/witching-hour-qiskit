# witching-hour-qiskit

`witching-hour-qiskit` is a minimal qBraid ecosystem Python package for running Qiskit circuits through the qBraid runtime.

This repository is designed to be simple to review, simple to publish as a custom environment, and simple to extend into a larger quantum application.

## Overview

`witching-hour-qiskit` is a minimal qBraid ecosystem project that demonstrates how to:

- authenticate with qBraid using an account API key
- inspect available runtime devices
- create a simple Qiskit circuit
- submit a job through the qBraid runtime
- retrieve measurement counts from the completed run

The current example is intentionally narrow. It is meant to validate the basic qBraid-to-Qiskit workflow without adding extra abstractions, domain-specific logic, or packaging complexity.

## Project links

- Repository: https://github.com/witchinghourartcollective/witching-hour-qiskit
- Documentation: https://github.com/witchinghourartcollective/witching-hour-qiskit#readme
- Package link: use the GitHub repository until a PyPI release exists

## qBraid submission metadata

- Software type: application tooling
- Interface: Python API workflow with an optional command-line entrypoint
- Primary topics:
  - research demo
  - circuit building
  - circuit manipulation
  - provider
  - openqasm
- Qiskit-pattern coverage:
  - execute on hardware
  - post process results

This repository does not currently implement problem mapping or hardware-specific optimization passes. It focuses on a minimal end-to-end runtime workflow using qBraid and Qiskit.

## What this repo includes

- `src/witching_hour_qiskit` as the installable Python package
- `examples/bell_state_job.py` as a minimal runtime example using the package
- `SUBMISSION.md` with draft copy for the qBraid publish request form
- `.gitignore` for a clean public repository

## Recommended use

Use this repository as a public GitHub repo and installable Python package for a qBraid environment submission.

If you want to target a specific provider, update the device ID in `examples/bell_state_job.py` after verifying that the device is available in your qBraid account.

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

You can also install from a clone without editable mode:

```bash
pip install .
```

## Configure credentials

Set your qBraid API key before running examples:

```bash
export QBRAID_API_KEY="your_api_key_here"
```

You can find the API key in your qBraid account dashboard.

## Quick smoke test

This checks that authentication works and your account can list devices:

```bash
python - <<'PY'
from qbraid.runtime import QbraidProvider

provider = QbraidProvider()
devices = provider.get_devices()
print(f"Discovered {len(devices)} devices")
for device in devices[:10]:
    print(device)
PY
```

## Python API usage

```python
from witching_hour_qiskit import create_bell_state_circuit, run_bell_state_job

circuit = create_bell_state_circuit()
result = run_bell_state_job()
print(result.data.get_counts())
```

## Command-line usage

After installing the package, you can use the console entrypoint:

```bash
witching-hour-qiskit list-devices --limit 5
witching-hour-qiskit run-bell --device-id aws:aqt:qpu:ibex-q1 --shots 1000
```

You can also run it as a module:

```bash
python3 -m witching_hour_qiskit list-devices --limit 5
```

## Example workflow

The repository currently demonstrates the following runtime flow:

1. Initialize a `QbraidProvider`
2. Resolve a target device through the qBraid runtime
3. Build a Bell-state circuit in Qiskit
4. Submit the circuit with a fixed shot count
5. Wait for completion and print the result counts

This workflow is exposed through the package API and demonstrated in `examples/bell_state_job.py`.

## Run the example

```bash
python3 examples/bell_state_job.py
```

## Repository structure

```text
.
├── README.md
├── SUBMISSION.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── src
│   └── witching_hour_qiskit
│       ├── __init__.py
│       ├── __main__.py
│       ├── api.py
│       └── cli.py
└── examples
    └── bell_state_job.py
```

## Intended ecosystem positioning

This repository fits best as:

- application tooling
- research demo
- circuit building
- circuit manipulation
- provider integration

It is not a simulator, transpiler, synthesis library, or standalone compute provider.

## Why this belongs in the ecosystem

`witching-hour-qiskit` gives new users a low-friction entry point into qBraid with a minimal dependency set, a documented setup flow, and a runnable end-to-end Qiskit example. It is intentionally small enough for quick review and simple enough to use as a starting point for larger quantum workflows.

## Limitations

- The example depends on valid qBraid credentials.
- The configured device ID may need to be changed depending on your account access.
- This package is intentionally minimal and does not yet include advanced transpilation, optimization, or domain-specific workflows.

## Publishing to PyPI

Once you are ready to publish a real package release:

```bash
python3 -m pip install --upgrade build twine
python3 -m build
python3 -m twine upload dist/*
```

Until then, the GitHub repository is the correct public package reference.
