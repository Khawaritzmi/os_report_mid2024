def FCFS(proses):
    n = len(proses)
    proses.sort(key=lambda x: x[1])  # Urutkan berdasarkan waktu kedatangan
    waktu_tunggu = [0] * n
    waktu_penyelesaian = [0] * n
    waktu_selesai = 0
    
    for i in range(n):
        if waktu_selesai < proses[i][1]:
            waktu_selesai = proses[i][1]
        waktu_selesai += proses[i][2]
        waktu_penyelesaian[i] = waktu_selesai - proses[i][1]
        waktu_tunggu[i] = waktu_penyelesaian[i] - proses[i][2]
    
    rata_rata_waktu_tunggu = sum(waktu_tunggu) / n
    rata_rata_waktu_penyelesaian = sum(waktu_penyelesaian) / n
    
    return rata_rata_waktu_tunggu, rata_rata_waktu_penyelesaian

proses = [("P1", 0, 4), ("P2", 1, 3), ("P3", 2, 5), ("P4", 3, 2)]
rata_rata_waktu_tunggu, rata_rata_waktu_penyelesaian = FCFS(proses)
print(f"FCFS - Rata-rata Waktu Tunggu: {rata_rata_waktu_tunggu}, Rata-rata Waktu Penyelesaian: {rata_rata_waktu_penyelesaian}")