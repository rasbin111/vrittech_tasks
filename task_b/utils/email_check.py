import re
from dns import resolver
from smtplib import SMTP

def validate_email(email: str):
    """ 
    Rules for email validation:
    -  should have: username, "@", domain 
    - username: 1. letters, numbers, periods, underscores and dashes
                2. dot(.) can't be used at the beginning or at end 
                3. no consecutive dots(.) like a..b@gmail.com (invalid)
    - domain: 1. consists of parts seperated by a dot
                   2. the second part must be at least two characters. For eg: .com, .org, .cc
                   3. allowed characters: -, a-z, 0-9 and dashes(-) can't be used at the beginning or end
    """
    if "@" not in email: 
        return False
    
    match = re.search(r"^[a-z0-9]+\.?\-*\_*[a-z0-9]+@[a-z0-9]+(\.[a-z0-9]{2,}){1,}$", email)
    print(match)
    if match:
        return True
    else:
        return False

def check_mx_records(domain: str):
    """ check if domain has valid MX records """
    try:
        answers = resolver.resolve(domain, "MX")
        mx_records = [r.exchange.to_text() for r in answers]
        return mx_records
    except Exception:
        return []

def check_smtp(email: str, mx_records: list):
    """ check if email exists in mx_records """
    for mx in mx_records:
        try:
            server = SMTP(timeout=10)
            server.connect(mx)
            server.helo(server.local_hostname)
            server.mail(email)
            code, message = server.rcpt(email)
            server.quit()
            print(code, message)
            if code == 250:
                return True
        except Exception:
            pass
    return False
