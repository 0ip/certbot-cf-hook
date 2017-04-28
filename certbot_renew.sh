#!/usr/bin/env bash
certbot renew --post-hook "systemctl reload nginx" --quiet
