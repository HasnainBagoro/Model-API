import re
import math
import tldextract
import urllib.parse
import numpy as np
import pandas as pd

# --- Feature Engineering Function ---
def shannon_entropy(s: str) -> float:
    if not s: return 0
    probs = [s.count(c)/len(s) for c in set(s)]
    return -sum(p * math.log2(p) for p in probs)

def extract_features(url: str) -> dict:
    try:
        parsed = urllib.parse.urlparse(url)
        host = parsed.netloc or ""
        path = parsed.path or ""
        query = parsed.query or ""
        scheme = parsed.scheme or ""

        features = {
            "url_length": len(url),
            "host_length": len(host),
            "path_length": len(path),
            "query_length": len(query),
            "digit_count": sum(c.isdigit() for c in url),
            "letter_count": sum(c.isalpha() for c in url),
            "special_count": sum(not c.isalnum() for c in url),
            "dot_count": url.count("."),
            "hyphen_count": url.count("-"),
            "at_count": url.count("@"),
            "question_count": url.count("?"),
            "equal_count": url.count("="),
            "slash_count": url.count("/"),
            "percent_count": url.count("%"),
            "colon_count": url.count(":"),
            "underscore_count": url.count("_"),
            "ampersand_count": url.count("&"),
            "param_count": url.count("&") + url.count("="),
            "subdir_count": path.count("/"),
            "entropy_url": shannon_entropy(url),
            "entropy_host": shannon_entropy(host),
            "entropy_path": shannon_entropy(path),
            "entropy_query": shannon_entropy(query),
            "is_https": 1 if scheme.lower()=="https" else 0,
            "shortener": 1 if re.search(r"bit\.ly|goo\.gl|tinyurl|ow\.ly", url) else 0,
            "ip_in_host": 1 if re.match(r"^\d+\.\d+\.\d+\.\d+$", host) else 0,
            "subdomain_count": host.count("."),
        }
        return features
    except:
        return {f:0 for f in ["url_length","host_length","path_length","query_length",
                              "digit_count","letter_count","special_count","dot_count",
                              "hyphen_count","at_count","question_count","equal_count",
                              "slash_count","percent_count","colon_count","underscore_count",
                              "ampersand_count","param_count","subdir_count","entropy_url",
                              "entropy_host","entropy_path","entropy_query","is_https",
                              "shortener","ip_in_host","subdomain_count"]}
