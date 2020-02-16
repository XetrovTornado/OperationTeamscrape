import os

print("Scout San Diego or Hawaii Regional? (S or H)")
regional = input()[0].upper()

if regional == "S":
    print("Scouting San Diego Regional...")
    filename = 'teams_sandiego.csv'
elif regional == "H":
    print("Scouting Hawaii Regional...")
    filename = 'teams_hawaii.csv'
else:
    print("Not understood, ending program")
    quit()
teamnums = []
with open(filename) as teamfile:
    for line in teamfile:
        tnum = line.split(",")[0].strip()
        tname = line.split(",")[1].strip()
        teamnums.append(tnum)

for num in teamnums:
    fqa_url = "https://frc-qa.firstinspires.org/qa/team/{0}".format(num)
    os.system('start "" "' + fqa_url + '"')

print("Earliest date to show Chief Delphi posts (YYYY-MM-DD): ")
date_start = input()

for num in teamnums:
    cd_url = "https://www.chiefdelphi.com/search?q={0}%20after%3A{1}%20order%3Alatest".format(num, date_start)
    os.system('start "" "' + cd_url + '"')
