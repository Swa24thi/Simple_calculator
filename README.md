# Time Recording Scheduler
A simple Python script to log timestamps using WSL and Cron.

## Setup
To run this every 3 minutes, add the following to your `crontab -e`:
```bash
*/3 * * * * cd /mnt/c/Users/swath/PycharmProjects/PythonProject && /usr/bin/python3 -u py_time.py >> cron_log.txt 2>&1

