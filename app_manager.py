from monitor_scripts.postgresql_status import build_postgresql_status
from monitor_scripts.replication_status import send_replication_lag_zoho_email
from utils import logging_utils
from monitor_scripts.resource_status import check_resource_usage


def run_application():
    
    logging_utils.configure_logging()
    check_resource_usage()
    build_postgresql_status()
    send_replication_lag_zoho_email()
