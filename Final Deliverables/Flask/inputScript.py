import ipaddress
import re
import socket
import time
import urllib.request
from datetime import date, datetime
from tracemalloc import DomainFilter
from urllib.parse import urlencode, urlparse
from xml.dom.xmlbuilder import DOMInputSource
import regex
import fast_pagerank
import requests
import urllib3
import whois
from bs4 import BeautifulSoup
from dateutil.parser import parse as date_parse
from googlesearch import search

  # 1.UsingIp

def UsingIp(url):

        try:

            ipaddress.ip_address(url)

            return 2

        except:

            return 1



    # 2.longUrl

def longUrl(url):

        if len(url) < 54:

            return 1

        if len(url) >= 54 and len(url) <= 75:

            return 0

        return 2



    # 3.shortUrl

def shortUrl(url):

        match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'

                    'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'

                    'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'

                    'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'

                    'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'

                    'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'

                    'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|tr\.im|link\.zip\.net', url)

        if match:

            return 2

        return 1



    # 4.Symbol@

def symbol(url):

        if "@" in url:

            return 2

        return 1

    

    # 5.Redirecting//

def redirecting(url):

        if url.rfind('//')>6:

            return 2

        return 1

    

    # 6.prefixSuffix

def prefixSuffix(url):

        if '-' in urlparse(url).netloc:
            return 2
        else:
            return 1
    

    # 7.SubDomains

def SubDomains(url):

        dot_count = len(re.findall("\.", url))

        if dot_count == 1:

            return 2

        elif dot_count == 2:

            return 0

        return 1



    # 8.HTTPS

def Hppts(url):

        try:

            https = url.urlparse.scheme

            if 'https' in https:

                return 1

            return 2

        except:

            return 2



    # 9.DomainRegLen

def DomainRegLen(url):

        try:

            expiration_date = url.whois_response.expiration_date

            creation_date = url.whois_response.creation_date

            try:

                if(len(expiration_date)):

                    expiration_date = expiration_date[0]

            except:

                pass

            try:

                if(len(creation_date)):

                    creation_date = creation_date[0]

            except:

                pass



            age = (expiration_date.year-creation_date.year)*12+ (expiration_date.month-creation_date.month)

            if age >=12:

                return 1

            return 2

        except:

            return 2



    # 10. Favicon

def Favicon(url):

        try:

            for head in url.soup.find_all('head'):

                for head.link in url.soup.find_all('link', href=True):

                    dots = [x.start(0) for x in re.finditer('\.', head.link['href'])]

                    if url.url in head.link['href'] or len(dots) == 1 or DOMInputSource in head.link['href']:

                        return 1

            return 2

        except:

            return 2



    # 11. NonStdPort

def NonStdPort(url):

        try:

            port = url.domain.split(":")

            if len(port)>1:

                return 2

            return 1

        except:

            return 2



    # 12. HTTPSDomainURL

def HTTPSDomainURL(url):

        try:

            if 'https' in url.domain:

                return 1

            return 2

        except:

            return 2

    

    # 13. RequestURL

def RequestURL(url):

        try:

            for img in url.soup.find_all('img', src=True):

                dots = [x.start(0) for x in re.finditer('\.', img['src'])]

                if url.url in img['src'] or url.domain in img['src'] or len(dots) == 1:

                    success = success + 1

                i = i+1



            for audio in url.soup.find_all('audio', src=True):

                dots = [x.start(0) for x in re.finditer('\.', audio['src'])]

                if url.url in audio['src'] or url.domain in audio['src'] or len(dots) == 1:

                    success = success + 1

                i = i+1



            for embed in url.soup.find_all('embed', src=True):

                dots = [x.start(0) for x in re.finditer('\.', embed['src'])]

                if url.url in embed['src'] or url.domain in embed['src'] or len(dots) == 1:

                    success = success + 1

                i = i+1



            for iframe in url.soup.find_all('iframe', src=True):

                dots = [x.start(0) for x in re.finditer('\.', iframe['src'])]

                if url.url in iframe['src'] or url.domain in iframe['src'] or len(dots) == 1:

                    success = success + 1

                i = i+1



            try:

                percentage = success/float(i) * 100

                if percentage < 22.0:

                    return 1

                elif((percentage >= 22.0) and (percentage < 61.0)):

                    return 0

                else:

                    return 2

            except:

                return 0

        except:

            return 2

    

    # 14. AnchorURL

def AnchorURL(url):

        try:

            i,unsafe = 0,0

            for a in url.soup.find_all('a', href=True):

                if "#" in a['href'] or "javascript" in a['href'].lower() or "mailto" in a['href'].lower() or not (url in a['href'] or url.domain in a['href']):

                    unsafe = unsafe + 1

                i = i + 1



            try:

                percentage = unsafe / float(i) * 100

                if percentage < 31.0:

                    return 1

                elif ((percentage >= 31.0) and (percentage < 67.0)):

                    return 0

                else:

                    return 2

            except:

                return 2



        except:

            return 2



    # 15. LinksInScriptTags

def LinksInScriptTags(url):

        try:

            i,success = 0,0

        

            for link in url.soup.find_all('link', href=True):

                dots = [x.start(0) for x in re.finditer('\.', link['href'])]

                if url.url in link['href'] or url.domain in link['href'] or len(dots) == 1:

                    success = success + 1

                i = i+1



            for script in url.soup.find_all('script', src=True):

                dots = [x.start(0) for x in re.finditer('\.', script['src'])]

                if url.url in script['src'] or url.domain in script['src'] or len(dots) == 1:

                    success = success + 1

                i = i+1



            try:

                percentage = success / float(i) * 100

                if percentage < 17.0:

                    return 1

                elif((percentage >= 17.0) and (percentage < 81.0)):

                    return 0

                else:

                    return 2

            except:

                return 0

        except:

            return 2



    # 16. ServerFormHandler

def ServerFormHandler(url):

        try:

            if len(url.soup.find_all('form', action=True))==0:

                return 1

            else :

                for form in url.soup.find_all('form', action=True):

                    if form['action'] == "" or form['action'] == "about:blank":

                        return 2

                    elif url.url not in form['action'] and url.domain not in form['action']:

                        return 0

                    else:

                        return 1

        except:

            return 2



    # 17. InfoEmail

def InfoEmail(url):

        try:

            if re.findall(r"[mail\(\)|mailto:?]", url.soap):

                return 1

            else:

                return 2

        except:

            return 2



    # 18. AbnormalURL

def AbnormalURL(url):

        try:

            if url.response.text == url.whois_response:

                return 1

            else:

                return 2

        except:

            return 2



    # 19. WebsiteForwarding

def WebsiteForwarding(url):

        try:

            if len(url.response.history) <= 1:

                return 1

            elif len(url.response.history) <= 4:

                return 0

            else:

                return 2

        except:

             return 2



    # 20. StatusBarCust

def StatusBarCust(url):

        try:

            if re.findall("<script>.+onmouseover.+</script>", url.response.text):

                return 1

            else:

                return 2

        except:

             return 2



    # 21. DisableRightClick
def DisableRightClick(url):

        try:

            if re.findall(r"event.button ?== ?2", url.response.text):

                return 1

            else:

                return 2

        except:

             return 2



    # 22. UsingPopupWindow

def UsingPopupWindow(response):

        try:

            if re.findall(r"alert\(", response.text):

                return 1

            else:

                return 2

        except:

             return 2



    # 23. IframeRedirection

def IframeRedirection(url):

        try:

            if re.findall(r"[<iframe>|<frameBorder>]", url.response.text):

                return 1

            else:

                return 2

        except:

             return 2



    # 24. AgeofDomain

def AgeofDomain(url):

        try:

            creation_date = url.whois_response.creation_date

            try:

                if(len(creation_date)):

                    creation_date = creation_date[0]

            except:

                pass



            today  = date.today()

            age = (today.year-creation_date.year)*12+(today.month-creation_date.month)

            if age >=6:

                return 2

            return 1

        except:

            return 2



    # 25. DNSRecording    

def DNSRecording(url):

        try:

            creation_date = url.whois_response.creation_date

            try:

                if(len(creation_date)):

                    creation_date = creation_date[0]

            except:

                pass



            today  = date.today()

            age = (today.year-creation_date.year)*12+(today.month-creation_date.month)

            if age >=6:

                return 2

            return 1

        except:

            return 2



    # 26. WebsiteTraffic   

def WebsiteTraffic(url):

        try:

            rank = BeautifulSoup(urllib.request.urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml").find("REACH")['RANK']

            if (int(rank) < 100000):

                return 2

            return 1

        except :

            return 2



    # 27. PageRank

def PageRank(url):

        try:

            prank_checker_response = requests.post("https://www.checkpagerank.net/index.php", {"name": url.domain})



            global_rank = int(re.findall(r"Global Rank: ([0-9]+)", prank_checker_response.text)[0])

            if global_rank > 0 and global_rank < 100000:

                return 1

            return 2

        except:

            return 2

            



    # 28. GoogleIndex

def GoogleIndex(url):

        try:

            site = search(url, 5)

            if site:

                return 1

            else:

                return 2

        except:

            return 2



    # 29. LinksPointingToPage

def LinksPointingToPage(url):

        try:

            number_of_links = len(re.findall(r"<a href=", url.response.text))

            if number_of_links == 0:

                return 1

            elif number_of_links <= 2:

                return 0

            else:

                return 2

        except:

            return 2

 # 30. StatsReport

def StatsReport(self):

        try:

            url_match = re.search('at\.ua|usa\.cc|baltazarpresentes\.com\.br|pe\.hu|esy\.es|hol\.es|sweddy\.com|myjino\.ru|96\.lt|ow\.ly', urlencode)

            ip_address = socket.gethostbyname(self.domain)

            ip_match = re.search('146\.112\.61\.108|213\.174\.157\.151|121\.50\.168\.88|192\.185\.217\.116|78\.46\.211\.158|181\.174\.165\.13|46\.242\.145\.103|121\.50\.168\.40|83\.125\.22\.219|46\.242\.145\.98|'

                                '107\.151\.148\.44|107\.151\.148\.107|64\.70\.19\.203|199\.184\.144\.27|107\.151\.148\.108|107\.151\.148\.109|119\.28\.52\.61|54\.83\.43\.69|52\.69\.166\.231|216\.58\.192\.225|'

                                '118\.184\.25\.86|67\.208\.74\.71|23\.253\.126\.58|104\.239\.157\.210|175\.126\.123\.219|141\.8\.224\.221|10\.10\.10\.10|43\.229\.108\.32|103\.232\.215\.140|69\.172\.201\.153|'

                                '216\.218\.185\.162|54\.225\.104\.146|103\.243\.24\.98|199\.59\.243\.120|31\.170\.160\.61|213\.19\.128\.77|62\.113\.226\.131|208\.100\.26\.234|195\.16\.127\.102|195\.16\.127\.157|'

                                '34\.196\.13\.28|103\.224\.212\.222|172\.217\.4\.225|54\.72\.9\.51|192\.64\.147\.141|198\.200\.56\.183|23\.253\.164\.103|52\.48\.191\.26|52\.214\.197\.72|87\.98\.255\.18|209\.99\.17\.27|'

                                '216\.38\.62\.18|104\.130\.124\.96|47\.89\.58\.141|78\.46\.211\.158|54\.86\.225\.156|54\.82\.156\.19|37\.157\.192\.102|204\.11\.56\.48|110\.34\.231\.42', ip_address)

            if url_match:

                return 1

            elif ip_match:

                return 1

            return 2

        except:

            return 2

def Result(url):
    return 0   


def main(url):


    
    check = [[UsingIp(url),longUrl(url), shortUrl(url),symbol(url),redirecting(url), prefixSuffix(url),
              SubDomains(url),Hppts(url), DomainRegLen(url),Favicon(url),NonStdPort(url), HTTPSDomainURL(url),
              RequestURL(url), AnchorURL(url), LinksInScriptTags(url),ServerFormHandler(url),InfoEmail(url),
              AbnormalURL(url), WebsiteForwarding(url),StatusBarCust(url),DisableRightClick(url), UsingPopupWindow(url),
              IframeRedirection(url), AgeofDomain(url), DNSRecording(url),WebsiteTraffic(url),PageRank(url),
              GoogleIndex(url),LinksPointingToPage(url),StatsReport(url),Result(url)]]
    
    
    
    return check