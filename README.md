\# OSINT-Powered Phishing Domain Tracker



A defensive cybersecurity project that detects suspicious phishing domains using passive OSINT techniques.  

The tool analyzes domain names for brand impersonation, phishing intent, and evasion patterns, and classifies risk as \*\*LOW\*\*, \*\*MEDIUM\*\*, or \*\*HIGH\*\*.



---



\## 🔍 Features



\- Tier-based brand impersonation detection (Tier 1 / Tier 2 / Tier 3)

\- Leetspeak and typographic homoglyph normalization

\- Keyword-based phishing intent analysis

\- Rule-based risk classification (LOW / MEDIUM / HIGH)

\- Input sanitization for malformed or deceptive domains

\- Explainable output with clear detection reasons

\- Passive OSINT only (no active interaction)



---



\## 🛡️ Ethical Scope



This project is strictly defensive and ethical.



\- Passive OSINT only

\- No scanning of live websites

\- No brute-force or exploitation

\- No interaction with phishing pages

\- No collection of private or sensitive user data



---



\## 🧠 Detection Logic



The domain classification is rule-based:



\- \*\*HIGH Risk\*\*

&nbsp; - Brand impersonation detected \*\*and\*\*

&nbsp; - Strong phishing intent (two or more phishing keywords)



\- \*\*MEDIUM Risk\*\*

&nbsp; - Brand impersonation with weak phishing intent  

&nbsp; - OR multiple phishing keywords without a brand



\- \*\*LOW Risk\*\*

&nbsp; - No brand impersonation

&nbsp; - No phishing intent indicators



This logic is designed to reduce false positives while maintaining detection accuracy.



---



\## 📁 Project Structure



```

phishing-domain-tracker/

├── src/

│   └── detector.py          # Core detection logic

├── data/

│   ├── brands\_tier1.txt     # High-priority brands

│   ├── brands\_tier2.txt     # Medium-priority brands

│   ├── brands\_tier3.txt     # Regional/custom brands

│   ├── keywords.txt         # Phishing intent keywords

│   └── results.json         # Analysis output

├── main.py                  # CLI entry point

├── README.md

├── requirements.txt

├── .gitignore

└── LICENSE

```



