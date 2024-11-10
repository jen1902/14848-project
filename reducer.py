import sys
current_key = None
current_count = 0
for line in sys.stdin:
    key, count = line.split()
    count = int(count)
    if key == current_key:
        current_count += count
    else:
        if current_key:
            print(f"{current_key} {current_count}")
        current_key = key
        current_count = count
# Output the last key-value pair
if current_key:
    print(f"{current_key} {current_count}")
