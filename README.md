## Soc Log Analyzer

This project analyzes authentication logs generated from a simulated enterprise environment. It identifies failed login attempts, suspicious users, blacklisted IPs, and generates a security report similar to what a SOC analyst would review.

## Features

- Analyze 1000+ authentication logs
- Count successful and failed logins
- Detect unique IP addresses
- Identify blacklisted IPs
- Detect suspicious users with multiple failed login attempts
- Calculate login success and failure rates
- Generate overall threat level (LOW / MEDIUM / HIGH / CRITICAL)

## Technologies Used

- Python
- MySQL
- Git
- GitHub

## Project Structure

SOC_Log_Analyzer/
├── analyzer.py
├── database.py
├── generate_logs.py
├── sample_logs.txt
├── report.txt
└── README.md

## How to Run

1. Clone the repository
2. Install Python
3. Run:

python analyzer.py

## Sample Output

SOC SECURITY REPORT

Total Logs Analyzed : 1000
Unique IP Addresses : 13
Successful Logins : 722
Failed Logins : 278
Blacklisted IPs : 5
Overall Threat Level : CRITICAL

## What I Learned

- Parsing log files using Python
- Using dictionaries to count login attempts
- Detecting suspicious login patterns
- Working with MySQL for storing log data
- Managing projects with Git and GitHub

## Future Improvements

- Real-time log monitoring
- Email alert system
- Web dashboard
- SIEM integration
- Threat intelligence API integration


## Author

Sujal Kumar