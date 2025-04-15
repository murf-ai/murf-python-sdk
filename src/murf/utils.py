import hmac
import hashlib
import time

def validate_hmac(secret: str, payload: str, timestamp_header: str, hmac_signature: str, tolerance_seconds: int):
    try:
        received_timestamp = int(timestamp_header)
        current_timestamp = int(time.time())
        if abs(current_timestamp - received_timestamp) > tolerance_seconds:
            print("Timestamp is outside the allowed tolerance window.")
            return False
        data_to_sign = f"{payload}.{timestamp_header}"
        calculated_hmac = hmac.new(
            secret.encode('utf-8'),
            data_to_sign.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        return hmac.compare_digest(calculated_hmac, hmac_signature)
    except Exception as e:
        print(f"Error validating HMAC: {e}")
        return False