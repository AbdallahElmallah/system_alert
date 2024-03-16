import re
from utils.logging_utils import log_info, log_error

from monitor_scripts.send_zoho_email import send_zoho_email
from utils.script_utils import SystemUtils


def build_postgresql_status():
    postgresql_info = SystemUtils.run_command("systemctl status postgresql")
    
    status_match = re.search(r'Active:\s+(.*?)\(', postgresql_info)
    if status_match:
        status = status_match.group(1)
        if 'active' in status.lower():
            log_info("PostgreSQL service is active")
            
    else:
        log_error("Unable to determine PostgreSQL service status")
        send_zoho_email('=== PostgreSQL Status ===', 'Unable to determine PostgreSQL service status')

    
