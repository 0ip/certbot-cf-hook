This repository serves the purpose to fully automate the deployment and renewal of Let's Encrypt certificates.

Assumptions:

* Python 3 is installed (incl. the `requests` module)
* `certbot` is installed, see <https://certbot.eff.org/>

In order to set up everything:

1. Clone this repo somewhere, e. g. `cd && git clone git://github.com/0ip/certbot-cf-hook cch`
2. Specify your Cloudflare API key and mail in `auth.py`
3. Adapt the webserver reload command in `certbot_renew.sh` to your environment
4. Specify your e-mail address and (sub)domains in `certbot_init.sh` and adapt the paths
5. Redo step 5 and run `certbot_init.sh` for each domain once
6. If step 5 completed without any errors, you can try `certbot renew --dry-run` to see if everything works
7. Create a root cronjob `0 3 * * * /home/user/cch/certbot_renew.sh` (runs daily at 03:00 a.m.)
8. Done :)

