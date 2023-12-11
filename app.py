from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random
import string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(50), unique=False, nullable=False)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    
    def __repr__(self):
        return f"Seu link é: {self.link}"

with app.app_context():
    db.create_all()

def obter_link(nome):
    link = Links.query.filter_by(nome=nome).first()
    return link.link if link else None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar_link', methods=['POST'])
def processar():
    link = request.form['link']
    nome = request.form['nome']
    valor = request.referrer.split("processar_link")[0] + nome

    if not nome:
        nome = ''.join(random.choices(string.ascii_letters + string.digits, k=15))

    link_encurtado = Links(link=link, nome=nome)
    db.session.add(link_encurtado)
    db.session.commit()
    
    visivel = True

    return render_template('index.html', valor=valor, visivel=visivel)

@app.route('/<nome>')
def redirecionar(nome):
    link = obter_link(nome)
    if link:
        return redirect(link)
    else:
        return f'Link não encontrado para o nome: {nome}'

if __name__ == '__main__':
    app.run(debug=True)
