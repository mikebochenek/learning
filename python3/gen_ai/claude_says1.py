# https://claude.ai/chat/8f042b60-9ca3-4dd5-a55b-480273d80699
# generate a snippet of python3 code, to print out the boot time of a windows 11 computer
import psutil
import datetime

def get_boot_time():
    # Get boot time in seconds since epoch
    boot_time_seconds = psutil.boot_time()
    
    # Convert to datetime object
    boot_time = datetime.datetime.fromtimestamp(boot_time_seconds)
    
    return boot_time

def main():
    try:
        boot_time = get_boot_time()
        print(f"System boot time: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Calculate uptime
        current_time = datetime.datetime.now()
        uptime = current_time - boot_time
        
        # Format uptime
        days = uptime.days
        hours, remainder = divmod(uptime.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        print(f"System uptime: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
        
    except Exception as e:
        print(f"Error getting boot time: {e}")

if __name__ == "__main__":
    main()