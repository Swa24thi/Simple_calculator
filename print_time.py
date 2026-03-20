from datetime import datetime

# No need to open a file manually; cron handles the writing!
print(f"scheduler ran at - {datetime.now()}")