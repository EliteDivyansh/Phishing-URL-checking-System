# feature.py
import re
from urllib.parse import urlparse

SHORTENERS = [
    "bit.ly","tinyurl","goo.gl","ow.ly","t.co","bit.do","adf.ly","buff.ly","shorturl.at",
    "tiny.cc","is.gd","shorte.st","trib.al","clk.im"
]
SUSPICIOUS_KEYWORDS = [
    "secure","account","update","login","verify","confirm","bank","ebay","paypal",
    "signin","wp-admin","webscr"
]

class FeatureExtraction:
    def __init__(self, url: str):
        self.url = url.strip()
        if not self.url:
            self.url = ""
        # ensure scheme exists for parsing
        if self.url and not re.match(r"^https?://", self.url):
            self.url = "http://" + self.url
        try:
            self.parsed = urlparse(self.url)
        except:
            self.parsed = None

    def has_ip(self):
        """Return True if URL contains an IP address instead of domain"""
        try:
            host = self.parsed.netloc
            # IPv4 pattern
            if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", host.split(':')[0]):
                return True
            return False
        except:
            return False

    def has_at_symbol(self):
        return "@" in self.url

    def is_long(self):
        return len(self.url) > 75

    def uses_shortener(self):
        for s in SHORTENERS:
            if s in self.url.lower():
                return True
        return False

    def missing_https(self):
        # if scheme exists and not https -> suspicious
        return self.parsed and self.parsed.scheme != "https"

    def many_subdomains(self):
        try:
            host = self.parsed.hostname or ""
            # count dots
            return host.count('.') >= 3
        except:
            return False

    def suspicious_keywords(self):
        p = (self.parsed.path or "") + (self.parsed.netloc or "")
        p = p.lower()
        for kw in SUSPICIOUS_KEYWORDS:
            if kw in p:
                return True
        return False

    def score(self):
        """
        Compute a simple score (0..1) where higher = safer.
        Start at 100 and subtract points for suspicious cues.
        """
        score = 100.0
        # strong signals (big penalties)
        if self.has_ip(): score -= 40
        if self.has_at_symbol(): score -= 20
        if self.uses_shortener(): score -= 20
        if self.is_long(): score -= 10
        # medium signals
        if self.many_subdomains(): score -= 8
        if self.suspicious_keywords(): score -= 10
        if self.missing_https(): score -= 10

        # clamp between 0..100
        if score < 0: score = 0.0
        if score > 100: score = 100.0
        return score / 100.0  # return 0..1

    def getFeaturesList(self):
        # kept for compatibility; returns list of raw features (optional)
        return [
            int(self.has_ip()),
            int(self.has_at_symbol()),
            int(self.is_long()),
            int(self.uses_shortener()),
            int(self.many_subdomains()),
            int(self.suspicious_keywords()),
            int(self.missing_https())
        ]
