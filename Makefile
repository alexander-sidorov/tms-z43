# ---------------------------------------------------------
# [  INCLUDES  ]
# override to whatever works on your system

PIPENV := pipenv

include ./Makefile.in.mk


# ---------------------------------------------------------
# [  TARGETS  ]
# override to whatever works on your system

WSGI_APPLICATION := project.asgi:application
LOCAL_RUN := $(PYTHON) src/manage.py runserver

include ./Makefile.targets.mk


# ---------------------------------------------------------
# [  TARGETS  ]
# keep your targets here


.PHONY: migrations
migrations::
	$(PYTHON) src/manage.py makemigrations


.PHONY: migrate
migrate::
	$(PYTHON) src/manage.py migrate


.PHONY: sh
sh:
	$(call log, starting Django shell)
	$(RUN) python src/manage.py shell


.PHONY: test
test::
	$(RUN) python src/manage.py test -v 2 applications


.PHONY: su
su:
	$(call log, starting Django shell)
	$(RUN) python src/manage.py createsuperuser


.PHONY: run-dev
run-dev:
	$(RUN) uvicorn "project.asgi:application" --reload

