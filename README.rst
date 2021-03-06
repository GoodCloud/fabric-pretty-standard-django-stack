Overview
========

The fabric-pretty-standard-django-stack (fabric-psds) is a project
that aims to create a useful fabfile for the following stack.

* Ubuntu
* Nginx
* Virtualenv / Virtualenvwrapper
* Gunicorn
* Pip
* Django
* Celery with a Redis Backend
* South (supported, but not required)
* Codebase in Git, with tagged releases.

It will support the following operations:

* Provision a working server from scratch
* Deploy
* Rollback
* Stop/Start/Restart of any of the above services (that are
  restartable)


Project Status
==============

The code is currently being abstracted and combined from several
in-house and personal scripts. This README will be updated once the
above tasks are actually functional.

Project Notes
=============
http://wiki.wraithan.net/projects:software:fablib
