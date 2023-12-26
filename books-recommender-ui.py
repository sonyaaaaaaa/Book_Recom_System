import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QComboBox, QListWidget
import recom

class BooksRecommenderGUI(QMainWindow):
    def __init__(self, books_list):
        super().__init__()
        self.books_list = books_list
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Books Recommender')
        self.setGeometry(100, 100, 600, 600)

        # Создаем центральный виджет и макет
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Выпадающий список для названий книг
        self.bookTitleComboBox = QComboBox(self)
        self.bookTitleComboBox.addItems(self.books_list)
        layout.addWidget(self.bookTitleComboBox)

        # Кнопка для получения рекомендаций
        self.recommendButton = QPushButton('Recommend Books', self)
        self.recommendButton.clicked.connect(self.onRecommend)
        layout.addWidget(self.recommendButton)

        # Список для отображения рекомендаций
        self.recommendationList = QListWidget(self)
        layout.addWidget(self.recommendationList)

    def onRecommend(self):
        title = self.bookTitleComboBox.currentText()
        recommendations = recom.get_recommendations_new(title)  # Берём функцию из файла с ней
        self.recommendationList.clear()
        for book in recommendations:
            self.recommendationList.addItem(book)

def load_books_list():
    # Путь к файлу CSV
    books_csv_path = r"D:\univer\3course\Project_Sonya_Nastya\Proj_Sonya_Nastya\books.csv"

    try:
        books_df = pd.read_csv(books_csv_path)
        books_list = books_df['original_title'].dropna().unique().tolist()
        books_list = [title for title in books_list if str(title).strip()]  # Удаление пустых строк
        return books_list
    except Exception as e:
        print(f"Error reading the books file: {e}")
        return []

def main():
    app = QApplication(sys.argv)
    books_list = load_books_list()  # Загрузить список книг
    ex = BooksRecommenderGUI(books_list)
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
