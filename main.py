import json
import platform
import socket
from checks.antivirus_check import check_antivirus
from checks.cis_check import check_password_policy
from checks.firewall_status import get_firewall_status

def run_all_checks():
    result = {
        "hostname": socket.gethostname(),
        "os": platform.system() + " " + platform.release()
    }

    result.update(check_antivirus())

    result.update(check_password_policy())

    result.update(get_firewall_status())

    with open("results/compliance_results.json", "w") as f:
        json.dump(result, f, indent=4)

    print("Compliance checks completed. Results saved in results/compliance_results.json")

if __name__ == "__main__":
    run_all_checks()
