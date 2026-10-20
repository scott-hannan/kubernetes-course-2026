from datetime import datetime, timezone
import secrets
import string
import time

SLEEP_TIME=5
STRING_LEN=12

def generate_random_string(length:int=12):
     characters = string.ascii_letters + string.digits
     random_string = ''.join(secrets.choice(characters) for _ in range(length))
     return random_string
            
def log_with_timestamp(string:str):
    now = datetime.now(timezone.utc)
    timestamp = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    print(f"{timestamp}: {string}")


if __name__ == "__main__":
    generated_string = generate_random_string(length=STRING_LEN)
    while(True):
        log_with_timestamp(generated_string)
        time.sleep(SLEEP_TIME)
        
    
