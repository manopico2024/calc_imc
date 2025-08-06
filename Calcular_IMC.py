# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_telaPrincipal(object):
    def setupUi(self, telaPrincipal):
        telaPrincipal.setObjectName("telaPrincipal")
        telaPrincipal.resize(899, 703)
        self.centralwidget = QtWidgets.QWidget(telaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_gerarRelatorio = QtWidgets.QPushButton(self.frame_5)
        self.btn_gerarRelatorio.setObjectName("btn_gerarRelatorio")
        self.gridLayout_3.addWidget(self.btn_gerarRelatorio, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_5, 1, 0, 1, 1)
        self.frame_titulo = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        self.frame_titulo.setSizePolicy(sizePolicy)
        self.frame_titulo.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_titulo.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_titulo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_titulo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_titulo.setObjectName("frame_titulo")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_titulo)
        self.label_titulo = QtWidgets.QLabel(self.frame_titulo)
        font = QtGui.QFont("Times New Roman", 14)
        self.label_titulo.setFont(font)
        self.label_titulo.setObjectName("label_titulo")
        self.gridLayout_9.addWidget(self.label_titulo, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.frame_titulo, 0, 0, 1, 2)
        self.gb_relatorio = QtWidgets.QGroupBox(self.frame_2)
        self.gb_relatorio.setObjectName("gb_relatorio")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.gb_relatorio)
        self.entry_relatorio = QtWidgets.QTextEdit(self.gb_relatorio)
        self.entry_relatorio.setObjectName("entry_relatorio")
        self.gridLayout_13.addWidget(self.entry_relatorio, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.gb_relatorio, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_3)
        self.gb_principal = QtWidgets.QGroupBox(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        self.gb_principal.setFont(font)
        self.gb_principal.setObjectName("gb_principal")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gb_principal)
        self.tb_calcularImc = QtWidgets.QTabWidget(self.gb_principal)
        font.setBold(False)
        self.tb_calcularImc.setFont(font)
        self.tb_calcularImc.setObjectName("tb_calcularImc")
        self.tab = QtWidgets.QWidget()
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab)
        self.frame_8 = QtWidgets.QFrame(self.tab)
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_9)
        self.label_peso = QtWidgets.QLabel(self.frame_9)
        font.setPointSize(14)
        font.setBold(True)
        self.label_peso.setFont(font)
        self.verticalLayout_2.addWidget(self.label_peso)
        self.label_altura = QtWidgets.QLabel(self.frame_9)
        self.label_altura.setFont(font)
        self.verticalLayout_2.addWidget(self.label_altura)
        self.gridLayout_12.addWidget(self.frame_9, 0, 0, 1, 1)
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_10)
        self.entry_peso = QtWidgets.QLineEdit(self.frame_10)
        self.gridLayout_11.addWidget(self.entry_peso, 0, 0, 1, 1)
        self.entry_altura = QtWidgets.QLineEdit(self.frame_10)
        self.gridLayout_11.addWidget(self.entry_altura, 1, 0, 1, 1)
        self.gridLayout_12.addWidget(self.frame_10, 0, 1, 1, 1)
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_11)
        self.btn_calcularImc = QtWidgets.QPushButton(self.frame_11)
        self.gridLayout_7.addWidget(self.btn_calcularImc, 0, 0, 1, 1)
        self.label_resultado = QtWidgets.QLabel(self.frame_11)
        font.setPointSize(9)
        font.setBold(True)
        self.label_resultado.setFont(font)
        self.gridLayout_7.addWidget(self.label_resultado, 1, 0, 1, 1)
        self.gridLayout_12.addWidget(self.frame_11, 1, 0, 1, 2)
        self.gridLayout_10.addWidget(self.frame_8, 0, 0, 1, 1)
        self.tb_calcularImc.addTab(self.tab, "")
        self.gridLayout_8.addWidget(self.tb_calcularImc, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.gb_principal, 0, 1, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_6)
        self.lv_relatorio = QtWidgets.QListView(self.frame_6)
        self.gridLayout_6.addWidget(self.lv_relatorio, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_6, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        telaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(telaPrincipal)
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        telaPrincipal.setMenuBar(self.menubar)
        self.actionPredicoes = QtWidgets.QAction(telaPrincipal)
        self.menuMenu.addAction(self.actionPredicoes)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(telaPrincipal)
        self.tb_calcularImc.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(telaPrincipal)

        # === Banco de dados ===
        self.conn = sqlite3.connect("relatorios_imc.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS relatorios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                texto TEXT NOT NULL
            )
        """)
        self.conn.commit()

        self.modelo_relatorio = QtCore.QStringListModel()
        self.lv_relatorio.setModel(self.modelo_relatorio)
        self.lista_relatorios = []
        self.carregar_relatorios()

        self.btn_calcularImc.clicked.connect(self.executar_calculo)
        self.btn_gerarRelatorio.clicked.connect(self.gerar_relatorio)

    def retranslateUi(self, telaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        telaPrincipal.setWindowTitle(_translate("telaPrincipal", "Calcular IMC Relatorio do Aluno"))
        self.btn_gerarRelatorio.setText(_translate("telaPrincipal", "Gerar Relatório"))
        self.label_titulo.setText(_translate("telaPrincipal", "Calcular IMC"))
        self.gb_relatorio.setTitle(_translate("telaPrincipal", "Relatório do Aluno:"))
        self.gb_principal.setTitle(_translate("telaPrincipal", "Calcula IMC:"))
        self.label_peso.setText(_translate("telaPrincipal", "Peso(Kg):"))
        self.label_altura.setText(_translate("telaPrincipal", "Altura(m):"))
        self.btn_calcularImc.setText(_translate("telaPrincipal", "Calcular IMC"))
        self.label_resultado.setText(_translate("telaPrincipal", "Resultado:"))
        self.tb_calcularImc.setTabText(self.tb_calcularImc.indexOf(self.tab), _translate("telaPrincipal", "Calcular IMC"))
        self.menuMenu.setTitle(_translate("telaPrincipal", "Menu"))
        self.actionPredicoes.setText(_translate("telaPrincipal", "Predições"))

    def calcular_imc(self, peso, altura):
        try:
            return peso / (altura ** 2)
        except ZeroDivisionError:
            return 0

    def interpretar_imc(self, imc):
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 25:
            return "Peso normal"
        elif 25 <= imc < 30:
            return "Sobrepeso"
        elif 30 <= imc < 35:
            return "Obesidade grau I"
        elif 35 <= imc < 40:
            return "Obesidade grau II"
        else:
            return "Obesidade grau III"

    def executar_calculo(self):
        peso_texto = self.entry_peso.text()
        altura_texto = self.entry_altura.text()
        try:
            peso = float(peso_texto)
            altura = float(altura_texto)
            imc = self.calcular_imc(peso, altura)
            classificacao = self.interpretar_imc(imc)
            resultado = f"IMC: {imc:.2f} - {classificacao}"
        except ValueError:
            resultado = "Erro: insira valores numéricos válidos."
        self.label_resultado.setText(resultado)

    def gerar_relatorio(self):
        texto_adicional = self.entry_relatorio.toPlainText().strip()
        resultado_imc = self.label_resultado.text().strip()
        if not resultado_imc or resultado_imc == "Resultado:":
            resultado_imc = "IMC ainda não calculado."
        if not texto_adicional:
            texto_adicional = "Sem observações adicionais."
        relatorio_final = f"{resultado_imc} | Observações: {texto_adicional}"
        self.cursor.execute("INSERT INTO relatorios (texto) VALUES (?)", (relatorio_final,))
        self.conn.commit()
        self.lista_relatorios.append(relatorio_final)
        self.modelo_relatorio.setStringList(self.lista_relatorios)
        self.entry_relatorio.clear()

    def carregar_relatorios(self):
        self.cursor.execute("SELECT texto FROM relatorios")
        resultados = self.cursor.fetchall()
        self.lista_relatorios = [r[0] for r in resultados]
        self.modelo_relatorio.setStringList(self.lista_relatorios)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    telaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_telaPrincipal()
    ui.setupUi(telaPrincipal)
    telaPrincipal.show()
    exit_code = app.exec_()
    ui.conn.close()
    sys.exit(exit_code)
