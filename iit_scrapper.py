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
    s = s.replace(" AT ","@")
    s = s.replace("(AT)","@")
    s = s.replace("[AT]","@")
    s = s.replace(" DOT ",".")
    s = s.replace("(DOT)",".")
    s = s.replace("[DOT]",".")
    s = s.replace("[AT*]","@")
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

                                        # Splitting Text and storing in a list
        temp_text = text.splitlines()
        temp2_text = ", ".join(temp_text)
        l = temp2_text.split(", ")

        data=[]

                                        # Checking if there are emails on the page and correcting them 
        for tex in l :
            mail=re.match(regex,tex)
            if(mail):
                mail2 = mail.group()
                corrected_mail = checker(mail2)
                data.append(corrected_mail)

                                        # Writing in a file
        global i
        if(data):
            filename = "emails_on_page_"+str(i)+".csv"
            f = open(filename,"w")
            f.write("Email id\n" )
            for mail in data :
                f.write(mail+"\n")
            i+=1
        # go_to_links_in_links()
                                # Accesing the html on the given URL or html
url = "http://www.iitg.ac.in/biotech/faculty.php"



url = input("Give the starting url : ")
i=1
startCrawler = pyCrawler(url)

print("Task Completed")
print(links)