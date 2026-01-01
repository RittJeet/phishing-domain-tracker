import requests

def fetch_domains():
    print("Fetching public domain data (OSINT)...")

    url = "https://crt.sh/?q=%25&output=json"
    headers = {
        "User-Agent": "Mozilla/5.0 (OSINT Research Project)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)

        if response.status_code != 200:
            print(f"Failed to fetch data. HTTP Status: {response.status_code}")
            return []

        try:
            data = response.json()
        except ValueError:
            print("Received non-JSON response from crt.sh (likely rate-limited).")
            return []

        domains = set()

        for entry in data:
            name = entry.get("name_value", "")
            for d in name.split("\n"):
                if "*" not in d:
                    domains.add(d.lower())

        print(f"Collected {len(domains)} domains")
        return list(domains)

    except requests.exceptions.RequestException as e:
        print("Network error while fetching OSINT data:", e)
        return []
