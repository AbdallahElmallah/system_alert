from utils.script_utils import SystemUtils
from utils.logging_utils import log_info, log_error
from monitor_scripts.send_zoho_email import send_zoho_email

def check_resource_usage():
    high_resource_usage_flag = False
    ram_used_percentage=0.0
    storage_used_percentage=0
    cpu_usage_percentage = 0
    
    try:
        ram_info = SystemUtils.get_ram_usage()
        storage_info = SystemUtils.get_storage_usage()
        cpu_usage_percentage = SystemUtils.get_cpu_usage()

        ram_total, ram_used = SystemUtils.parse_ram_usage(ram_info)        
        ram_total /= 1024
        ram_used  /= 1024
        ram_used_percentage = (ram_used / ram_total) * 100
        storage_used_percentage = int(storage_info.split("\n")[1].split()[4].replace("%", ""))

        log_info(f"RAM status reads --> Total: {ram_total:.2f}, Used: {ram_used:.2f}, Percentage: {ram_used_percentage:.2f}%")
        log_info(f"Storage status read --> {storage_used_percentage:.2f}%")
        log_info(f"CPU usage: {cpu_usage_percentage:.2f}%")

        if ram_used_percentage > SystemUtils.RAM_THRESHOLD_PERCENTAGE:
            log_info("RAM resource alert flag triggered.")
            high_resource_usage_flag = True
        
        if " /" in storage_info and storage_used_percentage > SystemUtils.STORAGE_THRESHOLD_PERCENTAGE:
            log_info("Storage resource alert flag triggered.")
            high_resource_usage_flag = True
    
        if cpu_usage_percentage > SystemUtils.CPU_THRESHOLD_PERCENTAGE:
            log_info("CPU resource alert flag triggered.")
            high_resource_usage_flag = True

    except Exception as e:
        log_error(f"Error in check_resource_usage: {str(e)}")
        send_zoho_email("Error in check_resource_usage:\n\n", str(e))

    resource_info = {
        'ram_used_percentage': ram_used_percentage,
        'storage_used_percentage': storage_used_percentage,
        'cpu_usage_percentage': cpu_usage_percentage
    }

    resources_status_report = [
        "High usage resources alert:\n\n",
        f"RAM Percentage: {resource_info['ram_used_percentage']:.2f}%\n",
        f"Storage Percentage: {resource_info['storage_used_percentage']:.2f}%\n",
        f"CPU Percentage: {resource_info['cpu_usage_percentage']:.2f}%\n"
    ]

    return send_zoho_email("Subject: Resources Status Report\n\n", "".join(resources_status_report)) \
        if high_resource_usage_flag \
        else log_info("Resources are currently stable. No action required.")
