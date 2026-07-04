from collections import defaultdict

class DomainResolver:
    def __init__(self):
        self.ip_to_domain = defaultdict(set)
        self.domain_to_subdomain = defaultdict(set)
    
    def register_domain(self, ip, domain):
        self.ip_to_domain[ip].add(domain)
    
    def register_subdomain(self, domain, subdomain):
        self.domain_to_subdomain[domain].add(subdomain)
    
    def has_subdomain(self, ip, domain, subdomain):
        return domain in self.ip_to_domain[ip] and subdomain in self.domain_to_subdomain[domain]