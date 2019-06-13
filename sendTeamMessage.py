import re

l_str = """Script path         : /home/oracle/tools/travel/Scripts/cron_extra/gg_check_ext/gg_check_ext.sh
Specification sheet : https://confluence.rakuten-it.com/confluence/x/7Fv_Yg
Contact             : DbaTRAVEL

Current checkpoint ~ Current time gap exceeded 55662 sec.
Please check status of extract and heavy duty user sessions on the DBMS.
Executed time: 2019/05/30 08:50:07
"""

# print (l_str)
l_array = l_str.splitlines()



# 2019/05/30 08:50:07
for x in range(len(l_array)):
 if re.search(r'20[1-2][0-9]([\w|\d/\s\:])+[0-9]', l_array[x]):
  print("Time cursor is : ", x)
  time_cursor = x
 
 





# time = re.search(r'20[1-2][0-9]([\w|\d/\s\:])+[0-9]', l_str)
# print("TIME : ", time)


# url = re.search(r'http[s]://([\w.])*', l_str)
# print("URL : ",url)

print("-----------------------------------")



print ("Line number of input is : ", len(l_array))

for x in range(len(l_array)):
 print (x, l_array[x])

#print("Line 0",l_array[0])
#print("Line 1",l_array[1])
#print("Line 2",l_array[2])
#print("Line 3",l_array[3])
#print("Line 4",l_array[4])
#print("Line 5",l_array[5])

#for x in l_read:
# urls = re.findall('https?://[a-zA-Z0-9._\-\/]+', x)

# print(urls)

#l_read.close()

#print("urls" , urls)

l_json = """{
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "themeColor": "0076D7",
    "summary": "alarms from send_mail.sh",
    "sections": [{
        "activityTitle": "TRAVEL Alarms",
        "activitySubtitle": "from send_mail.sh",
        "facts": [{
            "name": "TIME",
            "value": "$$TIME$$"
        }, {
            "name": "HOST_NAME",
            "value": "$$HOST_NAME$$"
        }, {
            "name": "TARGET_NAME",
            "value": "$$TARGET_NAME$$"
        }, {
            "name": "LEVEL",
            "value": "$$LEVEL$$"
        }, {
            "name": "MESSAGE",
            "value": "$$MESSAGE$$"
        }],
        "markdown": "true"
    }],
    "potentialAction": [{
        "@type": "OpenUri",
        "name": "SCRIPT SPEC",
        "targets": [
            { "os": "default", "uri": "$$TARGET_URL$$" }
        ]
    },{
        "@type": "OpenUri",
        "name": "RUNBOOK",
        "targets": [
            { "os": "default", "uri": "https://confluence.rakuten-it.com/confluence/x/xs4Ua" }
        ]
    }]
}"""

l_json=l_json.replace("$$TIME$$","2019/11")

# print ( l_json )

