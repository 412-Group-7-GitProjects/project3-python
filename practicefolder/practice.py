
import urllib.request

def main():
    webURL = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
    print("result code: " + str(webURL.getcode()))
    data = webURL.read()
    #print (data)
    countrequests("10/May/1995", "12/Oct/1995")    

#startDate = "11/May/1995"
#endDate = "11/Oct/1995"

def countrequests(startDate, endDate):
    count = 0
    with open('/Users/connorplank/Documents/GitHub/project3-python/practicefolder/http_access_log.txt') as f:
        for line in f.readlines():
            if startDate in line:
                count = 0
            if endDate not in line:
                count += 1
            if endDate in line:
                break
    print("Number of requests from " + startDate + " to " + endDate + ": " + str(count) + " requests")
    
if __name__ == '__main__':
    main()