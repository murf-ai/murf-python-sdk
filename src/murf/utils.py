import hmac
import hashlib
import time

def validate_hmac(secret: str, payload: str, timestamp_header: str, hmac_signature: str, tolerance_seconds: int):
    """
    Validate the HMAC signature of a payload against a secret key and timestamp.

    Args:
        secret (str): The secret key used for HMAC generation.
        payload (str): The payload to validate.
        timestamp_header (str): The timestamp header from the request.
        hmac_signature (str): The HMAC signature to validate against.
        tolerance_seconds (int): The allowed time tolerance in seconds.
    """
    try:
        received_timestamp = int(timestamp_header) 
        current_timestamp = int(time.time()) * 1000
        if (abs(current_timestamp - received_timestamp) / 1000) > tolerance_seconds:
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