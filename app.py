import flet as ft
from modelo import Produto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///projeto2.db"

engine = create_engine(CONN, echo = True)
Session = sessionmaker(bind=engine)
session = Session()

def main(page: ft.Page):
    page.titulo = 'Cadastro App'
    
   
    lista_produtos=ft.ListView()
   
    def cadastrar(e):
        try:
            novo_produto = Produto(titulo=produto.value, preco=preco.value)
            session.add(novo_produto)
            session.commit()
            lista_produtos.controls.append(  ft.Container(    
                    ft.Text(produto.value),
                    bgcolor=ft.colors.BLACK12,
                    padding=15,
                    alignment=ft.alignment.center,
                    margin=3,
                    border_radius=10
                ))
            txt_erro.visible = False
            txt_acerto.visible = True
        except:
            txt_erro.visible = True
            txt_acerto.visible = False
        
        
        page.update()
        print('Produto salvo com sucesso')
        
    txt_erro = ft.Container(ft.Text('Erro ao salvar o produto'),visible= False, bgcolor=ft.colors.RED, padding=10, alignment=ft.alignment.center)
    txt_acerto = ft.Container(ft.Text('Salvo com sucesso'),visible= False, bgcolor=ft.colors.GREEN, padding=10, alignment=ft.alignment.center)
    
    
    txt_titulo = ft.Text('Título do produto: ')
    produto = ft.TextField(label="Digite o nome do produto...", text_align=ft.TextAlign.LEFT) # deixar o texto a direita
    txt_preco = ft.Text('informe o preço do produto')
    preco= ft.TextField(label ="Digite o preço do produto", text_align=ft.TextAlign.LEFT)
    btn_produto = ft.ElevatedButton('Cadastrar', on_click=cadastrar)
    
    page.add(
        txt_acerto,
        txt_erro,
        txt_acerto,
        txt_erro,
        txt_titulo,
        produto,
        txt_preco,
        preco,
        btn_produto
    )

    for p in session.query(Produto).all():
        print(p.titulo)
        lista_produtos.controls.append(
            ft.Container(    
                ft.Text(p.titulo),
                bgcolor=ft.colors.BLACK12,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=10
                
            )
            )
        page.add(
            lista_produtos,
        )
        
ft.app(target=main)
