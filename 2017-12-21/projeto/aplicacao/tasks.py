# Create your tasks here
from __future__ import absolute_import, unicode_literals

import requests
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

from aplicacao.models import Email

@shared_task(name="consulta_web")
def consulta_no_havebeenpwned(email_id):
    email_model = Email.objects.get(id=email_id)

    email_model.status = 'em_processo'
    email_model.save()

    logger.info('dormindo por 30seg')

    try:
        resultado = requests.get('https://haveibeenpwned.com/api/v2/unifiedsearch/{}'.format(email_model.email))

        if resultado.status_code == 404:
            email_model.fui = False
        else:
            email_model.fui = True
            j = resultado.json()
            titles = [i['Title'] for i in j['Breaches']]

            email_model.resultado = ', '.join(titles)
    except:
        email_model.status = 'falhou'
    else:
        email_model.status='processado'

    email_model.save()

    return email_id
