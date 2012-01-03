
.PHONY: venv

ENV=./env/bin/python
MANAGE=$(ENV) kstore/manage.py

KSTORE_PORT=7012

run:
	./env/bin/python kstore/manage.py runserver

fcgi:
	$(MANAGE) runfcgi method=threaded daemonize=false host=127.0.0.1 port=$(KSTORE_PORT)

setup:
	$(MANAGE) syncdb
	$(MANAGE) satchmo_load_l10n
	$(MANAGE) satchmo_load_store
	$(MANAGE) satchmo_rebuild_pricing

venv:
	virtualenv --no-site-packages env
	./env/bin/pip install -r requirements.txt

i18n: 
	cd kstore && ../env/bin/python manage.py compilemessages
