import subprocess
import re

def extract_value(pattern, text):
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    return "Not Found"

def check_password_policy():
    try:
        output = subprocess.check_output("net accounts", shell=True, text=True)

        min_length = extract_value(r"Minimum password length:\s+(\d+)", output)
        max_age = extract_value(r"Maximum password age \(days\):\s+(\d+)", output)
        lockout = extract_value(r"Lockout threshold:\s+(\d+)", output)

        return {
            "minimum_password_length": min_length,
            "maximum_password_age_days": max_age,
            "account_lockout_threshold": lockout
        }

    except Exception as e:
        return {"password_policy_error": str(e)}
