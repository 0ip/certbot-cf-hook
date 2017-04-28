certbot certonly --email MAIL --rsa-key-size 4096 --manual-public-ip-logging-ok \
--manual --preferred-challenges=dns \
--manual-auth-hook /home/user/cch/auth.py \
--manual-cleanup-hook /home/user/cch/auth.py \
-d domain.net -d www.domain.net

