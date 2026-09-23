import hashlib
import hmac
import time
import secrets

SHARED_SECRET = b"my_super_secret_key"
used_nonces = set()

def generate_challenge():
    nonce = secrets.token_hex(8)
    timestamp = int(time.time())
    return nonce, timestamp

def create_response(username, nonce, timestamp, client_ip):
    message = f"{username}:{nonce}:{timestamp}:{client_ip}".encode('utf-8')
    return hmac.new(SHARED_SECRET, message, hashlib.sha256).hexdigest()

def verify_response(username, nonce, timestamp, client_ip, received_hmac, current_time):
    if nonce in used_nonces:
        return "REJECTED: Replay Attack Detected"
    
    if current_time - timestamp > 5:
        return "REJECTED: Request Expired"
    
    expected_message = f"{username}:{nonce}:{timestamp}:{client_ip}".encode('utf-8')
    expected_hmac = hmac.new(SHARED_SECRET, expected_message, hashlib.sha256).hexdigest()
    
    if not hmac.compare_digest(expected_hmac, received_hmac):
        return "REJECTED: Invalid HMAC or Wrong IP"
    
    used_nonces.add(nonce)
    return "SUCCESS: Authenticated"


user = "alice"
ip = "192.168.1.10"

nonce, ts = generate_challenge()
valid_hmac = create_response(user, nonce, ts, ip)

print("1. Normal Login:", verify_response(user, nonce, ts, ip, valid_hmac, time.time()))
print("2. Replay Attack:", verify_response(user, nonce, ts, ip, valid_hmac, time.time()))
print("3. Expired Request:", verify_response(user, nonce, ts, ip, valid_hmac, time.time() + 10))
print("4. Wrong IP Check:", verify_response(user, nonce, ts, "10.0.0.99", valid_hmac, time.time()))
