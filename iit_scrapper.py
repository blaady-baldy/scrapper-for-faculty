from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import re


 # REGEX of EMAILS after analysing data 
regex = r"^[\w-]{1,20}(@|\[AT\]|\[AT\*\]|\(AT\)|\sAT\s)[\w]{2,20}(\.|\[DOT\]|\(DOT\)|\sDOT\s)([a-z]{2,8})((\.|\[DOT\]|\(DOT\)|\sDOT\s)[a-z]{2,8})?$"
links = set()

def go_to_links_in_links():
    for link in links:
        goCrawler = pyCrawler(link)

def checker(s):
    s = s.replace(" at ","@")
    s = s.replace("(at)","@")
    s = s.replace("[at]","@")
    s = s.replace("{at}","@")
    s = s.replace(" dot ",".")
    s = s.replace("(dot)",".")
    s = s.replace("[dot]",".")
    s = s.replace("[at*]","@")
    s = s.replace("[dot*]",".")
    return s

class pyCrawler(object):
    def __init__(self,starting_url):

        url=starting_url
        html = uReq(url).read()
        soup = BeautifulSoup(html,"html.parser")


        # for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        #     checkedLink = link.get('href')
        #     links.add(checkedLink)     

                                        # refining the text
        for script in soup(["script", "style"]):
            script.extract()
        text = soup.get_text()

        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        # print(text)
                                        # Splitting Text and storing in a list
        temp_text = text.splitlines()
        temp2_text = ", ".join(temp_text)
        l = temp2_text.split(", ")
        # print(l)

        data=[]

                                        # Checking if there are emails on the page and correcting them 
        for tex in l :
            tex = tex.lower()
            tex = checker(tex)
            # print(tex)
            mail=re.match(regex,tex)
            # print(mail)
            if(mail):
                mail2 = mail.group()
                corrected_mail = checker(mail2)
                data.append(corrected_mail)
        # print(data)

                                        # Writing in a file
        global i
        if(data):
            filename = "emails_on_page"+".csv"
            f = open(filename,"w")
            f.write("Email id\n" )
            for mail in data :
                f.write(mail+"\n")
            i+=1
        print("Task Completed")
        # go_to_links_in_links()
                                # Accesing the html on the given URL or html

url = input("Give the starting url : ")
i=1
startCrawler = pyCrawler(url)

# print(links)