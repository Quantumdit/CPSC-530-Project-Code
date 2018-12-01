include "qelib1.inc";
qreg q[5];
creg c[5];

//q[0] = Bob's output register
//q[1] = Bob's random bit register
//q[2] = Channel register
//q[3] = Alice's random bit register
//q[4] =  Alice's input register

//Negate input bit to send a one
x q[4];

// Alice Section:

//Generate a random bit for Alice
h q[3];

// Controlled Hadamard q[3] -> q[4]
s q[3];
h q[4];
sdg q[4];
cx q[3],q[4];
h q[4];
t q[4];
cx q[3],q[4];
t q[4];
h q[4];
s q[4];
x q[4];

// Channel section

// Alice pushes qubit to channel
// X basis
cx q[4],q[2];
// Z basis
h q[4];
h q[2];
cx q[4],q[2];
h q[2];
h q[4];

// Bob pulls qubit from channel
// X basis
cx q[2],q[0];
// Z basis
h q[2];
h q[0];
cx q[2],q[0];
h q[0];
h q[2];

// Generate random bit for Bob
h q[1];

// Controlled Hadamard q[1] -> q[0]
s q[1];
h q[0];
sdg q[0];
cx q[1],q[0];
h q[0];
t q[0];
cx q[1],q[0];
t q[0];
h q[0];
s q[0];
x q[0];

//Measure result
measure q[0] -> c[4];

//Measure bases
measure q[3] -> c[0];
measure q[1] -> c[1];