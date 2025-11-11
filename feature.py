import re
from urllib.parse import urlparse

class FeatureExtraction:
    def __init__(self, url):
        self.url = url.strip()
        if not self.url.startswith(("http://", "https://")):
            self.url = "http://" + self.url
        self.parsed = urlparse(self.url)

    def has_ip(self):
        return bool(re.match(r'^\d{1,3}(\.\d{1,3}){3}$', self.parsed.netloc.split(':')[0]))

    def uses_shortener(self):
        shorteners = ['bit.ly', 'tinyurl', 'goo.gl', 't.co', 'ow.ly', 'adf.ly']
        return any(s in self.url for s in shorteners)

    def suspicious_keywords(self):
        keywords = ['secure', 'login', 'update', 'free', 'account', 'bank', 'paypal', 'verify', 'signin']
        return any(k in self.url.lower() for k in keywords)

    def many_subdomains(self):
        return self.parsed.netloc.count('.') >= 3

    def missing_https(self):
        return self.parsed.scheme != "https"

    def is_long(self):
        return len(self.url) > 80

    def score(self):
        score = 100

        if self.has_ip(): score -= 60
        if self.uses_shortener(): score -= 50
        if self.suspicious_keywords(): score -= 40
        if self.many_subdomains(): score -= 30
        if self.missing_https(): score -= 20
        if self.is_long(): score -= 15

        score = max(0, min(100, score))
        return score / 100.0
