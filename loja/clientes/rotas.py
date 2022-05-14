from flask import redirect, render_template, url_for, flash, request, session, current_app
from loja import db, app, photos, bcrypt
from .forms import CadastroClienteForm

import secrets, os
from .models import Cadastrar

@app.route("/cliente/cadastrar", methods=['GET', 'POST'])
def cadastrar_clientes():
    form = CadastroClienteForm(request.form)
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        cadatrar = Cadastrar(name=form.name.data, username=form.username.data, email=form.email.data,
                             password=hash_password, country=form.country.data, city=form.city.data, contact=form.contact.data, address=form.address.data,
                             zipcode=form.zipcode.data)
        db.session.add(cadatrar)
        flash(f'Obrigado {form.name.data} por cadastrar','success')
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('cliente/cliente.html', form=form)
