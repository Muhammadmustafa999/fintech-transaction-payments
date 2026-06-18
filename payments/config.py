"""
Production Configuration — Fintech Service
"""
# SEC DJANGO-001: DEBUG=True
DEBUG = True

# SEC DJANGO-002: Wildcard hosts
ALLOWED_HOSTS = ['*']

# SEC: Hardcoded Stripe live key
STRIPE_SECRET_KEY = "sk_live_EXAMPLEKEYPATTERNFORDETECTION123456"

# SEC: Hardcoded JWT secret
JWT_SECRET = "jwt_weak_secret_123"

# SEC CRYPTO-003: DES encryption for card data
def encrypt_card(card_number):
    from Crypto.Cipher import DES
    key = b'8bytekey'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(card_number.encode()[:8])
