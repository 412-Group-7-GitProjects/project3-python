#startDate = "11/May/1995"
#endDate = "11/Oct/1995"


def countrequests(startDate, endDate):
    count = 0
    with open('C:\\Users\\olivi\\Documents\\http_access_log.txt') as f:
        for line in f.readlines():
            if startDate in line:
                count = 0
            if endDate not in line:
                count += 1
            if endDate in line:
                break
    print("Number of requests from " + startDate + " to " + endDate + ": " + str(count) + " requests")
    

countrequests("10/May/1995", "12/Oct/1995")

