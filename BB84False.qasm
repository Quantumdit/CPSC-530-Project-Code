// Name of Experiment: BB84 v2

OPENQASM 2.0;
include "qelib1.inc";

qreg q[5];
creg c[3];

//Send message = true
id q[4];

// Encrypt
h q[3]; //Random bit
cx q[3], q[4];
measure q[3] -> c[0];

// Channel Transmission
cx q[4],q[2];
cx q[2],q[0];

// Decrypt
h q[1];
cx q[1], q[0];
measure q[1] -> c[1];

// Measure Result
measure q[0] -> c[2];