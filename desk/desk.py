import pyforms
from pyforms import basewidget as bw
from pyforms import controls as ct

class Desk(bw.BaseWidget):
    def __init__(self):
        super(Desk, self).__init__('To-do desk')

        # Definition of the forms fields
        self.nameDo = ct.ControlLabel('To-do')
        self.toAdd = ct.ControlText('Add: ')
        self.add=ct.ControlButton('Add')
        self.delet=ct.ControlButton('Delete')
        self.list = ct.ControlList()

if __name__=='__main__':
    pyforms.start_app(Desk, geometry=(500, 200, 200, 200))
