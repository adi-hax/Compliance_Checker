import subprocess

def check_antivirus():
    try:
        command = 'powershell "Get-CimInstance -Namespace \\"root\\SecurityCenter2\\" -ClassName AntivirusProduct | Select-Object displayName"'
        output = subprocess.check_output(command, shell=True, text=True)

        antivirus_installed = []

        for line in output.strip().split("\n"):
            if line.strip() and "displayName" not in line:
                antivirus_installed.append(line.strip())

        if antivirus_installed:
            return {"antivirus": "Installed", "antivirus_names": antivirus_installed}
        else:
            return {"antivirus": "Not Found", "antivirus_names": []}
    except Exception as e:
        return {"antivirus": "Error", "antivirus_error": str(e)}
