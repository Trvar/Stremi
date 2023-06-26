import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds
    
    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        print(f"Remaining Time: {remaining_seconds // 60}:{remaining_seconds % 60:02d}", end="\r")
        time.sleep(1)
    
    print("Focus Timer Complete!")

# 设置专注时长为25分钟（根据个人需求进行调整）
focus_timer(25)
