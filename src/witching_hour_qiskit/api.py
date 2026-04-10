"""Minimal qBraid and Qiskit helper functions."""

from __future__ import annotations

from collections.abc import Sequence

from qbraid.runtime import QbraidProvider
from qiskit import QuantumCircuit

DEFAULT_DEVICE_ID = "aws:aqt:qpu:ibex-q1"
DEFAULT_SHOTS = 1000


def create_bell_state_circuit() -> QuantumCircuit:
    """Create a 2-qubit Bell-state circuit with measurement."""
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])
    return circuit


def list_devices(limit: int = 10) -> Sequence[object]:
    """Return a small list of devices visible to the current qBraid account."""
    provider = QbraidProvider()
    return provider.get_devices()[:limit]


def run_bell_state_job(
    device_id: str = DEFAULT_DEVICE_ID,
    shots: int = DEFAULT_SHOTS,
) -> object:
    """Submit the Bell-state circuit to a qBraid runtime device and return the result."""
    provider = QbraidProvider()
    device = provider.get_device(device_id)
    circuit = create_bell_state_circuit()

    print(f"Submitting circuit to {device_id}")
    job = device.run(circuit, shots=shots)
    result = job.result()
    print("Counts:", result.data.get_counts())
    return result
