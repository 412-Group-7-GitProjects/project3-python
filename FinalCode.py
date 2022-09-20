from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

# Alt. 2: a progress bar with reduced output (every 1000 blocks)
urlretrieve(URL_PATH, LOCAL_FILE, lambda x, y, z: print('.', end='', flush=True) if x % 100 == 0 else False)


def countrequests(startDate, endDate):
    count = 0
    with open('local_copy.log') as f:
        for line in f.readlines():
            if startDate in line:
                count = 0
            if endDate not in line:
                count += 1
            if endDate in line:
                break
    print("Scan Complete:\nNumber of requests from " + startDate + " to " + endDate + ": " + str(count) + " requests")
    
    with open('local_copy.log') as fp:
        num_lines = sum(1 for line in fp if line.rstrip())
    print('Total requests:', num_lines) 


countrequests("10/May/1995", "12/Oct/1995")

input("Press Enter to exit:")
