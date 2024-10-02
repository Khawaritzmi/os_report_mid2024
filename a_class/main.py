class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0

def fcfs(processes):
    time = 0
    for p in processes:
        if time < p.arrival_time:
            time = p.arrival_time
        p.waiting_time = time - p.arrival_time
        time += p.burst_time
        p.completion_time = time

def sjn(processes):
    time = 0
    remaining = processes.copy()
    completed = []
    
    while remaining:
        available = [p for p in remaining if p.arrival_time <= time]
        if not available:
            time += 1
            continue
        
        next_process = min(available, key=lambda p: p.burst_time)
        next_process.waiting_time = time - next_process.arrival_time
        time += next_process.burst_time
        next_process.completion_time = time
        remaining.remove(next_process)
        completed.append(next_process)
    
    return completed

def round_robin(processes, quantum):
    time = 0
    remaining = processes.copy()
    queue = []
    
    while remaining or queue:
        # Tambahkan proses yang baru tiba ke antrian
        new_arrivals = [p for p in remaining if p.arrival_time <= time and p not in queue]
        queue.extend(new_arrivals)
        for p in new_arrivals:
            remaining.remove(p)
        
        if not queue:
            time += 1
            continue
        
        current_process = queue.pop(0)
        if current_process.remaining_time <= quantum:
            time += current_process.remaining_time
            current_process.completion_time = time
            current_process.waiting_time += time - current_process.arrival_time - current_process.burst_time
        else:
            time += quantum
            current_process.remaining_time -= quantum
            current_process.waiting_time += time - current_process.arrival_time - (current_process.burst_time - current_process.remaining_time)
            
            # Tambahkan proses yang baru tiba selama eksekusi quantum
            new_arrivals = [p for p in remaining if p.arrival_time <= time and p not in queue]
            queue.extend(new_arrivals)
            for p in new_arrivals:
                remaining.remove(p)
            
            queue.append(current_process)

def calculate_averages(processes):
    avg_waiting_time = sum(p.waiting_time for p in processes) / len(processes)
    avg_turnaround_time = sum(p.completion_time - p.arrival_time for p in processes) / len(processes)
    return avg_waiting_time, avg_turnaround_time

# Data proses
processes = [
    Process("P1", 0, 10),
    Process("P2", 1, 4),
    Process("P3", 3, 2),
    Process("P4", 5, 1)
]

# FCFS
fcfs_processes = [Process(p.pid, p.arrival_time, p.burst_time) for p in processes]
fcfs(fcfs_processes)
fcfs_avg_waiting, fcfs_avg_turnaround = calculate_averages(fcfs_processes)

# SJN
sjn_processes = [Process(p.pid, p.arrival_time, p.burst_time) for p in processes]
sjn_completed = sjn(sjn_processes)
sjn_avg_waiting, sjn_avg_turnaround = calculate_averages(sjn_completed)

# Round Robin
rr_processes = [Process(p.pid, p.arrival_time, p.burst_time) for p in processes]
round_robin(rr_processes, 2)
rr_avg_waiting, rr_avg_turnaround = calculate_averages(rr_processes)

print("Algoritma | Waktu Tunggu Rata-rata | Waktu Penyelesaian Rata-rata")
print(f"FCFS      | {fcfs_avg_waiting:.2f}                | {fcfs_avg_turnaround:.2f}")
print(f"SJN       | {sjn_avg_waiting:.2f}                | {sjn_avg_turnaround:.2f}")
print(f"RR (q=2)  | {rr_avg_waiting:.2f}                | {rr_avg_turnaround:.2f}")