
from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui.ui_mainwindow import Ui_MainWindow  # Importa la clase generada desde el archivo Python
from model_lg import update_model, predict_quality
from database import register_data

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        
        self.ui.pushButton_quality.clicked.connect(self.viniq_page)
        self.ui.calculate_quality.clicked.connect(self.calculate_quality)
        self.ui.edit.clicked.connect(self.edit_quality)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.back.clicked.connect(self.back)
        self.ui.save.clicked.connect(self.save)

    def viniq_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def edit_quality(self):
        self.ui.quality.setReadOnly(False)

    def clear(self):
        self.ui.fixed_acidity.clear()
        self.ui.volatile_acidity.clear()
        self.ui.citric_acid.clear()
        self.ui.residual_sugar.clear()
        self.ui.chlorides.clear()
        self.ui.free_sulfur_dioxide.clear()
        self.ui.total_sulfur_dioxide.clear()
        self.ui.density.clear()
        self.ui.ph.clear()
        self.ui.sulphates.clear()
        self.ui.alcohol.clear()
        self.ui.quality.clear()

    def back(self):
        self.clear()
        self.ui.stackedWidget.setCurrentIndex(0)

    def save(self):
        msg = QMessageBox()
        msg.setWindowTitle("Confirmación")
        msg.setText("¿Estás seguro de que quieres guardar el registro?")
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg.setDefaultButton(QMessageBox.StandardButton.No)

        result = msg.exec()

        if result == QMessageBox.StandardButton.Yes:
            register_data('quality_wine', self.get_values())
            msg.setWindowTitle("Confirmación")
            msg.setText("Registro Guardado con Éxito")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            result = msg.exec()
            self.clear()
        else:
            print("Se ha cancelado.")

    def calculate_quality(self):
        model = update_model()
        quality = str(predict_quality(model, self.get_values()))
        self.ui.quality.setText(quality)
        self.ui.quality.setReadOnly(True)

    def get_values(self):
        values = {}
        values['fixed_acidity'] = self.ui.fixed_acidity.text()
        values['volatile_acidity'] = self.ui.volatile_acidity.text()
        values['citric_acid'] = self.ui.citric_acid.text()
        values['residual_sugar'] = self.ui.residual_sugar.text()
        values['chlorides'] = self.ui.chlorides.text()
        values['free_sulfur_dioxide'] = self.ui.free_sulfur_dioxide.text()
        values['total_sulfur_dioxide'] = self.ui.total_sulfur_dioxide.text()
        values['density'] = self.ui.density.text()
        values['pH'] = self.ui.ph.text()
        values['sulphates'] = self.ui.sulphates.text()
        values['alcohol'] = self.ui.alcohol.text()
        values['quality'] = self.ui.quality.text()
        return values
        