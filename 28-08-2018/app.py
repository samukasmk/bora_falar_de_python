from flask import Flask, request, escape, render_template_string
app = Flask(__name__)

@app.route("/xss/sec")
def xss_seguro():
    nome = escape(request.args.get("nome"))
    return "Bem vindo ao site seguro: {}".format(nome)

@app.route('/xss/vuln')
def xss_vulneravel():
    nome = request.args.get('nome')
    return 'Bem vindo ao site vulneravel: {}'.format(nome)

@app.route('/template/vuln')
def template_vulneravel():
    nome = request.args.get('nome')
    segredo = 42
    return render_template_string('Bem vindo ao site vulneravel: {}'.format(nome), segredo=segredo)

# http://cpro37523.publiccloud.com.br/template/vuln?nome={{%27%27.__class__.__mro__[1].__subclasses__()[220](%27http://cpro37523.publiccloud.com.br/xss/vuln?nome=samuka%27)}}

# @app.route('/sql/vuln')
# def template_vulneravel():
#     nome = request.args.get('nome')
#     "SELECT * FROM XPTO WHERE nome=" + nome
#     return render_template_string('Bem vindo ao site vulneravel: {}'.format(nome), segredo=segredo)

