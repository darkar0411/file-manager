import threading
import time

time.sleep(2)
print("core 1")
core2 = threading.Thread(target=print("core 2"))
