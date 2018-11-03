# CPSC-530-Project-Code

Allows transmitting a bitstring using the BB84 algorithm inside a quantum computer. Designed for the 5 qubit "ibmqx4" quantum computer. In the Python code, a message is transmitted through the quantum computer one bit at a time, with 1024 "shots" being used the calculate the probabilities of success and failure.

## Running the Code

**Option 1 (Preferred)**: Run the main file using python 3.

You may need to use a python package manager like pip or easy_install on the command line to install the package "IBMQuantumExperience".

    $ pip install IBMQuantumExperience

Note that this method requires you to have "BB84True.qasm" and "BB84False.qasm" in the same directory.

**Option 2**: Run one of the QASM files in a QASM simulator.

By using any QASM simulator, you can simulate the circuit. Additionally, if you use the IBM composer, you can simulate or run the circuit on "ibmqx4".

Use "BB84True.qasm" to send the bit "1" and "BB84False.qasm" to send the bit "0". You cannot send a bitstring of length greater than one using this method.

Additionally, if you use this method then you will have to interpret the results manually. Let "b" be the bit that you are trying to transmit and let not(b) be its negation. Measuring "00b" or "11b" is a successful transmission, measuring "01b" or "10b" is an invalid transmission and measuring "00not(b) or "11not(b)" is a corrupted transmission.


## Files

**main**: The main file for the project and the one that should be run in most cases.

**BB84False.qasm**: Quantum Assembly Language code for transmitting the bit "0". Designed for the topology of "ibmqx4".

**BB84True.qasm**: Quantum Assembly Language code for transmitting the bit "1". Designed for the topology of "ibmqx4".
