import time

def send_emails():
    for x in range(100000):
        pass

start = time.time()
send_emails()
end = time.time()

duration = end - start
print(duration)