# 🚦 Traffic Concurrency Controller

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OS Concepts](https://img.shields.io/badge/OS_Concurrency-Multi--Threading-blue?style=for-the-badge)

## 📖 About the Project
The **Traffic Concurrency Controller** is a multi-threaded system designed to simulate and manage complex intersection traffic flow. Built to demonstrate advanced Operating System concurrency concepts, this project ensures smooth execution of vehicle threads while strictly preventing deadlocks, race conditions, and thread starvation. 

This simulation models real-world constraints where multiple processes (vehicles) must safely share limited resources (intersection zones) without colliding or causing system halts.

## ⚙️ Algorithms & Core Concepts
This project relies on several key concurrency control mechanisms to manage traffic safely:

* **Resource Allocation & Deadlock Prevention:** Implemented a strict resource ordering protocol to ensure vehicles claiming intersection zones cannot form a circular wait state.
* **Thread Synchronization:** Utilizes concurrency primitives like `Locks` and `Semaphores` to guarantee mutual exclusion when a thread enters a critical section (the intersection).
* **Scheduling Logic:** Applied a First-Come-First-Serve (FCFS) queue alongside a starvation-prevention mechanism to ensure heavy-traffic lanes do not indefinitely block other vehicles.

## 🛠️ Implementation Details
The simulation is built entirely in **Python**, leveraging its standard libraries to handle concurrent execution.

* **Threads & Execution:** Each vehicle is instantiated as an independent thread using Python's `threading.Thread`, simulating its lifecycle (arrival, waiting, crossing, exiting).
* **Concurrency Utilities:** Heavily utilized `threading.Lock()` and `threading.Condition()` to manage thread states, state transitions, and safe resource sharing efficiently.
* **Shared State Management:** The intersection acts as a shared resource matrix, with strict access protocols to maintain thread safety across concurrent reads and writes, carefully accounting for Python's Global Interpreter Lock (GIL) mechanics.

## 🚀 Setup Procedure
Follow these instructions to run the simulation on your local machine.

### Prerequisites
* **Python 3.x** installed on your system. 

### Installation & Execution
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sathwikchilapuram1-hue/Traffic-Concurrency-Controller.git](https://github.com/sathwikchilapuram1-hue/Traffic-Concurrency-Controller.git)
   cd Traffic-Concurrency-Controller

Built by [sathwikchilapuram](https://github.com/sathwikchilapuram) , [PavanReddy666](https://github.com/PavanReddy666) and [partheevg03](https://github.com/partheevg03)
