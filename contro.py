from PyQt5 import  uic,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from reportlab.pdfgen import canvas
import mysql.connector
from reportlab.platypus.flowables import PageBreak
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
numero_id = 0

banco = mysql.connector.connect(
    host="26.10.149.113",
    port=3306,
    user="teste",
    passwd="73914682@Vv",
    database="cadastro_produtos"
)
def gerar_pdf():
    cursor = banco.cursor()
    comando_SQL = "SELECT nome, preco, categoria, marca FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    y2 = 0
    
    width = 600
    height = 5000
    pdfmetrics.registerFont(TTFont('Rockwell','Rockwell.ttc'))
    pdfmetrics.registerFont(TTFont('Rockwell-Bold','Rockwell.ttc'))
    pdf = canvas.Canvas("catalogo_produtos.pdf")
    pdf.setPageSize((width,height))
    pdf.drawImage (("650x5000px.png"),0,0)
    pdf.drawImage (("Logo wild BRANCA.png"),490,4932,mask='auto')
    pdf.setFont("Rockwell-Bold", 25)
    pdf.setFillColorRGB(255,255,255)
    pdf.setStrokeColorRGB(255,255,255,alpha=0.2)
    pdf.drawString(170,4955, "Catálogo completo")
    pdf.setFont("Rockwell", 15)
    

    pdf.drawString(110,4900, "NOME")
    pdf.drawString(278,4900, "PREÇO")
    pdf.drawString(350,4900, "CATEGORIA")
    pdf.drawString(350,4900, "MARCA")
    for i in range(0, len(dados_lidos)):
        y = y + 30
        pdf.drawString(30,4900 - y, str(dados_lidos[i][0]))
        pdf.drawString(278,4900 - y, str(dados_lidos[i][1]))
        pdf.drawString(350,4900 - y, str(dados_lidos[i][2]))
        pdf.drawString(490,4900 - y, str(dados_lidos[i][3])) 
        
    for j in range (164):
        pdf.line(0,y2,700,y2)
        y2 = y2 + 30
    pdf.rotate(90)
    pdf.line(0,-270,4920,-270)
    pdf.line(0,-338,4920,-338)   
    pdf.line(0,-455,4920,-455)  
        
    pdf.save()
    pdfs.show()


def fechar_pdfs():

    pdfs.close()


def editar_dados():
    global numero_id
   
    linha = segunda_tela.tableWidget.currentRow()
    
    cursor = banco.cursor()
    cursor.execute("SELECT codigo FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM produtos WHERE codigo="+ str(valor_id))
    produto = cursor.fetchall()
    tela_editar.show()

    tela_editar.lineEdit.setText(str(produto[0][0]))
    tela_editar.lineEdit_2.setText(str(produto[0][1]))
    tela_editar.lineEdit_3.setText(str(produto[0][2]))
    tela_editar.lineEdit_4.setText(str(produto[0][3]))
    tela_editar.lineEdit_5.setText(str(produto[0][4]))
    tela_editar.lineEdit_6.setText(str(produto[0][5]))
    tela_editar.lineEdit_7.setText(str(produto[0][6]))
    tela_editar.lineEdit_8.setText(str(produto[0][7]))
    numero_id = valor_id

def salvar_dados():

        global numero_id

        codigo = tela_editar.lineEdit_2.text()
        quantidade = tela_editar.lineEdit_3.text()
        nome = tela_editar.lineEdit_4.text()
        preco = tela_editar.lineEdit_5.text()
        categoria = tela_editar.lineEdit_7.text()
        marca = tela_editar.lineEdit_8.text()
        precocusto = tela_editar.lineEdit_6.text()
        cursor = banco.cursor()
        cursor.execute("UPDATE produtos SET codigo = '{}', quantidade = '{}', nome = '{}', preco ='{}', precocusto ='{}', categoria ='{}', marca ='{}'  WHERE codigo = {}".format(codigo,quantidade,nome,preco,precocusto,categoria,marca,numero_id))
        banco.commit()
        tela_editar.close()
        segunda_tela.close()
        chama_segunda_tela()
        
def excluir_dados():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT codigo FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM produtos WHERE codigo="+ str(valor_id))
    tela_editar.close()
    segunda_tela.close()
    chama_segunda_tela()
    
def funcao_principal(self):
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha4 = formulario.lineEdit_4.text()
    linha5 = formulario.lineEdit_5.text()
    linha6 = formulario.lineEdit_6.text()
    

    categoria = ""
    
    if formulario.radioButton.isChecked() :
        categoria ="Juice"
        
    elif formulario.radioButton_2.isChecked() :
        
        categoria ="NicSalt"
    elif formulario.radioButton_3.isChecked() :
        
        categoria ="Aparelhos"
    elif formulario.radioButton_4.isChecked() :
        
        categoria ="Acessorios"
    elif formulario.radioButton_5.isChecked() :
        
        categoria ="Vape"
    else :
        categoria ="Pod"



    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,quantidade,nome,preco,precocusto,categoria,marca) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(linha2),str(linha1),str(linha3),str(linha4),str(linha6),categoria,str(linha5))
    cursor.execute(comando_SQL,dados)
    banco.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    formulario.lineEdit_4.setText("")
    formulario.lineEdit_5.setText("")
    formulario.lineEdit_6.setText("")

    
def chama_segunda_tela():

    segunda_tela.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(8)
    for i in range(0, len(dados_lidos)):
        for j in range(0, 8):
           segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    cursor.reset()       
    cursor = banco.cursor() 
    cursor.execute("SELECT SUM(ROUND((precocusto*quantidade))) FROM produtos")
    cursor.fetchall
    gasto = cursor.fetchall()

    
    res = [list(ele) for ele in gasto]
    
    lt = ' '.join([str(elem) for elem in res])
    
    lt = (lt)[1:-1]
    
    segunda_tela.label_2.setText(lt)
    cursor = banco.cursor()
    cursor.execute("SELECT SUM(ROUND((preco*quantidade))) FROM produtos")
    lucro = cursor.fetchall()
    
    res = [list(ele) for ele in lucro]
    
    lt2 = ' '.join([str(elem) for elem in res])
    
    lt2 = (lt2)[1:-1]
    
    lucro1 = float(lt2)
    gasto1 =float(lt)
    lucro_total = lucro1-gasto1
    lucro_total1 = str(lucro_total)
    segunda_tela.label_4.setText(lucro_total1)

    



               
def search(dados_lidos):

    
    segunda_tela.tableWidget.setCurrentItem(None)
    
    
    if not str(dados_lidos):

        return

    matching_items = segunda_tela.tableWidget.findItems(str(dados_lidos), Qt.MatchContains)
    if matching_items:
            # We have found something.
            for item in matching_items:  # Take the first.
                item.setSelected(True)

app=QtWidgets.QApplication([])
pdfs =uic.loadUi("pdfsalvo.ui")
formulario=uic.loadUi("cadastro.ui")
segunda_tela=uic.loadUi("listar_dados.ui")
tela_editar=uic.loadUi("menu_editar.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(excluir_dados)
segunda_tela.pushButton_2.clicked.connect(editar_dados)
tela_editar.pushButton.clicked.connect(salvar_dados)
segunda_tela.lineEdit.textChanged.connect(search)
segunda_tela.pushButton_3.clicked.connect(gerar_pdf)
pdfs.pushButton.clicked.connect(fechar_pdfs)

formulario.show()
app.exec()