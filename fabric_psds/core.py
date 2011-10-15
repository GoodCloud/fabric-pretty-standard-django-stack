from fabric.api import env, task
import fabric_psds


@task
def provision():
    setup_git()
    clone_code()
    setup_nginx()
    setup_gunicorn()
    setup_celery()
    setup_redis()
    make_virtualenv()
    sync_db()
    deploy()

@task
def deploy():
    checkout_code()
    install_requirements()
    load_code()
    migrate()
