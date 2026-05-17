## Detailed Software Description

This repository provides an algorithmic breakdown of the strategic asymmetric interaction between classical and quantum computational frameworks. 

### 1. Classical Simulation (`classical_simulation.py`)
The classical architecture implements a stochastic 3-turn game loop. The system initializes a binary register to representing the "Tails" state ($0$). 
- **Turn 1:** The Computer selects an action via a uniform pseudo-random distribution: $\text{Choice} \in \{\text{Keep}, \text{Flip}\}$.
- **Turn 2:** The Human Player provides an independent stochastic binary input under identical parameter spaces.
- **Turn 3:** The Computer applies a secondary random operation.

The software tracks the final state register over an arbitrary iteration space ($N = 100,000$). Because all paths execute modular bit-flips over uniform distributions, the output bounds asymptotically to a standard Bernoulli distribution with a strict probability parameter of $p = 0.5$.

### 2. Quantum Circuit Infrastructure (`quantum_simulation.py`)
The quantum script translates the physical principles of superposition into an operational circuit leveraging Qiskit 1.x and the `qiskit-aer` execution backend.
- **State Initialization:** A single-qubit quantum register is initialized in the computational ground state $|0\rangle$.
- **Superposition Phase:** The software applies a Hadamard gate ($H$), performing a basis change to map the qubit onto the equator of the Bloch Sphere, achieving the state:
  $$|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$$
- **Invariance Phase:** To simulate unpredictable human behavior, the script randomly decides whether the player applies a Pauli-$X$ operator (a computational bit-flip) or an Identity ($I$) operator. Because $X|+\rangle = |+\rangle$, the script demonstrates that the player's choice yields zero physical phase or state modifications on the underlying density matrix.
- **Collapsing and Readout:** A secondary Hadamard gate is applied by the computer, reversing the original basis transformation and mapping the state back to $|0\rangle$. A final deterministic Pauli-$X$ gate guarantees that the final projective measurement maps to $|1\rangle$ ("Heads") with a probability amplitude equal to $1.0$.
