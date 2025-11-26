from ping3 import ping
import time

def wait_for_host_ping3(host) -> bool:
    count = 0
    while True:
        print(f"[PING] Pinging {host}... Attempt {count + 1}", end="")
        count += 1
        response = ping(host, timeout=1)
        
        if response is not None and response is not False:
            print(f"\n[PING] Success: {host} is reachable! (Latency: {response*1000:.2f}ms)")
            return True
        else:
            if count >= 5:
                print(f"\n[PING] Failure: {host} is not reachable after {count} attempts.")
                return False
            time.sleep(5)
