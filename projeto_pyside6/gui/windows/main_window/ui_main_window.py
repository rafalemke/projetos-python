from qt_core import *

# IMPORT PAGES
from gui.pages.ui_pages import Ui_StackedWidget



# MAIN WINDOW
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # SET INITIAL PARAMETERS
        parent.resize(1200,680)
        parent.setMinimumSize(960,540)

        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        

        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)
        

        # LEFT MENU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")
        

        # CONTENT LAYOUT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        # TOP BAR
        self.topBar = QFrame()
        self.topBar.setMaximumHeight(30)
        self.topBar.setMinimumHeight(30)
        self.topBar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.topBar_Layout = QHBoxLayout(self.topBar)
        self.topBar_Layout.setContentsMargins(10,0,10,0)

        # LEFT LABEL
        self.top_label_left = QLabel("Minha primeira aplicação utilizando PySide6")

        # TOP SPACER
        self.top_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # RIGHT LABEL
        self.top_label_right = QLabel("| PÁGINA INICIAL")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # ADD TO TOPBAR LAYOUT
        self.topBar_Layout.addWidget(self.top_label_left)
        self.topBar_Layout.addItem(self.top_spacer)
        self.topBar_Layout.addWidget(self.top_label_right)

        # APP PAGES

        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2")
        self.ui_pages = Ui_StackedWidget()
        self.ui_pages.setupUi(self.pages)

        # BOTTOM BAR
        self.BottomBar = QFrame()
        self.BottomBar.setMaximumHeight(30)
        self.BottomBar.setMinimumHeight(30)
        self.BottomBar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.BottomBar_Layout = QHBoxLayout(self.BottomBar)
        self.BottomBar_Layout.setContentsMargins(10,0,10,0)

        # LEFT LABEL
        self.Bottom_label_left = QLabel("Criado por Rafael")

        # TOP SPACER
        self.Bottom_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # RIGHT LABEL
        self.Bottom_label_right = QLabel("@ 2024")
        self.Bottom_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # ADD TO BOTTOM BAR LAYOUT
        self.BottomBar_Layout.addWidget(self.Bottom_label_left)
        self.BottomBar_Layout.addItem(self.Bottom_spacer)
        self.BottomBar_Layout.addWidget(self.Bottom_label_right)

        # ADD TO CONTENT LAYOUT
        self.content_layout.addWidget(self.topBar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.BottomBar)


        # ADD WIDGETS TO APP
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)



        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)
