from difflib import SequenceMatcher
from pathlib import Path
import re

# --------------------------------------------------
# BASE DIRECTORY
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------
# LOAD BRAND & KEYWORD FILES
# --------------------------------------------------
def load_list(filename):
    path = BASE_DIR / "data" / filename
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip().lower() for line in f if line.strip()]

BRANDS = {
    "tier1": load_list("brands_tier1.txt"),
    "tier2": load_list("brands_tier2.txt"),
    "tier3": load_list("brands_tier3.txt"),
}

KEYWORDS = load_list("keywords.txt")

# --------------------------------------------------
# NORMALIZATION LOGIC
# --------------------------------------------------
LEET_MAP = {
    "0": "o",
    "1": "l",
    "3": "e",
    "4": "a",
    "5": "s",
    "7": "t"
}

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def normalize_domain(domain):
    """
    Normalize domain safely.
    Returns normalized base domain OR None if invalid format.
    """

    domain = domain.lower().strip()

    # Remove protocol
    domain = domain.replace("http://", "").replace("https://", "")

    # Remove www.
    if domain.startswith("www."):
        domain = domain[4:]

    # Reject invalid characters (like @, space, unicode tricks)
    if not re.match(r"^[a-z0-9.-]+$", domain):
        return None

    base = domain.split(".")[0]
    base = base.replace("-", "")

    normalized = ""
    for c in base:
        normalized += LEET_MAP.get(c, c)

    # Typographic homoglyphs
    normalized = normalized.replace("rn", "m")
    normalized = normalized.replace("vv", "w")

    return normalized

# --------------------------------------------------
# MAIN ANALYSIS FUNCTION (RULE-BASED)
# --------------------------------------------------
def analyze_domain(domain):
    reasons = []
    keyword_count = 0
    brand_detected = False

    normalized = normalize_domain(domain)

    # -------- Invalid Domain Handling --------
    if normalized is None:
        return 20, ["Invalid or suspicious domain format detected"]

    # -------- Brand Detection --------
    for tier, brands in BRANDS.items():
        for brand in brands:
            if brand in normalized or similarity(brand, normalized) >= 0.75:
                brand_detected = True
                reasons.append(f"{tier.upper()} brand impersonation detected: {brand}")
                break
        if brand_detected:
            break

    # -------- Keyword Detection --------
    for word in KEYWORDS:
        if word in domain.lower():
            keyword_count += 1
            reasons.append(f"Contains keyword: {word}")

    # -------- FINAL RISK LOGIC --------
    if brand_detected and keyword_count >= 2:
        score = 90      # HIGH
        reasons.append("Strong phishing intent detected")

    elif brand_detected:
        score = 50      # MEDIUM

    elif keyword_count >= 2:
        score = 40      # MEDIUM

    else:
        score = 10      # LOW

    return score, reasons
