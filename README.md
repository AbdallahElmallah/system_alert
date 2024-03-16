# System Monitoring Script

This script monitors various system resources (CPU, RAM, storage, PostgreSQL status, and replication lag) and sends email alerts if their usage or status exceeds predefined thresholds.

## Requirements

- Python 3.x
- `python-dotenv` package

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd system_alert
    ```

3. Install the required dependencies:

    ```bash
    pip install python-dotenv
    ```

4. Set up the environment variables:

    - Add the following environment variables to the `.env` file:
        ```plaintext
        SENDER_EMAIL=your_email@example.com
        ZOHO_APP_PASSWORD=your_zoho_app_password
        MAIL_GROUP_EMAIL=mail_group@example.com
        ```
    - Replace `your_email@example.com` with the sender email address, `your_zoho_app_password` with the Zoho app password, and `mail_group@example.com` with the recipient email address.

## Usage

To run the script, execute the following command in your terminal:

```bash
python3 main.py
```

The script will monitor various system resources and statuses in the background. If any usage or status exceeds the predefined thresholds, an email alert will be sent to the specified recipient.

## Customization

- **Thresholds**: You can customize the thresholds for CPU, RAM, storage, and PostgreSQL replication lag in the respective functions located in `monitor_scripts/resource_checks.py`.
- **Email Configuration**: You can configure the email settings by modifying the `send_zoho_email` function in `monitor_scripts/send_zoho_email.py`. Duplicate this file and customize it to use a different SMTP server and port if needed.

## Automation 

You can automate the script to run periodically using `cron` or `systemd` timers. Here's an example `cron` entry to run the script every hour:

```cron
0 * * * * cd /path/to/system_alert && /usr/bin/python3 main.py
```

Replace `/path/to/system_alert` with the actual path to the project directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
