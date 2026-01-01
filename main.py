from src.detector import analyze_domain
from src.scorer import classify_risk
import json

def get_valid_domain():
    while True:
        domain = input("Enter domain (example: paypa1-login-secure.com): ").strip().lower()

        if domain in ["", "y", "n"]:
            print("❌ Invalid domain. Try again.")
            continue

        if "." not in domain:
            print("❌ Domain must contain a dot (.)")
            continue

        if domain.startswith("http"):
            domain = domain.replace("https://", "").replace("http://", "")

        return domain

print("=== OSINT Phishing Domain Tracker ===")

choice = input("Do you want to analyze a domain manually? (y/n): ").strip().lower()

results = []

if choice == "y":
    domain = get_valid_domain()

    score, reasons = analyze_domain(domain)
    risk = classify_risk(score)

    print("\nAnalysis Result")
    print("----------------")
    print(f"Domain     : {domain}")
    print(f"Risk Level : {risk}")

    if reasons:
        for r in reasons:
            print(f" - {r}")
    else:
        print(" - No suspicious patterns detected")

    results.append({
        "domain": domain,
        "score": score,
        "risk": risk,
        "reasons": reasons
    })

else:
    print("Manual analysis skipped.")

with open("data/results.json", "w") as f:
    json.dump(results, f, indent=2)

print("\nResults saved to data/results.json")
