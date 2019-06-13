import requests, json
 
VAR_JSON="""{
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "themeColor": "0076D7",
    "summary": "alarms from send_mail.sh",
    "sections": [{
        "activityTitle": "TRAVEL Alarms",
        "activitySubtitle": "from send_mail.sh",
        "facts": [{
            "name": "TIME",
            "value": "time"
        }, {
            "name": "HOST_NAME",
            "value": "time"
        }, {
            "name": "TARGET_NAME",
            "value": "time"
        }, {
            "name": "LEVEL",
            "value": "time"
        }, {
            "name": "MESSAGE",
            "value": "time"
        }],
        "markdown": "true"
    }],
    "potentialAction": [{
        "@type": "OpenUri",
        "name": "SCRIPT SPEC",
        "targets": [
            { "os": "default", "uri": "time" }
        ]
    },{
        "@type": "OpenUri",
        "name": "RUNBOOK",
        "targets": [
            { "os": "default", "uri": "https://confluence.rakuten-it.com/confluence/x/xs4Ua" }
        ]
    }]
}"""
 
WEB_HOOK_URL = "https://outlook.office.com/webhook/c18e1b8c-3d06-47b4-9387-e689c3b7fdfa@53a8b0d9-d900-48cc-9d7e-5935dc8d5b17/IncomingWebhook/cd69a03f38854b6cbd4ac6112bd0480b/40abea6a-82e1-476b-b7e6-79ac477c592b"
requests.post(WEB_HOOK_URL, data = json.dumps(VAR_JSON))