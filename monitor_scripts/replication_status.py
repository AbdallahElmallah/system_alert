from utils.patroni_utils import check_replication_lag
from utils.script_utils import SystemUtils
from monitor_scripts.send_zoho_email import send_zoho_email
from utils.logging_utils import logging



def send_replication_lag_zoho_email():
    lag_value = check_replication_lag()
    if isinstance(lag_value, float): 
        if lag_value > SystemUtils.PATRONI_THRESHOLD_IN_MB:
            subject = "Replication Lag Alert"
            body = f"Replication lag detected: {lag_value} MB"
            send_zoho_email(subject, body)
        else:
            logging.info("Replication lag is within threshold.")
    else:
        logging.warning(lag_value)
