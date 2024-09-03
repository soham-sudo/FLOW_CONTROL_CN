# Flow Control Mechanisms for Data Link Layer in Python

## Overview
This project implements various flow control mechanisms at the Data Link Layer in Python. It features a Sender and a Receiver program that communicate over a simulated channel. The channel is capable of introducing delays and errors, mimicking real-world network conditions. The project showcases three primary flow control techniques: Stop and Wait, Go-Back-N ARQ, and Selective Repeat ARQ.

## Features
- **Flow Control Techniques**: Implementation of Stop and Wait, Go-Back-N ARQ, and Selective Repeat ARQ.
- **Data Framing**: Structured data frames with headers, payload, and trailers, including error detection using CRC/Checksum.
- **Error and Delay Simulation**: The channel can introduce random delays and bit errors during transmission.
- **Multithreading**: The Sender and Receiver programs run on separate threads, simulating asynchronous communication.
- **Socket Simulation**: The communication channel acts as a socket, managing data transfer with error handling.

## Project Structure
.
├── sender.py          # Implementation of the Sender program
├── receiver.py        # Implementation of the Receiver program
├── channel.py         # Channel simulation with error and delay features
├── crc_checksum.py    # CRC/Checksum implementation for error detection
├── README.md          # Project documentation

## Getting Started
Prerequisites

    Python 3.x
    Familiarity with basic networking concepts and Python threading

Installation

    Clone this repository:

    bash

git clone https://github.com/yourusername/datalink-layer-flow-control.git

## Navigate to the project directory:

bash

    cd datalink-layer-flow-control

Running the Project

    Start the Receiver program:

    bash

python receiver.py

Start the Sender program:

bash

    python sender.py

## Detailed Components
### Framing
  Framing(): Prepares a data frame with a header (source/destination MAC addresses, length, sequence number), payload (data), and a trailer (CRC/Checksum) for error detection.

### Channel
  Channel(): Simulates the transmission channel with threading, introducing potential delays and errors during data transmission.

### Sender
  Send(): Sends data frames from the Sender to the Receiver and handles retransmissions in case of errors or timeouts.
  Timer() and Timeout(): Manages transmission timing, detecting when a retransmission is necessary.

### Receiver
  Recv(): Receives and checks data frames for errors, sends acknowledgments back to the Sender.

### Flow Control Techniques
  Stop and Wait:
      Sender transmits one frame, waits for an acknowledgment, and retransmits if no ACK is received after a timeout.
  Go-Back-N ARQ:
      Sender can send multiple frames up to a specified window size (N). A cumulative acknowledgment is used, and all frames within the window are retransmitted in case of an error.
  Selective Repeat ARQ:
      Both Sender and Receiver manage windows of size N. Receiver can acknowledge and buffer out-of-order frames, and the Sender retransmits only unacknowledged frames.

### Testing and Evaluation

The project includes testing scenarios to evaluate the performance of each flow control technique:
    No Errors: Efficiency analysis under ideal conditions.
    With Errors: Performance comparison with varying error probabilities (0.1 to 0.5), including delays and frame losses.
