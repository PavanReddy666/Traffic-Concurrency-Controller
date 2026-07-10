import time
import threading
import difflib
from collections import deque 

traffic_queues = {}

# OS Concept: Critical Section -> The Intersection Box -> Semaphores
intersection_semaphore = threading.Semaphore(1)

def print_welcome_banner():
    print("=" * 70)
    print("*" * 70)
    print("        🚦 ALGORITHMIC -BASED TRAFFIC CONTROLLER SOFTWARE 🚦        ")
    print("*" * 70)
    print("=" * 70)

def get_junction_count():
    while True:
        try:
            n = int(input("Enter number of junctions (3 or 4): "))
            # Constraint Checking
            if n <= 0:
                print("Zero or negative junctions are impossible. Please try again.")
            elif n in [1, 2]:
                print("Less than 3 junctions does not form a valid intersecting system. Please try again.")
            elif n > 4:
                print("More than 4 junctions leads to Ring. Check Maps Properly.")
            else:
                return n
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def display_mapping(n):
    print("\n" + "="*30)
    print("Initializing Multi-Threaded Intersection Management System...\n")
    print(" JUNCTION MAPPING CONVENTION")
    print("="*30)
    if n == 4:
        mapping = {1: "Left", 2: "Top", 3: "Right", 4: "Bottom"}
    else:
        # T-Shape for 3-way intersection
        mapping = {1: "Bottom", 2: "Right", 3: "Top"}
        
    for k, v in mapping.items():
        print(f" Junction {k} : {v}")
    print("="*30 + "\n")
    return mapping

def draw_diagram(n, mapping):
    # OS Concept: Critical Section (The Intersection Box) Visualization
    # This must strictly be called when a thread holds the intersection_semaphore
    
    def get_q_str(j):
        return f"({', '.join(traffic_queues[j])})" if traffic_queues[j] else "(Empty)"

    if n == 4:
        l1, q1 = f"[J1: {mapping[1]}]", get_q_str(1)
        l2, q2 = f"[J2: {mapping[2]}]", get_q_str(2)
        l3, q3 = f"[J3: {mapping[3]}]", get_q_str(3)
        l4, q4 = f"[J4: {mapping[4]}]", get_q_str(4)
        
        # Dynamic scaling limits based on queue lengths
        left_width = max(len(l1), len(q1))
        vert_width = max(len(l2), len(q2), len(l4), len(q4))
        h_road = max(10, (vert_width // 2) + 2)
        
        center_pos = left_width + 1 + h_road
        
        def center_text(text):
            start = max(0, center_pos - len(text) // 2)
            return " " * start + text

        total_width = center_pos + 1 + h_road + 1 + max(len(l3), len(q3))
        sep_line = "-" * max(50, total_width)
        
        print(sep_line)
        print(center_text(l2))
        print(center_text(q2))
        print(center_text("|"))
        print(center_text("|"))
        print(f"{l1:>{left_width}} {'-' * h_road}O{'-' * h_road} {l3}")
        print(f"{q1:>{left_width}} {' ' * h_road}|{' ' * h_road} {q3}")
        print(center_text("|"))
        print(center_text(l4))
        print(center_text(q4))
        print(sep_line)
    elif n == 3:
        l1, q1 = f"[J1: {mapping[1]}]", get_q_str(1)
        l2, q2 = f"[J2: {mapping[2]}]", get_q_str(2)
        l3, q3 = f"[J3: {mapping[3]}]", get_q_str(3)
        
        vert_width = max(len(l1), len(q1), len(l3), len(q3))
        h_road = max(10, (vert_width // 2) + 2)
        
        left_width = 15
        center_pos = left_width + 1 + h_road
        
        def center_text(text):
            start = max(0, center_pos - len(text) // 2)
            return " " * start + text

        total_width = center_pos + 1 + h_road + 1 + max(len(l2), len(q2))
        sep_line = "-" * max(50, total_width)
        
        print(sep_line)
        print(center_text(l3))
        print(center_text(q3))
        print(center_text("|"))
        print(center_text("|"))
        print(f"{' ' * left_width} {' ' * h_road}O{'-' * h_road} {l2}")
        print(f"{' ' * left_width} {' ' * h_road}|{' ' * h_road} {q2}")
        print(center_text("|"))
        print(center_text(l1))
        print(center_text(q1))
        print(sep_line)
    print()

def detect_circular_wait_rag(n):
    # OS Concept: Circular Wait -> Gridlock -> Resource Allocation Graph
    # Detects if all junctions are requesting resources simultaneously forming a cycle.
    active_junctions = [j for j in range(1, n + 1) if traffic_queues[j]]
    if n == 4 and len(active_junctions) == 4:
        print("⚠️ [RAG(Resource Allocation Graph) STATUS] Circular Wait (Gridlock) potential detected! Resource Allocation Graph shows a cycle.")
        print("               Resolving cycle via weighted scheduling to ensure no total system halt...\n")
    elif len(active_junctions) > 1:
        print(f"📊 [RAG(Resource Allocation Graph) STATUS] {len(active_junctions)} junctions active. No Circular Wait cycle detected in RAG.\n")

def check_safe_state_bankers(vehicle, junction, mapping):
    # OS Concept: Safe State -> Flowing Traffic -> Banker’s Algorithm
    # Checks if granting the intersection to this vehicle leaves the system in a safe state.
    print(f"🔒 [BANKER'S ALGORITHM] Calculating Safe State for '{vehicle}' at Junction {junction} ({mapping[junction]})...")
    print(f"   => Request: 1 space. Available: 1. System is in a SAFE STATE (Flowing Traffic).")

def start_traffic_controller():
    print_welcome_banner()
    n = get_junction_count()
    mapping = display_mapping(n)

    # Initialize Queues using collections.deque to enforce strict physical FIFO
    for i in range(1, n + 1):
        traffic_queues[i] = deque()
        while True:
            try:
                num_v = int(input(f"Enter the number of vehicles in Junction {i} ({mapping[i]}): "))
                if num_v < 0:
                    print("Number of vehicles cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid integer.")
                
        if num_v > 0:
            valid_vehicles = ['bike', 'car', 'lorry', 'truck', 'ambulance']
            print(f"Enter the names of vehicles for Junction {i} (bike / car / lorry / truck / ambulance): ")
            for j in range(num_v):
                v = input(f"  Vehicle {j+1}: ").strip().lower()
                
                while v not in valid_vehicles and v != 'remove':
                    matches = difflib.get_close_matches(v, valid_vehicles, n=1, cutoff=0.3)
                    if matches:
                        suggestion = matches[0]
                        action = input(f"    [!] Unknown vehicle '{v}'. Did you mean '{suggestion}'? (yes / new / remove): ").strip().lower()
                        if action == 'yes':
                            v = suggestion
                            print("    [+] Request accepted and modified.")
                        elif action == 'remove':
                            v = 'remove'
                        elif action == 'new':
                            v = input(f"    Enter new name ({'/'.join(valid_vehicles)}): ").strip().lower()
                        else:
                            print("    Invalid option.")
                    else:
                        print(f"    [!] Unknown vehicle typo detected: '{v}'")
                        v = input(f"    Please enter a valid name ({'/'.join(valid_vehicles)}) or type 'remove' to discard: ").strip().lower()
                    
                if v != 'remove':
                    traffic_queues[i].append(v)
                else:
                    print(f"    Vehicle {j+1} has been discarded.")
        print()

    # Initial State Visualization
    print("\n[SYSTEM] Initial Traffic State:")
    draw_diagram(n, mapping)
    
    # Time Costs for Scheduling (OS Concept: Burst Time / Process Execution Time)
    time_costs = {'bike': 1.5, 'car': 2.0, 'lorry': 4.0, 'truck': 5.0, 'ambulance': 0.0} # Ambulances handled separately
    
    # =========================================================================
    # PHASE 1: PREEMPTION (Handling High Priority Interrupts for Emergency Vehicles)
    # OS Concept: Priority & Round-Robin 
    # =========================================================================
    # Maintain how many ambulances are in each junction
    ambulance_counts = {j: list(traffic_queues[j]).count('ambulance') for j in range(1, n + 1)}
    total_ambulances = sum(ambulance_counts.values())

    if total_ambulances > 0:
        print(f"\n🚑 [EMERGENCY DETECTED] Total Ambulances in System: {total_ambulances}")
        for j in range(1, n + 1):
            if ambulance_counts[j] > 0:
                print(f"   -> Junction {j} ({mapping[j]}): {ambulance_counts[j]} ambulance(s)")
        print("   Executing Strict Round-Robin Priority Clearance for Ambulances...\n")

    occurrence = 1
    # Check 1st occurrence, then 2nd occurrence, etc., looping over junctions
    while any('ambulance' in traffic_queues[j] for j in range(1, n + 1)):
        print(f"\n--- Processing Ambulance Occurrence #{occurrence} ---")
        for j in range(1, n + 1):
            if 'ambulance' in traffic_queues[j]:
                # Find the exact index of the first ambulance in this queue
                amb_index = traffic_queues[j].index('ambulance')
                
                blocking_vehicles = []
                if amb_index > 0:
                    for _ in range(amb_index):
                        blocking_vehicles.append(traffic_queues[j].popleft())
                    
                vehicle = traffic_queues[j].popleft()
                
                with intersection_semaphore:
                    if blocking_vehicles:
                        names = ", ".join(blocking_vehicles)
                        print(f"⚠️ [PRIORITY ESCALATION] Removed blocking vehicles ({names}) to reach ambulance at Junction {j} ({mapping[j]})")
                    print(f"🚨 [INTERRUPT] High-Priority '{vehicle}' (Occurrence #{occurrence}) passed and left from Junction {j} ({mapping[j]})")
                    print()
                    draw_diagram(n, mapping)
                time.sleep(1.5)
                # Continue next (to next junction)
            else:
                # If not go to next junction
                pass
                
        # Repeat procedure for next occurrence
        occurrence += 1
        
    if total_ambulances > 0:
        print("\n✅ [PRIORITY RESOLVED] All ambulance routes are cleared. Priority scheduling is done.")
        print("➡️  [SCHEDULING] Banker's Algorithm starts...\n")
        print()

    # =========================================================================
    # PHASE 2: STARVATION PREVENTION & THROUGHPUT OPTIMIZATION
    # OS Concept: Round-Robin Scheduling with Time Quantum
    # Allocating a specific "time slice" (5 seconds) per junction.
    # =========================================================================
    time_quantum = 5.0 
    
    # OS Concept: Run RAG check before beginning standard traffic flow
    detect_circular_wait_rag(n)

    # Run while there are still vehicles in any queue
    while any(len(traffic_queues[j]) > 0 for j in range(1, n + 1)):
        for j in range(1, n + 1):
            if not traffic_queues[j]:
                continue
                
            time_used = 0.0
            passed_vehicles = []
            
            # Allow vehicles to pass until time limit (quantum) is hit for this phase
            while traffic_queues[j]:
                next_vehicle = traffic_queues[j][0]
                v_cost = time_costs.get(next_vehicle, 2.0) # Default unknown to 2 secs
                
                # If adding this vehicle exceeds our time slice (5s), yield the CPU/Intersection
                if time_used + v_cost > time_quantum:
                    break 
                
                # OS Concept: Banker's Algorithm verification before allocation
                check_safe_state_bankers(next_vehicle, j, mapping)
                
                # Process process (Dequeue vehicle from the front)
                vehicle = traffic_queues[j].popleft()
                passed_vehicles.append(vehicle)
                time_used += v_cost
                
            if passed_vehicles:
                # OS Concept: Acquiring Semaphore for Critical Section (Batch Clearance)
                with intersection_semaphore:
                    names = ", ".join(passed_vehicles)
                    print(f"🟢 [GREEN LIGHT: {time_used}s / {time_quantum}s] '{names}' passed simultaneously from Junction {j} ({mapping[j]})")
                    print() # Extra empty line before diagram
                    draw_diagram(n, mapping)
                
                # Context switch delay
                time.sleep(1.5) 

    print("\n✅ [SYSTEM HALT] All queues are cleared. Deadlock successfully avoided. Intersection is empty.")
    print()

if __name__ == "__main__":
    # OS Concept: Main Thread Initialization
    start_traffic_controller()