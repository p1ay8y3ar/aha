'''
Description: Editor's info in the top of the file
Author: p1ay8y3ar
Date: 2021-03-31 22:03:06
LastEditor: p1ay8y3ar
LastEditTime: 2021-03-31 23:34:15
Email: p1ay8y3ar@gmail.com
'''
import sys
import src
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    md = src.LoginWindow()
    md.show()
    sys.exit(app.exec_())