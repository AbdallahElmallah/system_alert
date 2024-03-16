from utils.script_utils import SystemUtils
from utils.logging_utils import logging



def check_replication_lag():
    patronictl_command = "sudo patronictl -c /etc/patroni/patroni.yml list"
    patronictl_output = SystemUtils.run_command(patronictl_command)

    if "Lag (MB)" in patronictl_output:
        lag_column_index = patronictl_output.index("Lag (MB)")
        for line in patronictl_output.split('\n'):
            if "Replica" in line:
                lag_value = float(line.split()[lag_column_index].replace('MB', ''))
                logging.warning(f"Replication lag detected: {lag_value} MB")
            return lag_value
    else:
        return 'You don\'t have Patroni installed or configured.'
