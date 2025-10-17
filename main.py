from PyQt5.QtWidgets import (QDialog, QMessageBox, 
QMainWindow, QApplication, QTreeWidgetItem,
QVBoxLayout, QTextEdit, QPushButton, QShortcut,
QHBoxLayout, QComboBox, QLabel, QInputDialog)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QPushButton, QTreeWidget, QTreeWidgetItem, QTableWidgetItem,
                           QLineEdit, QLabel, QMessageBox, QFileDialog)
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QKeySequence
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from Calcular_IMC4 import Ui_telaPrincipal
import sys
import sqlite3
import datetime

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_telaPrincipal()
        self.ui.setupUi(self)
        
        # Inicializar componentes da UI
        self.init_ui_components()
        
        # Inicializar banco de dados
        self.init_database()
        
        # Conectar sinais e slots
        self.connect_signals()

    def init_ui_components(self):
        self.entry_peso = self.ui.entry_peso 
        self.entry_altura = self.ui.entry_altura
        self.entry_relatorio = self.ui.entry_relatorio
        self.label_resultado = self.ui.label_resultado
        self.lv_relatorio = self.ui.lv_relatorio
        
        # Botões (ajuste os nomes conforme seu arquivo UI)
        self.btn_calcular = self.ui.btn_calcular
        self.btn_gerar_relatorio = self.ui.btn_gerar_relatorio
        self.btn_excluir_relatorio = self.ui.btn_excluir_relatorio
        self.btn_limpar = self.ui.btn_limpar

    def init_database(self):
        self.db_path = "imc_data.db"
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        
        # Criar tabela se não existir
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS relatorios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                texto TEXT NOT NULL,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
        self.conn.commit()

        # Inicializar modelo para a lista de relatórios
        self.modelo_relatorio = QtCore.QStringListModel()
        self.lv_relatorio.setModel(self.modelo_relatorio)
        self.lista_relatorios = []
        self.carregar_relatorios()

    def connect_signals(self):
        self.btn_calcular.clicked.connect(self.executar_calculo)
        self.btn_gerar_relatorio.clicked.connect(self.gerar_relatorio)
        self.btn_excluir_relatorio.clicked.connect(self.excluir_relatorio)
        self.btn_limpar.clicked.connect(self.limpar_campos)

    def calcular_imc(self, peso, altura):
        try:
            return peso / (altura ** 2)
        except ZeroDivisionError:
            return 0

    def interpretar_imc(self, imc): 
        if imc < 18.5:
            texto = "Resultado: Abaixo do peso"
            cor = "blue"
        elif 18.5 <= imc < 25:
            texto = "Resultado: Peso normal"
            cor = "green"
        elif 25 <= imc < 30:
            texto = "Resultado: Sobrepeso"
            cor = "orange"
        elif 30 <= imc < 35:
            texto = "Resultado: Obesidade grau I"
            cor = "red"
        elif 35 <= imc < 40:
            texto = "Resultado: Obesidade grau II"
            cor = "darkred"
        else:
            texto = "Resultado: Obesidade grau III"
            cor = "purple"
        self.label_resultado.setStyleSheet(f"color: {cor}; font-weight: bold;")
        return texto

    def executar_calculo(self):
        peso_texto = self.entry_peso.text().strip()
        altura_texto = self.entry_altura.text().strip()
        # Verificar se os campos estão vazios
        if not peso_texto or not altura_texto:
            QtWidgets.QMessageBox.warning(
                self, 
                "Campos Vazios", 
                "Por favor, preencha ambos os campos (peso e altura) para calcular o IMC.")
            return
            
        try:
            peso = float(peso_texto.replace(',', '.'))
            altura = float(altura_texto.replace(',', '.'))
            # Verificar se os valores são válidos
            if peso <= 0 or altura <= 0:
                QtWidgets.QMessageBox.warning(
                    self, 
                    "Valores Inválidos", 
                    "Por favor, insira valores positivos para peso e altura.")
                return
            imc = self.calcular_imc(peso, altura)
            classificacao = self.interpretar_imc(imc)
            
            # Atualizar o label com o resultado formatado
            resultado_texto = f"{classificacao}\nIMC: {imc:.2f}"
            self.label_resultado.setText(resultado_texto)
            
        except ValueError:
            QtWidgets.QMessageBox.warning(
                self, 
                "Valores Inválidos", 
                "Por favor, insira valores numéricos válidos para peso e altura.")
            self.label_resultado.setText("Erro: insira valores numéricos válidos.")
            self.label_resultado.setStyleSheet("color: red; font-weight: bold;")

    def excluir_relatorio(self):
        # Pega o índice selecionado no QListView
        indice = self.lv_relatorio.currentIndex()
        if not indice.isValid():
            QtWidgets.QMessageBox.warning(
                self, 
                "Nenhum Item Selecionado", 
                "Por favor, selecione um relatório na lista para excluir."
            )
            return  # nada selecionado
        # Confirmar exclusão
        resposta = QtWidgets.QMessageBox.question(
            self,
            "Confirmar Exclusão",
            "Tem certeza que deseja excluir este relatório?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)
        if resposta == QtWidgets.QMessageBox.No:
            return
        # Pega o texto selecionado
        texto = self.lista_relatorios[indice.row()]
        # Exclui do banco
        self.cursor.execute("DELETE FROM relatorios WHERE texto = ?", (texto,))
        self.conn.commit()
        # Atualiza a lista
        self.carregar_relatorios()
        QtWidgets.QMessageBox.information(
            self, 
            "Exclusão Concluída", 
            "Relatório excluído com sucesso.")

    def gerar_relatorio(self):
        # Verificar se o IMC foi calculado
        resultado_imc = self.label_resultado.text().strip()
        if resultado_imc == "Resultado:" or resultado_imc.startswith("Erro:"):
            QtWidgets.QMessageBox.warning(
                self, 
                "IMC Não Calculado", 
                "Por favor, calcule o IMC antes de gerar um relatório.")
            return
            
        texto_adicional = self.entry_relatorio.toPlainText().strip()
        if not texto_adicional:
            resposta = QtWidgets.QMessageBox.question(
                self,
                "Observações Vazias",
                "Não há observações adicionais. Deseja gerar o relatório mesmo assim?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No)
            if resposta == QtWidgets.QMessageBox.No:
                return
            texto_adicional = "Sem observações adicionais."
            
        # Criar relatório com timestamp
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        relatorio_final = f"[{data_atual}] {resultado_imc} | Observações: {texto_adicional}"
        
        # Salvar no banco
        self.cursor.execute("INSERT INTO relatorios (texto) VALUES (?)", (relatorio_final,))
        self.conn.commit()
        
        # Atualizar interface
        self.carregar_relatorios()
        self.entry_relatorio.clear()
        
        QtWidgets.QMessageBox.information(
            self, 
            "Relatório Gerado", 
            "Relatório salvo com sucesso!"
        )

    def carregar_relatorios(self):
        self.cursor.execute("SELECT texto FROM relatorios ORDER BY data_criacao DESC")
        resultados = self.cursor.fetchall()
        self.lista_relatorios = [r[0] for r in resultados]
        self.modelo_relatorio.setStringList(self.lista_relatorios)

    def limpar_campos(self):
        self.entry_altura.clear()
        self.entry_peso.clear()
        self.entry_relatorio.clear()
        self.label_resultado.setText("Resultado:")
        self.label_resultado.setStyleSheet("")  # Remove estilos anteriores

    def closeEvent(self, event):
        self.conn.close()
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())