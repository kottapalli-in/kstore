
.PHONY: venv

ENV=./env/bin/python
MANAGE=$(ENV) kstore/manage.py

run:
	./env/bin/python kstore/manage.py runserver

setup:
	$(MANAGE) syncdb
	$(MANAGE) satchmo_load_l10n
	$(MANAGE) satchmo_load_store
	$(MANAGE) satchmo_rebuild_pricing

venv:
	virtualenv --no-site-packages env
	./env/bin/pip install -r requirements.txt
