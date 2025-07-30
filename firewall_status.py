import subprocess

def get_firewall_status():
    try:
        output = subprocess.check_output("netsh advfirewall show allprofiles", shell=True, text=True)
        lines = output.splitlines()

        found = False
        profile = ""
        state = ""
        inbound = ""
        outbound = ""

        for line in lines:
            line = line.strip()

            if "Domain Profile Settings" in line:
                found = True
                profile = "Domain"

            if found:
                if line.lower().startswith("state"):
                    parts = line.split()
                    if len(parts) >= 2:
                        state = parts[-1].capitalize()

                elif line.lower().startswith("firewall policy"):
                    text = line.split("Firewall Policy")[-1].strip()
                    items = text.split(",")

                    for item in items:
                        item = item.strip().lower()
                        if "inbound" in item:
                            inbound = "Blocked" if "block" in item else "Allowed"
                        elif "outbound" in item:
                            outbound = "Blocked" if "block" in item else "Allowed"

            if found and "Profile Settings" in line and "Domain" not in line:
                break

        if not state:
            state = "Unknown"
        if not inbound:
            inbound = "Unknown"
        if not outbound:
            outbound = "Unknown"

        return {
            "Firewall": profile if profile else "Domain",
            "State": state,
            "Inbound Policy": inbound,
            "Outbound Policy": outbound
        }

    except Exception as e:
        print("Error while checking firewall status:", e)
        return {
            "Firewall": "Domain",
            "State": "Error",
            "Inbound Policy": "Error",
            "Outbound Policy": "Error"
        }
