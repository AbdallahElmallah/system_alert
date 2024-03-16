import subprocess
import re
import sys


class SystemUtils:

    RAM_THRESHOLD_PERCENTAGE = 50
    STORAGE_THRESHOLD_PERCENTAGE = 50
    PATRONI_THRESHOLD_IN_MB = 0
    CPU_THRESHOLD_PERCENTAGE = 50
    @staticmethod
    @staticmethod
    def run_command(command):
        try:
            if sys.version_info >= (3, 7):
                result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
                
            if result.returncode == 0:
                return result.stdout
            else:
                return f"Error: {result.stderr}"
        except Exception as e:
            return f"Exception: {str(e)}"
    @staticmethod
    def get_ram_usage():
        return SystemUtils.run_command("free -m")

    @staticmethod
    def get_storage_usage():
        return SystemUtils.run_command("df -h /")
    
    @staticmethod
    def get_cpu_usage():
        cpu_info = SystemUtils.run_command("mpstat 1 1 | awk '$12 ~ /[0-9.]+/ { print 100 - $12 }'")
        cpu_lines = cpu_info.strip().split('\n')
        cpu_percentage = 0.0
        
        for line in cpu_lines:
            cpu_percentage += float(line)
        
        return cpu_percentage / len(cpu_lines)
    
    @staticmethod
    def parse_ram_usage(ram_info):
        total_match = re.search(r"Mem:\s+(\d+)\s+\d+", ram_info)
        used_match = re.search(r"Mem:\s+\d+\s+(\d+)", ram_info)

        if total_match and used_match:
            total = int(total_match.group(1))
            used = int(used_match.group(1))
            return total, used
        else:
            return 0, 0

    
    
