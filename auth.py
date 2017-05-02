#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import requests as req

KEY = ""
MAIL = ""

ENDPOINT = "https://api.cloudflare.com/client/v4/"

assert os.environ["CERTBOT_DOMAIN"]
assert os.environ["CERTBOT_VALIDATION"]

DOMAIN = os.environ["CERTBOT_DOMAIN"]
ROOT_DOMAIN = ".".join(DOMAIN.split(".")[-2:])
CHALLENGE = os.environ["CERTBOT_VALIDATION"]

CLEAN = os.environ.get("CERTBOT_AUTH_OUTPUT")

headers = {
    "X-Auth-Key": KEY,
    "X-Auth-Email": MAIL,
    "Content-Type": "application/json"
}

if not CLEAN:
    result = req.get("{ep}/zones?name={domain}".format(ep=ENDPOINT, domain=ROOT_DOMAIN), headers=headers).json()
    assert result["success"], result["errors"]

    zone_id = result["result"][0]["id"]

    data = {
        "type": "TXT",
        "name": "_acme-challenge." + DOMAIN,
        "content": CHALLENGE,
        "ttl": 120
    }

    result = req.post("{ep}/zones/{zone_id}/dns_records".format(ep=ENDPOINT, zone_id=zone_id), headers=headers, json=data).json()
    assert result["success"], result["errors"]

    record_id = result["result"]["id"]

    print("{zone}|{record}".format(zone=zone_id, record=record_id))

    time.sleep(15)
else:
    zone_id, record_id = CLEAN.split("|")
    req.delete("{ep}/zones/{zone_id}/dns_records/{record_id}".format(
        ep=ENDPOINT,
        zone_id=zone_id,
        record_id=record_id),
        headers=headers)
    
