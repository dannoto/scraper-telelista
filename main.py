from textwrap import indent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
import re
from unidecode import unidecode
import string



class Scraper:

    def __init__(self):

        self.leads = []
        # self.url = "https://www.telelistas.net/go/goiania/construcao+civil?pag=84"
        self.Run()


        print(self.leads)

    def Run(self):

        driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

        driver.get("https://www.telelistas.net/sp/sao+paulo/construcao+civil")

        pagination =  driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[8]/div/div/div[2]").text
        pagination = int(pagination.replace('Página 1 de ',''))


        # print(pagination)

        for x in range(1, pagination):

            driver.get("https://www.telelistas.net/sp/sao+paulo/construcao+civil?pag="+str(x))
            divs =  driver.find_elements(by=By.XPATH, value="/html/body/div[1]/div[6]/div[1]/div")

            
            for div in divs:

                site = ""
                name = ""
                phone = ""
                email = ""
            

                try:
                    site = div.find_element(by=By.CLASS_NAME, value="vai-site").get_attribute('data-site')
                
                except:
                    print('')

                try:
                    name = div.find_element(by=By.CLASS_NAME, value="card-title").text
                
                except:
                    print('')

                try:
                    phone = div.find_element(by=By.CLASS_NAME, value="call-zap").get_attribute('data-telefone')
                
                except:
                    print('')


                if len(site) > 0:

                    try:
                        fp = urllib.request.urlopen(site)
                        mybytes = fp.read()
                        html = mybytes.decode("utf8")
                        fp.close()
                        # print(html)

                        match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', html)

                        email = match.group(0)
                        # print(email)
                    except:
                        print('')
                    # print(site)
                else:
                    print('')
                
                if len(email) > 0:
                    if email == "core-js-bundle@3.2.1":
                        print('NOT email EMAIL')
                    elif email == "select2@4.0.13":
                        print('NOT MATCH EMAIL')
                    elif email == "afterglowplayer@1.x":
                        print('NOT MATCH EMAIL')
                    elif email == "call-center-8TK3NA4@2x.png":
                        print('NOT MATCH EMAIL')
                    else:
                        sample_str = "Test&[88]%%$$$#$%-+String"
                        # Create a regex pattern to match all special characters in string
                        pattern = r'[' + string.punctuation + ']'

                        server = "https://socursoead.com/admin/leads_add?leads_name="+unidecode(name.replace(" ", ""))+"&leads_site="+unidecode(site) +"&leads_email="+unidecode(email) +"&leads_phone="+"55"+phone+""

                        fp = urllib.request.urlopen(server)
                        # mybytes = fp.read()
                        # html = mybytes.decode("utf8")
                        fp.close()

                print(self.leads)    


            

            
          

Scraper()