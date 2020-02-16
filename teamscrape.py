from bs4 import BeautifulSoup
# import urllib2
import requests

# print("Earliest date to show Chief Delphi posts (YYYY-MM-DD): ")
# date_start = input()

with open('teams.csv') as teamfile:
    for line in teamfile:
        tnum = line.split(",")[0].strip()
        tname = line.split(",")[1].strip()

        print(tnum + " - " + tname)
        # Chief delphi
        # cd_url = "https://www.chiefdelphi.com/search?q={0}%20after%3A{1}%20order%3Alatest".format(tnum, date_start)
        # print("Searching " + cd_url)
        # cd_request = urllib.request.urlopen(cd_url)
        # cd_html = cd_request.read().decode("utf-8")
        # print(cd_html)
        # cd_request.close()
        #
        # cd_parsed = BeautifulSoup(cd_html)
        # cd_posts = cd_parsed.find_all("div", {"class": "fps-result"})
        # print(cd_posts)
        # print(str(len(cd_posts)) + " new posts found on Chief Delphi")

        fqa_url = "https://frc-qa.firstinspires.org/qa/team/{0}".format(tnum)
        # fqa_request = urllib2.urlopen(fqa_url)
        # fqa_html = fqa_request.read()
        fqa_html = requests.get(fqa_url).text
        with open('test.html', 'w') as output_html:
            output_html.write(fqa_html)
        # fqa_request.close()

        fqa_soup = BeautifulSoup(fqa_html)
        fqa_posts = fqa_soup.find_all("div", {"class": "qaitem"})
        print(str(len(fqa_posts)) + " question(s) asked on First Q&A")

        print()
