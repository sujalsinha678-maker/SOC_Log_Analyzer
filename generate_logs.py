import random
from datetime import datetime, timedelta

users = [
    "admin", "root", "guest", "john", "alice",
    "bob", "mike", "sarah", "david", "raj",
    "alex", "tom", "james", "emma", "linda"
]

successful_ips = [
    "192.168.1.10",
    "192.168.1.15",
    "10.0.0.8",
    "172.16.0.5",
    "192.168.0.101",
    "192.168.0.102",
    "10.10.10.5",
    "172.20.10.8"
]

attack_ips = [
    "45.22.100.10",
    "103.45.67.88",
    "185.76.45.23",
    "91.210.34.55",
    "223.178.90.10"
]

start = datetime(2026,7,1,8,0,0)

logs = []

for i in range(1000):

    t = start + timedelta(minutes=i)

    if random.random() < 0.72:

        status = "SUCCESS"

        ip = random.choice(successful_ips)

    else:

        status = "FAILED"

        if random.random() < 0.35:
            ip = random.choice(attack_ips)
        else:
            ip = random.choice(successful_ips)

    user = random.choice(users)

    logs.append(
        f"{t.strftime('%Y-%m-%d %H:%M:%S')} {status} user={user} ip={ip}"
    )

with open("sample_logs.txt","w") as f:
    for log in logs:
        f.write(log+"\n")

print("1000 realistic logs generated successfully!")