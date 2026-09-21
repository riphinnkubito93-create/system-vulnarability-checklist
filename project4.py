def vulnerability_checklist():
    print("--- System Vulnerability Checklist ---")
    print("Please answer the following questions (yes/no):\n")
    vulnerabilities = []
    weak_pass = input("1. Do you use the same password across multiple accounts? (yes/no): ").lower()
    if weak_pass == 'yes':
        vulnerabilities.append("Weak Password Practice: Reusing passwords increases risk.")
    outdated_software = input("2. Is your operating system or software overdue for updates? (yes/no): ").lower()
    if outdated_software == 'yes':
        vulnerabilities.append("Outdated Software: Unpatched systems are vulnerable to known exploits.")
    unsafe_browsing = input("3. Do you click links or download files from unknown senders? (yes/no): ").lower()
    if unsafe_browsing == 'yes':
        vulnerabilities.append("Unsafe User Practice: High risk of phishing or malware infection.")
    print("\n--- Risk Assessment Report ---")
    if not vulnerabilities:
        print("Status: Secure. No major basic vulnerabilities detected.")
    else:
        print(f"Status: Vulnerable. Found {len(vulnerabilities)} issue(s):")
        for issue in vulnerabilities:
            print(f"- {issue}")
        print("\nRecommendation: Address these issues immediately to improve system security.")
vulnerability_checklist()