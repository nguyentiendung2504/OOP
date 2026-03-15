import time

seconds = time.time()

days = int(seconds // (24 * 3600))

remaining = seconds % (24 * 3600)

hours = int(remaining // 3600)
remaining = remaining % 3600

minutes = int(remaining // 60)
secs = int(remaining % 60)

print("Days since epoch:", days)
print("Current time:", hours, ":", minutes, ":", secs)