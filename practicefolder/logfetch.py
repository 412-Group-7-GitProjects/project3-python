
import urllib.request

def main():
    webURL = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
    print("result code: " + str(webURL.getcode()))
    data = webURL.read()
    print (data)

if __name__ == '__main__':
    main()