include "qelib1.inc";
qreg q[5];
creg c[5];

//q[0] = Bob's output register
//q[1] = Bob's random bit register
//q[2] = Channel register
//q[3] = Unused
//q[4] =  Alice's input register


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