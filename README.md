# witching-hour-qiskit

`witching-hour-qiskit` is a minimal qBraid ecosystem repository for running Qiskit circuits through the qBraid runtime.

This repository is designed to be simple to review, simple to publish as a custom environment, and simple to extend into a larger quantum application.

## What this repo includes

- `requirements.txt` with the core qBraid + Qiskit dependency set
- `examples/bell_state_job.py` as a minimal runtime submission example
- `SUBMISSION.md` with draft copy for the qBraid publish request form
- `.gitignore` for a clean public repository

## Recommended use

Use this repository as a public GitHub repo for a qBraid environment submission.

If you want to target a specific provider, update the device ID in `examples/bell_state_job.py` after verifying that the device is available in your qBraid account.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
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

## Run the example

```bash
python examples/bell_state_job.py
```

## Suggested next steps

1. Create a new GitHub repository.
2. Push this folder to GitHub.
3. Replace the placeholder metadata in `SUBMISSION.md`.
4. In qBraid Lab, create or import the environment from this repository.
5. Use the publish request flow and paste in the `SUBMISSION.md` content.
