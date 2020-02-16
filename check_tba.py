import requests

apiKey = "mGUS0gYwjX8QqyYvVWC1804128ZZKfCRlDWGvDria2iKUt1qqalnCjcBd6riqXu2"

sd_response = requests.get(f"https://www.thebluealliance.com/api/v3/event/2020casd/teams?X-TBA-Auth-Key={apiKey}")
sd_json = sd_response.json()
print("San Diego: " + str(len(sd_json)) + " teams")

# with open('teams_sandiego.csv', 'w') as sd_csv:
#     for team in sd_json:
#         sd_csv.write(str(team["team_number"]) + "," + team["nickname"].encode('ascii', 'replace').decode('utf-8') + "\n")

hi_response = requests.get(f"https://www.thebluealliance.com/api/v3/event/2020hiho/teams?X-TBA-Auth-Key={apiKey}")
hi_json = hi_response.json()
print("Hawaii: " + str(len(hi_json)) + " teams")

print()
print("Press enter to close...")
input()
