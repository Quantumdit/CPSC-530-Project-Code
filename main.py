"""
Main file for BB84
"""

from IBMQuantumExperience import IBMQuantumExperience
import typing


def main():
    #Input bitstring
    confirmed = False
    while (confirmed == False):
        bitstring = input("Please enter a bitstring: ")
        confirmed = True
        for bit in bitstring:
            if ((bit != "0") and (bit != "1")):
                print("Invalid bitstring, please try again.")
                confirmed = False
                break
            

    #Choose between simulation or running on a real quantum computer
    use_real_quantum_computer = False
    confirmed = False
    while (confirmed == False):
        confirm_string = input("Would you like to use the Simulator (\"S\") or a quantum computer (\"Q\")?: ")
        if ((confirm_string.upper() == "SIMULATOR") or (confirm_string.upper() == "S")):
            print("Using simulator.")
            confirmed = True
        elif ((confirm_string.upper() == "QUANTUM") or (confirm_string.upper() == "QUANTUM COMPUTER") or (confirm_string.upper() == "Q")):
            while (confirmed == False):
                confirm_string = input("Using a real quantum computer will use up limited credits, are you sure you wish to use the quantum computer? (\"Yes\" / \"No\"): ")
                if ((confirm_string.upper() == "YES") or (confirm_string.upper() == "Y")):
                    print("Using quantum computer.")
                    use_real_quantum_computer = True
                    confirmed = True
                elif ((confirm_string.upper() == "No") or (confirm_string.upper() == "N")):
                    print("Using simulator.")
                    confirmed = True
                else:
                    print("I'm sorry, I did not understand your input. Please enter \"Yes\" (\"Y\") or \"No\" (\"N\").")
        else:
            print("I'm sorry, I did not understand your input. Please enter \"Simulator\" (\"S\") or \"Quantum\" (\"Q\").")
            
            
    BB84(bitstring, use_real_quantum_computer)
    return



def BB84(bitstring, use_real_quantum_computer = False, num_shots = 1024):
    results = []
    backend = "simulator"
    if (use_real_quantum_computer):
        backend = "ibmqx4"
    
    #Set up API
    token = "fc5ece78b74c587781375562080c9045498ef906f494aae2a26598c42265083f1a7757f72b536431380d682d6ec9a18b1c40e21eeee3d350488bef58924c1cf0"
    api = IBMQuantumExperience(token)
    
    #Confirm enough credits remain if using a quantum computer
    if (backend != "simulator"):
        remaining_credits = (api.get_my_credits())["remaining"]
        print("Remaining credits: " + str(remaining_credits))
        if (remaining_credits < (len(bitstring)*3)):
            print("Not enough credits remaining to use a quantum computer.")
            print("Reverting to simulation mode.")
            backend = "simulator"
        else:
            print("Confirmed that there are enough credits remain to run the experiment.")
            
    #Run experiment
    for bit in bitstring:
        print("Sending \"" + bit + "\"")
        results.append(sendBoolBB84( (bit=="1"), api, num_shots=num_shots, backend=backend))
    
    print("Processing results...")
    total_SP = 0        #Success Probability, ie successful transmission
    total_IP = 0        #Invalid Probability, ie unsuccessful transmission
    total_CP = 0        #Corruption Probability, ie transmitted incorrect information
    for r in results:
        total_SP += r["Success Probability"]
        total_IP += r["Invalid Probability"]
        total_CP += r["Corruption Probability"]
    average_SP = total_SP/len(bitstring)
    average_IP = total_IP/len(bitstring)
    average_CP = total_CP/len(bitstring)
    
    print("\nResults:")
    print("Average success probability: " + str(average_SP))
    print("\tThis is the probability of a bit being transmitted successfully.")
    print("Average invalid probability: " + str(average_IP))
    print("\tThis is the probability of a bit failing to be transmitted.")
    print("Average corruption probability: " + str(average_CP))
    print("\tThis is the probability of a bit being transmitted incorrectly.")
    
    return
    
def sendBoolBB84(input_bool, api, num_shots=1024, backend="simulator"):

    #Read QASM program
    filename = ""
    if (input_bool):
        filename = "BB84True.qasm"
    else:
        filename = "BB84False.qasm"
    fo = open(filename, "r")
    qasm = fo.read()
    fo.close()
    
    #Run the experiment
    output = api.run_experiment(qasm, backend=backend, shots=num_shots, name="sendBoolBB84", timeout=300)
    results = output["result"]["measure"]
    
    #Process the results
    Processed_results = {"Message": input_bool, "Shots": num_shots, "Success Probability": 0, "Invalid Probability": 0, "Corruption Probability" : 0}
    for index in range(0,len(results["labels"])):
        label = results["labels"][index]
        valid_measurement = (label[0] == label[1])
        measurement_result = (label[2] == "1")
        if (valid_measurement):
            if (measurement_result == input_bool):
                Processed_results["Success Probability"] += results["values"][index]
            else:
                Processed_results["Corruption Probability"] += results["values"][index]
        else:
            Processed_results["Invalid Probability"] += results["values"][index]
    return Processed_results

    
main()