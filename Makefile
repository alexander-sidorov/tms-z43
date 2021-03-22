# ---------------------------------------------------------
# [  INCLUDES  ]
# override to whatever works on your system

PIPENV := pipenv

include ./Makefile.in.mk


# ---------------------------------------------------------
# [  TARGETS  ]
# override to whatever works on your system

WSGI_APPLICATION := project.wsgi:application
LOCAL_RUN := $(PYTHON) src/manage.py runserver

include ./Makefile.targets.mk


# ---------------------------------------------------------
# [  TARGETS  ]
# keep your targets here


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
