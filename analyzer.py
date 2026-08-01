
with open("sample_logs.txt", "r") as file:
    logs = file.readlines()

success_count = 0
failed_count = 0
failed_ips = {}

print("========== LOG FILE ==========\n")

for log in logs:
    print(log.strip())

    if "SUCCESS" in log:
        success_count += 1

    elif "FAILED" in log:
        failed_count += 1

        ip = log.split("ip=")[1].strip()

        if ip in failed_ips:
            failed_ips[ip] += 1
        else:
            failed_ips[ip] = 1

print("\n========== SUMMARY ==========")
print("Successful Logins :", success_count)
print("Failed Logins     :", failed_count)

print("\n========== FAILED ATTEMPTS BY IP ==========")

for ip, count in failed_ips.items():
    print(ip, ":", count, "failed attempts")

print("\n========== BRUTE FORCE DETECTION ==========")

alert_found = False

for ip, count in failed_ips.items():

    if count >= 3:
        alert_found = True
        print("🚨 ALERT")
        print("IP Address :", ip)
        print("Failed Attempts :", count)
        print("Severity : HIGH")
        print("---------------------------")

if not alert_found:
    print("No brute force attack detected.")
    print("\n========== TOP ATTACKING IP ==========")

top_ip = None
max_attempts = 0

for ip, count in failed_ips.items():
    if count > max_attempts:
        max_attempts = count
        top_ip = ip

if top_ip:
    print("Most Suspicious IP :", top_ip)
    print("Failed Attempts    :", max_attempts)

    print("\n========== BRUTE FORCE DETECTION ==========\n")

top_ips = sorted(failed_ips.items(), key=lambda x: x[1], reverse=True)[:5]

for ip, attempts in top_ips:

    if attempts >= 5:

        print(f"🚨 ALERT: Possible Brute Force Attack")

        print(f"IP Address : {ip}")

        print(f"Failed Attempts : {attempts}")

        if attempts >= 20:
            severity = "CRITICAL"
        elif attempts >= 11:
            severity = "HIGH"
        elif attempts >= 5:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        print(f"Severity : {severity}")

        print("-" * 40)

        print("\n========== BLACKLISTED IPS ==========\n")

blacklisted_ips = []

for ip, attempts in top_ips:
    if attempts >= 5:
        blacklisted_ips.append(ip)

for i, ip in enumerate(blacklisted_ips, start=1):
    print(f"{i}. 🚫 {ip}")

print(logs[0])
print(type(logs[0]))

ip_addresses = []

for log in logs:
    ip = log.split("ip=")[1]
    ip_addresses.append(ip)

    print("\n========== SUSPICIOUS USERS ==========")

failed_users = {}

for log in logs:
    if "FAILED" in log:
        print(log)
        break

for log in logs:
    if "FAILED" in log:
        username = log.split("user=")[1].split()[0]

        if username not in failed_users:
            failed_users[username] = 1
        else:
            failed_users[username] += 1

for user, attempts in failed_users.items():
    if attempts >= 5:
        print(f"⚠️ {user} -> {attempts} failed attempts")

print("\n" + "=" * 50)
print("          SOC SECURITY REPORT")
print("=" * 50)

print(f"Total Logs Analyzed      : {len(logs)}")
print(f"Unique IP Addresses      : {len(set(ip_addresses))}")
print(f"Successful Logins        : {success_count}")
print(f"Failed Logins            : {failed_count}")
print(f"Blacklisted IPs          : {len(blacklisted_ips)}")

print("\nOverall Threat Level :", severity)

print("=" * 50)
print("Report Generated Successfully")
print("=" * 50)

success_rate = (success_count / len(logs)) * 100
failure_rate = (failed_count / len(logs)) * 100

print(f"login Success Rate             : {success_rate:.2f}%")
print(f"login Failure Rate             : {failure_rate:.2f}%")