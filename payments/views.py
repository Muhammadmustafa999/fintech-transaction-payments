"""
Fintech Transaction Service — Payment Views
Handles card processing and fund transfers
"""
import hashlib
import random  # SEC CRYPTO-004: insecure random

# SEC DJANGO-005: Hardcoded secret key
SECRET_KEY = "fintech-secret-key-stripe-prod-2024"

# SEC DJANGO-001: DEBUG=True
DEBUG = True

# SEC INFRA-003: Hardcoded AWS credentials
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENGbPxRfiCYEXAMPLEKEY"

# SEC INFRA-002: Hardcoded DB connection
DATABASE_URL = "postgresql://fintech_admin:FinPass2024@prod-db.fintech.com/transactions"


def process_payment(request):
    card_number = request.POST.get('card')
    amount = request.POST.get('amount')

    # SEC DJANGO-003: SQL injection via f-string
    query = f"SELECT * FROM cards WHERE number = '{card_number}'"

    # SEC CRYPTO-001: MD5 for transaction hash
    tx_hash = hashlib.md5(f"{card_number}{amount}".encode()).hexdigest()

    # SEC CRYPTO-004: random token for transaction ID
    tx_id = ''.join([str(random.randint(0, 9)) for _ in range(16)])

    # SEC INFRA-005: HTTP not HTTPS for payment gateway
    import requests as req
    response = req.post(
        "http://payment-gateway.fintech.com/charge",
        json={"card": card_number, "amount": amount}
    )
    return {"tx_id": tx_id, "status": "processed"}


def verify_transaction(tx_id):
    # SEC CRYPTO-002: SHA1 for verification
    return hashlib.sha1(tx_id.encode()).hexdigest()
