"""Minimal qBraid + Qiskit runtime example."""

from qbraid.runtime import QbraidProvider
from qiskit import QuantumCircuit


DEVICE_ID = "aws:aqt:qpu:ibex-q1"


def main() -> None:
    provider = QbraidProvider()
    device = provider.get_device(DEVICE_ID)

    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])

    print(f"Submitting circuit to {DEVICE_ID}")
    job = device.run(circuit, shots=1000)
    result = job.result()
    print("Counts:", result.data.get_counts())


if __name__ == "__main__":
    main()
