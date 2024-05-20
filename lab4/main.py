import sys
from PyQt5.QtWidgets import QApplication as QApp, QMainWindow as QMainWin, QPushButton as QBtn, QVBoxLayout as VBoxLayout, QWidget as Wdg, QLabel as QLbl, QGraphicsView as QGraphView, QGraphicsScene as QGraphScene, QLineEdit as QLineEd
from PyQt5.QtCore import Qt as QtCore, pyqtSignal as pySig, QThread as QTh
import random
import time
from sort_algorithms import SelectionSort as SelSort, QuickSort as QuSort, InsertionSort as InsSort


class SThread(QTh):
    update_sig = pySig(list)

    def __init__(self, s_obj):
        super().__init__()
        self.s_obj = s_obj

    def run(self):
        s_time = time.time()
        for a in self.s_obj.sort():
            self.update_sig.emit(a)
            time.sleep(0.01)
        e_time = time.time()
        self.execution_time = e_time - s_time


class SApp(QMainWin):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SApp")
        self.setGeometry(100, 100, 800, 600)

        self.b_arr_size = 100
        self.b_arr = [random.randint(0, 1000) for _ in range(self.b_arr_size)]

        self.s_alg_quick = QuSort(self.b_arr.copy())
        self.s_alg_selection = SelSort(self.b_arr.copy())
        self.s_alg_insertion = InsSort(self.b_arr.copy())

        self.setup_ui()

    def setup_ui(self):
        c_widget = Wdg()
        self.setCentralWidget(c_widget)

        layout = VBoxLayout()

        self.arr_size_input = QLineEd()
        self.arr_size_input.setPlaceholderText("Enter array size (max 10000)")
        layout.addWidget(self.arr_size_input)

        self.start_button = QBtn("Start Sorting")
        self.start_button.clicked.connect(self.start_sorting)
        layout.addWidget(self.start_button)

        self.quick_sort_label = QLbl("Quick Sort:")
        layout.addWidget(self.quick_sort_label)
        self.quick_sort_view = QGraphView()
        layout.addWidget(self.quick_sort_view)

        self.selection_sort_label = QLbl("Selection Sort:")
        layout.addWidget(self.selection_sort_label)
        self.selection_sort_view = QGraphView()
        layout.addWidget(self.selection_sort_view)

        self.insertion_sort_label = QLbl("Insertion Sort:")
        layout.addWidget(self.insertion_sort_label)
        self.insertion_sort_view = QGraphView()
        layout.addWidget(self.insertion_sort_view)

        c_widget.setLayout(layout)

    def start_sorting(self):
        arr_size = int(self.arr_size_input.text()) if self.arr_size_input.text().isdigit() else 100
        if arr_size > 10000:
            arr_size = 10000
        self.b_arr = [random.randint(0, 1000) for _ in range(arr_size)]

        self.s_alg_quick = QuSort(self.b_arr.copy())
        self.s_alg_selection = SelSort(self.b_arr.copy())
        self.s_alg_insertion = InsSort(self.b_arr.copy())

        self.s_thread_quick = SThread(self.s_alg_quick)
        self.s_thread_quick.update_sig.connect(self.update_sorting_quick)
        self.s_thread_quick.start()

        self.s_thread_selection = SThread(self.s_alg_selection)
        self.s_thread_selection.update_sig.connect(self.update_sorting_selection)
        self.s_thread_selection.start()

        self.s_thread_insertion = SThread(self.s_alg_insertion)
        self.s_thread_insertion.update_sig.connect(self.update_sorting_insertion)
        self.s_thread_insertion.start()

    def update_sorting_quick(self, a):
        self.update_graph(self.quick_sort_view, a)

    def update_sorting_selection(self, a):
        self.update_graph(self.selection_sort_view, a)

    def update_sorting_insertion(self, a):
        self.update_graph(self.insertion_sort_view, a)

    def update_graph(self, v, a):
        scene = QGraphScene()
        s_factor = 0.3
        t_width = v.width()
        n_elements = len(a)

        b_width = t_width / n_elements

        for i, h in enumerate(a):
            s_height = h * s_factor
            scene.addRect(i * b_width, 0, b_width, s_height)

        v.setScene(scene)


if __name__ == "__main__":
    app = QApp(sys.argv)
    s_app = SApp()
    s_app.show()
    sys.exit(app.exec_())
