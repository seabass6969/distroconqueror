import requests
import re
from bs4 import BeautifulSoup

allhtml = []
file1 = open("result.txt", "w")
def lineW(name,mode):
    if mode == "s":
        return '"'+name+'":"' + input("distro sting of "+ name + ": ")+'",\n'
    elif mode == "a":
        return '"'+name+'":[' + input("distro array in "+ name + ": ")+"],\n"
    elif mode == "b":
        return '"'+name+'":' + input("distro true or false in " + name + ": ")+",\n"
    elif mode == "b+last":
        return '"'+name+'":' + input("distro true or false in " + name + ": ")+"\n"

def fetchallHTML():
    before_url = "https://distrowatch.com/table.php?distribution="
    html = open("word.txt", "r", encoding='utf-8')

    soup = BeautifulSoup(html, 'html.parser')
    getres = soup.find_all("td", class_="phr2")
    for x in range(0, 40):
        getres.pop(0)
    for i in getres:
        item = requests.get(before_url + i.find('a').getText()).text
        print(before_url + i.find('a').getText())
        souper = BeautifulSoup(item, 'html.parser')
        distroname = souper.find_all('h1')[0].text
        r_name = '"name":"'+distroname+'",\n'
        r_desktop = lineW('desktop', "a")
        r_wm_type = lineW('wm_type', "s")
        r_rpi_support = lineW('rpi_support', "b")
        r_weird_arch = lineW('weird_arch_support', "b")
        r_based = lineW('based', "s")
        r_user_friendly = lineW('user_friendly', "b")
        r_old_machine = lineW('old_machine', "b")
        r_usage_type = lineW('usage_type', "s")
        r_link = lineW('link', "s")
        r_hard = lineW('hard', "b")
        r_systemd = lineW('systemd', "b+last")
        file1.writelines(["{\n",r_name,r_desktop,r_wm_type,r_rpi_support,r_weird_arch,r_based,r_user_friendly,r_old_machine,r_usage_type,r_link,r_hard,r_systemd,"},\n"])
        allhtml.append(item)

# def proccessHTML()
try:
    fetchallHTML()
except KeyboardInterrupt:
    file1.close()
# allhtml.append(open("testing.html", "r", encoding='utf-8'))
