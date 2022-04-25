from flask import redirect, render_template, url_for, flash, request, session, current_app

from loja import db, app
from loja.produtos.models import Addproduto




def M_Dicionarios(dic1, dic2):
    if isinstance(dic1, list) and isinstance(dic2, list):
        return dic1 + dic2
    elif isinstance(dic1, dict) and isinstance(dic2, dict):
        return dict(list(dic1.items()) + list(dic2.items()))
    return False

    # """Função para ADCIONAR uma MARCA da loja"""

@app.route('/addCart', methods=['POST'])
def AddCart():
    try:   
        produto_id = request.form.get('produto_id')
        quantity = request.form.get('quantity')
        colors = request.form.get('colors')
        produto = Addproduto.query.filter_by(id=produto_id).first()

        if produto_id and quantity and colors and request.method == 'POST':
            DicItems = {produto_id:{'Nome':produto.name, 'Price':produto.price, 'Disconto':produto.discount,
                                    'Cor':produto.colors, 'Quantidade':produto.quantity, 'Img':produto.image_1,
                                    }}
            if 'LojainCarrinho' in session:
                print(session["LojainCarrinho"])
                if produto_id in session['LojainCarrinho']:
                    print('Este produto ja existe no carrinho')
                else:
                    session['LojainCarrinho'] = M_Dicionarios(session['LojainCarrinho'], DicItems)
                    return redirect(request.referrer)

            else:
                session['LojainCarrinho'] = DicItems
                return redirect(request.referrer)

    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)