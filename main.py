from gui import Ui_Dialog
from PyQt5 import QtWidgets,QtCore
from search import WeatherQuery
import sys

class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.handle_weather)

    def handle_weather(self):
        city = self.ui.lineEdit.text()
        api_key = "19f71c283421e05531f9f187a92c35ce"  
        weather_query = WeatherQuery(api_key)
        result = weather_query.query_weather(city)
        
        if "请求失败" in result or "解析结果异常" in result or "请求异常" in result:
            QtWidgets.QMessageBox.warning(self, "错误", result)
        else:
            weather_info = result.split("\n")
            for i in range(len(weather_info)-1):
                item = QtWidgets.QTableWidgetItem(weather_info[i])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget.setItem(0, i, item)

            future_weather_info = eval(weather_info[5])
            self.ui.tableWidget_2.setRowCount(5)
            for i in range(5):
                for j in range(4):
                    item = QtWidgets.QTableWidgetItem(future_weather_info[i][j])
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.ui.tableWidget_2.setItem(i, j, item)
                                 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())