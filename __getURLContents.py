'''
Python program to access and print a URL's content to theconsole
'''
def getURLContentsThroughConnection():
    from http.client import HTTPConnection
    conn = HTTPConnection("example.com")
    conn.request("GET", "/")  
    result = conn.getresponse()
    # retrieves the entire contents.  
    contents = result.read() 
    print(contents)
    print ("Example response")

def getURLContentsThroughReuquest():
    import requests
    data = requests.get('https://google.com/')
    print(data.text)
    print ("Google response")


def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : getURLContentsThroughConnection,
                  2 : getURLContentsThroughReuquest,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()
