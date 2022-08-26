from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from qtpy.QtWidgets import QTreeView, QDirModel
import napari
from aicsimageio import AICSImage
import json

def read_json(fn,target):
    with open(fn) as json_file:
        data = json.load(json_file)
        data_new = data['components']
        fn_options=[]
        for sample in data_new:
            if sample.get('Schema_ID')== target:
                fn_options.append(sample['Name'])
            else:
                pass
    return fn_options



class uic(object):
    def __init__(self,viewer):
        super(uic, self).__init__()
        self.viewer = viewer
        self.initUI()
        self.initTrigger()
        self.row=0
        self.kws =[]
        self.vws=[]
        self.PARAMS={}
        self.kvsi = 0
        self.filename= ""
        self.imgfilepath = ""
        self.meta_dim=[]
        self.default_setting={
            'dimension':{'label':['Image width in pixels (X): ', 'Image height in pixels (Y): ',  'Number of channels (C): ', 'Number of slices (Z): ','Number of frames (T): '],'type':'ComboBox'},
            'filter':{'label':["ExcitationFilter","StandardDichroic","EmissionFilter"],'type':'ComboBox'}
               }
        self.customized_setting={}
    def initUI(self):
        self.headcontentlayout =QVBoxLayout()
        self.headcontentwidget=QWidget()
        self.headcontentwidget.setLayout(self.headcontentlayout)

        self.head1 = QHBoxLayout()
        self.head1.addWidget(QLabel("Image"))

        self.imgfilele = QLineEdit()
        self.head1.addWidget(self.imgfilele)
        self.selbtn1 = QPushButton("Select File")
        self.head1.addWidget(self.selbtn1)

        self.headcontentlayout.addLayout(self.head1)
        self.head2 = QHBoxLayout()
        self.head2.addWidget(QLabel("Micro Meta App json file"))
        self.jsonfilele = QLineEdit()
        self.head2.addWidget(self.jsonfilele)
        self.selbtn = QPushButton("Select File")
        self.head2.addWidget(self.selbtn)
        self.headcontentlayout.addLayout(self.head2)

        self.head3 = QHBoxLayout()
        self.runbtn = QPushButton("Run")
        self.head3.addWidget(self.runbtn)
        self.headcontentlayout.addLayout(self.head3)
        self.viewer.window.add_dock_widget(self.headcontentwidget,name="Select File")
        #ScrollArea starts here
        self.scroll = QScrollArea()
        self.contentwidget = QWidget()
        self.contentlayout = QGridLayout()

        self.contentwidget.setLayout(self.contentlayout)
        self.contentwidget.setMinimumWidth(380)
        #self.scroll.setWidget(self.contentwidget)
        self.scroll.setMinimumSize(400, 800)
        self.viewer.window.add_dock_widget(self.scroll)

    #connect event
    def initTrigger(self):
        self.selbtn1.clicked.connect(self.selctImgFile)
        self.selbtn.clicked.connect(self.selctJsonFile)
        self.runbtn.clicked.connect(self.run)

    def selctImgFile(self):
        self.imgfilepath = QFileDialog.getOpenFileName(self.contentwidget, 'Select Json File', '', "img(*.tif *.png *.jpg);;All files (*.*)")[0]
        print(self.imgfilepath)
        if self.imgfilepath:
            im = AICSImage(self.imgfilepath)
            self.viewer.open(self.imgfilepath)
            self.meta_dim=list(im.dims[ 'X','Y','C','Z','T'])
            self.default_setting['dimension']['value']=self.meta_dim
            print(self.default_setting)
            self.imgfilele.setText(self.imgfilepath)


    def selctJsonFile(self):
        self.filename=QFileDialog.getOpenFileName(self.contentwidget,'Select Json File','', "Json(*.json)")[0]
        print(self.filename)
        if self.filename:
            self.jsonfilele.setText(self.filename)

    def widget_generation(self,type,label,option):
        if type=='ComboBox':
            l = QLabel(label)
            cb = QComboBox()
            cb.setObjectName("cb")
            cb.addItems(option)
            return {'label':l,'combo':cb}

        if type =='SpinBox':
            l = QLabel(label)
            sb = QSpinBox()
            sb.setMaximum(9999)
            sb.setMinimum(0)
            sb.setValue(option)
            sb.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
            return [l,sb]

    def run(self):
        #
        item_list = list(range(self.contentlayout.count()))
        item_list.reverse()  
        for i in item_list:
            item = self.contentlayout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()
            self.contentlayout.removeItem(item)

        #Image Dimension information
        dimk=[]
        dimv=[]
        for i in range(len(self.default_setting['dimension']['label'])):
            l,sb= self.widget_generation('SpinBox',self.default_setting['dimension']['label'][i],self.meta_dim[i])
            self.row+=1
            self.contentlayout.addWidget(l, self.row,0)
            self.contentlayout.addWidget(sb, self.row, 1,1,3)
            self.PARAMS['img_dim']=[l,sb]
            



        '''
        {'x':abc,'y': }
        l = QLabel("Image width in pixels(X):")
        sb = QSpinBox()
        sb.setMaximum(9999)
        sb.setMinimum(0)
        sb.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.contentlayout.addWidget(l, 0,0)
        self.contentlayout.addWidget(sb, 0, 1,1,3)
        sb.text()
        l = QLabel("Image width in pixels(X):")
        sb = QSpinBox()
        sb.setMaximum(9999)
        sb.setMinimum(0)
        sb.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.contentlayout.addWidget(l, 1, 0)
        self.contentlayout.addWidget(sb, 1, 1, 1, 3)

        l = QLabel("Image width in pixels(X):")
        sb = QSpinBox()
        sb.setMaximum(9999)
        sb.setMinimum(0)
        sb.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.contentlayout.addWidget(l, 2, 0)
        self.contentlayout.addWidget(sb, 2, 1, 1, 3)

        l = QLabel("Image width in pixels(X):")
        sb = QSpinBox()
        sb.setMaximum(9999)
        sb.setMinimum(0)
        sb.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.contentlayout.addWidget(l, 3, 0)
        self.contentlayout.addWidget(sb, 3, 1, 1, 3)

        l = QLabel("Image width in pixels(X):")
        sb = QSpinBox()
        sb.setMaximum(9999)
        sb.setMinimum(0)
        sb.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.contentlayout.addWidget(l, 4, 0)
        self.contentlayout.addWidget(sb, 4, 1, 1, 3)

        '''
        self.kw=[]
        self.vm=[]
        l = QLabel("Filter Objective "+"-"*50)
        self.row+=1
        self.contentlayout.addWidget(l, self.row+ self.kvsi * 9, 0,1,4)
        self.row+=1
        obj_option= read_json(self.filename,'Objective.json')
        obj_info = self.widget_generation('ComboBox','objective',obj_option)
        self.contentlayout.addWidget(obj_info['label'], self.row, 0)
        self.contentlayout.addWidget(obj_info['combo'], self.row, 1, 1, 3)
        # self.kw.append(obj_info['label'])
        # self.vw.append(obj_info['combo'])


        
        for i in range(self.meta_dim[2]):
            self.generation()
        
        # checkComplete = QPushButton("All set!")
        # checkComplete.setObjectName("finished")
        # checkComplete.stateChanged.connect(lambda: self.saveValue())
        # self.row+=1
        # self.contentlayout.addWidget(checkComplete, self.row, 0)
        self.scroll.setWidget(self.contentwidget)

    def saveValue(self):
        values={}
        for key,value in self.PARAMS.items():
            return 

    


    def ckchange(self,ck):
        if ck.checkState():
            #ck_XXXX
            index = int(ck.objectName().split("_")[1])
            ks = self.kws[index]
            vs = self.vws[index]
            for i in range(len(ks)):
                #print(ks[i].text())
                if vs[i].objectName()=="cb":
                    print('--------------user input-----------------')
                    print(ks[i].text()+vs[i].currentText())
                else:
                    print(ks[i].text()+vs[i].text())


    

    def generation(self):
        self.kw =[]
        self.vw =[]
        l = QLabel("Filter Properties  "+"-"*50)
        self.row+=1
        self.contentlayout.addWidget(l, self.row+ self.kvsi * 9, 0,1,4)
        
        for i in range(len(self.default_setting['filter']['label'])):
            self.row+=1
            filter_option= read_json(self.filename,self.default_setting['filter']['label'][i]+'.json')
            img_info = self.widget_generation('ComboBox',self.default_setting['filter']['label'][i],filter_option)
            self.contentlayout.addWidget(img_info['label'], self.row, 0)
            self.contentlayout.addWidget(img_info['combo'], self.row, 1, 1, 3)
            self.kw.append(img_info['label'])
            self.vw.append(img_info['combo'])
        self.row+=1
        ck = QCheckBox("complete")
        ck.setObjectName("ck_"+str(self.kvsi))
        ck.stateChanged.connect(lambda: self.ckchange(ck))
        self.contentlayout.addWidget(ck, self.row, 0)
        self.kws.append(self.kw)
        self.vws.append(self.vw)
        self.kvsi+=1


        
def methods_main():
    viewer = napari.Viewer()
    ui = uic(viewer)
    napari.run()