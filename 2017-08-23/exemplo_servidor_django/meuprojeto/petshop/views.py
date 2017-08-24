from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def exemplo_get(request):
    return HttpResponse('Aee galera!!')

pagina_com_form = """
    <html>
    <header>
    </header>
    <body>
        <form action="/exemplo_post?parametro_get=valordoformaction" method="post">
            <label for="parametro">Seu parametro: </label> <br/>
            <input id="parametro_post" type="text" name="parametro_post" value="Digite seu valor aqui"> <br/>
            <input type="submit" value="OK">
        </form>
    </body>
"""


@csrf_exempt
def exemplo_post(request):
    if request.method == 'GET':
        return HttpResponse(pagina_com_form)

    elif request.method == 'POST':

        parametro_get = request.GET.get('parametro_get')
        parametro_post = request.POST.get('parametro_post')

        resposta_html = """Aee galera!! <br/>
Voce passou na url: {} <br/>
Voce passou no POST: {}""".format(parametro_get, parametro_post)

        return HttpResponse(resposta_html)
