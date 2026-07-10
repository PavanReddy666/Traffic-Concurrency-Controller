# 🚦 Traffic Concurrency Controller

![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![OS Concepts](https://img.shields.io/badge/OS_Concurrency-Multi--Threading-blue?style=for-the-badge)

## 📖 About the Project
The **Traffic Concurrency Controller** is a multi-threaded system designed to simulate and manage complex intersection traffic flow. Built to demonstrate advanced Operating System concurrency concepts, this project ensures smooth execution of vehicle threads while strictly preventing deadlocks, race conditions, and thread starvation. 

This simulation models real-world constraints where multiple processes (vehicles) must safely share limited resources (intersection zones) without colliding or causing system halts.

## ⚙️ Algorithms & Core Concepts
This project relies on several key concurrency control mechanisms to manage traffic safely:

* **Resource Allocation & Deadlock Prevention:** [Explain your approach here. e.g., Implemented a strict resource ordering protocol to ensure vehicles claiming intersection zones cannot form a circular wait state.]
* **Thread Synchronization:** Utilizes [Locks / Semaphores / Monitors] to guarantee mutual exclusion when a thread enters a critical section (the intersection).
* **Scheduling Logic:** [Explain how you decide who goes next. e.g., Applied a First-Come-First-Serve (FCFS) queue alongside a starvation-prevention mechanism for heavy-traffic lanes.]

## 🛠️ Implementation Details
The simulation is built entirely in **Java**, leveraging its built-in concurrency libraries. 

* **Threads & Runnables:** Each vehicle is instantiated as an independent thread simulating its lifecycle (arrival, waiting, crossing, exiting).
* **Concurrency Utilities:** Heavily utilized `java.util.concurrent` [or `synchronized` blocks / `wait()` and `notifyAll()`] to manage thread states and state transitions efficiently.
* **Shared State Management:** The intersection acts as a shared resource matrix, with strict access protocols to maintain thread safety across concurrent reads and writes.

## 🚀 Setup Procedure
Follow these instructions to compile and run the simulation on your local machine.

### Prerequisites
* Java Development Kit (JDK) 8 or higher installed on your system.

### Installation & Execution
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sathwikchilapuram1-hue/Traffic-Concurrency-Controller.git](https://github.com/sathwikchilapuram1-hue/Traffic-Concurrency-Controller.git)
   cd Traffic-Concurrency-Controller
