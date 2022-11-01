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
        self.labelwidgets = []
        self.valuewidgets = []
        self.initUI()
        self.initTrigger()
        self.row=-1
        self.kws =[]
        self.vws=[]
        self.PARAMS={}
        self.kvsi = 0
        self.filename= ""
        self.imgfilepath = ""
        self.meta_dim=[]
        self.default_setting={
            'dimension':{'label':['Image width in pixels (X): ', 'Image height in pixels (Y): ',  'Number of channels (C): ', 'Number of slices (Z): ','Number of frames (T): '],'sourceData':'metadata','type':'SpinBox'},
            'filter':{'label':["ExcitationFilter","StandardDichroic","EmissionFilter"],'sourceData':'hardware_json_file','type':'ComboBox'},
            'objective':{'label':['Objective'],'sourceData':'hardware_json_file','type':'ComboBox'}
            # 'other':{'label':['PiezoElectricStage'],'sourceData':'hardware_json_file','type':'ComboBox'}
               }
        self.optional_setting={'lightsource':{'label':['PiezoElectricStage'],'sourceData':'hardware_json_file','type':'ComboBox'}

        }


        self.paramkey=[]
        self.paramvalue=[]
        self.hswidgets=[]

        self.customized_setting={}
    def initUI(self):
        self.headcontentlayout =QVBoxLayout()
        self.headcontentwidget=QWidget()
        self.headcontentwidget.setLayout(self.headcontentlayout)

        self.head1 = QHBoxLayout()
        self.inputimglb = QLabel("Image")
        self.head1.addWidget(self.inputimglb)
        self.imgfilele = QLineEdit()
        self.head1.addWidget(self.imgfilele)
        self.selbtn1 = QPushButton("Select File")
        self.head1.addWidget(self.selbtn1)
        self.headcontentlayout.addLayout(self.head1)
        self.head2 = QHBoxLayout()
        self.jsonlb = QLabel("Micro Meta App json file")
        self.head2.addWidget(self.jsonlb)
        self.jsonfilele = QLineEdit()
        self.head2.addWidget(self.jsonfilele)
        self.selbtn = QPushButton("Select File")
        self.head2.addWidget(self.selbtn)
        self.headcontentlayout.addLayout(self.head2)

        self.labelwidgets.append(self.inputimglb)
        self.valuewidgets.append(self.imgfilele)
        self.labelwidgets.append(self.jsonlb)
        self.valuewidgets.append(self.jsonfilele)

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
        self.contentwidget.setMinimumWidth(480)
        #self.scroll.setWidget(self.contentwidget)
        self.scroll.setMinimumSize(400, 800)
        self.viewer.window.add_dock_widget(self.scroll)

        self.savebtn = QPushButton("Save")
        self.savebtn.clicked.connect(self.saveValue)
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
            self.labelwidgets.append(l)
            self.valuewidgets.append(cb)
            return {'label':l,'combo':cb}

        if type =='SpinBox':
            l = QLabel(label)
            sb = QSpinBox()
            sb.setMaximum(9999)
            sb.setMinimum(0)
            sb.setValue(option)
            sb.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
            self.labelwidgets.append(l)
            self.valuewidgets.append(sb)
            return [l,sb]

        if type == "LineEdit":
            l = QLabel(label)
            le = QLineEdit()
            self.labelwidgets.append(l)
            self.valuewidgets.append(le)
            return {'label':l,'le':le}


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

        ############
        for i in range(len(self.default_setting['dimension']['label'])):
            l,sb= self.widget_generation('SpinBox',self.default_setting['dimension']['label'][i],self.meta_dim[i])
            self.row+=1
            self.contentlayout.addWidget(l, self.row,0)
            self.contentlayout.addWidget(sb, self.row, 1,1,3)
            self.PARAMS['img_dim']=[l,sb]
            
        self.kw=[]
        self.vm=[]
        l = QLabel("Filter Objective "+"-"*30)
        self.row += 1
        print(self.row)
        self.contentlayout.addWidget(l, self.row, 0,1,4)

        self.row += 1
        obj_option= read_json(self.filename,'Objective.json')
        obj_info = self.widget_generation('ComboBox','objective',obj_option)
        self.contentlayout.addWidget(obj_info['label'], self.row, 0)
        self.contentlayout.addWidget(obj_info['combo'], self.row, 1, 1, 3)

        

   
        #self.meta_dim[2]: number of channels
        #get filter properties n times(n=number of channels)
        for i in range(self.meta_dim[2]):
            self.generation()
        
        self.kw =[]
        self.vw =[]
        l = QLabel("Optional Setting  "+"-"*50)
        self.row+=1
        self.contentlayout.addWidget(l, self.row, 0,1,4)
        for optionalKey in list(self.optional_setting.keys()):
            self.row+=1
            other_option= read_json(self.filename,self.optional_setting[optionalKey]['label'][0]+'.json')
            # print(other_option)
            other_info = self.widget_generation(self.optional_setting[optionalKey]['type'],self.optional_setting[optionalKey]['label'][0],other_option)
            self.contentlayout.addWidget(other_info['label'], self.row, 0)
            self.contentlayout.addWidget(other_info['combo'], self.row, 1, 1, 3)


       
        checkbox_0 = QCheckBox("Environmental conditions maintained by device \n (temperature, CO2, humidity)")
        self.row += 1
        self.contentlayout.addWidget(checkbox_0,self.row,0,1,3)
        checkbox_0.setObjectName("checkbox_0")
        checkbox_0.stateChanged.connect(lambda: self.ckchange(checkbox_0))

        self.row += 1
        temparr = []
        obj_info = self.widget_generation('ComboBox', 'Environmental Control Device:', ['LCI stage-top incubator', 'A', 'B'])
        self.contentlayout.addWidget(obj_info["label"], self.row, 0, 1, 1)
        self.contentlayout.addWidget(obj_info["combo"], self.row, 1, 1, 2)
        temparr.append(obj_info["label"])
        temparr.append(obj_info["combo"])
        self.row += 1
        obj_info = self.widget_generation('LineEdit', 'Temperature:', [])
        self.contentlayout.addWidget(obj_info["label"], self.row, 0, 1, 1)
        self.contentlayout.addWidget(obj_info["le"], self.row, 1, 1, 2)
        temparr.append(obj_info["label"])
        temparr.append(obj_info["le"])
        self.row += 1
        obj_info = self.widget_generation('LineEdit', 'CO2:', [])
        self.contentlayout.addWidget(obj_info["label"], self.row, 0, 1, 1)
        self.contentlayout.addWidget(obj_info["le"], self.row, 1, 1, 2)
        temparr.append(obj_info["label"])
        temparr.append(obj_info["le"])

        self.hswidgets.append(temparr)


        checkbox_1 = QCheckBox("Focus Stabilization:")
        self.row += 1
        self.contentlayout.addWidget(checkbox_1, self.row, 0,1,3)
        checkbox_1.setObjectName("checkbox_1")
        checkbox_1.stateChanged.connect(lambda: self.ckchange(checkbox_1))

        temparr = []
        obj_info = self.widget_generation('ComboBox', 'Focus stabilization device:',
                                          ['Definite Focus 2', 'A', 'B'])
        self.row += 1
        self.contentlayout.addWidget(obj_info["label"], self.row, 0, 1, 1)
        self.contentlayout.addWidget(obj_info["combo"], self.row, 1, 1, 2)
        temparr.append(obj_info["label"])
        temparr.append(obj_info["combo"])
        self.hswidgets.append(temparr)
        # save button
        self.row += 1
        self.contentlayout.addWidget(self.savebtn, self.row, 0, 1, 3)
        self.scroll.setWidget(self.contentwidget)
        for i in self.hswidgets:
            for w in i:
                w.setHidden(True)

    #save input
    def saveValue(self):
        self.paramkey = []
        self.paramvalue = []
        for i in range(len(self.labelwidgets)):
            self.paramkey.append(self.labelwidgets[i].text())
            try:
                self.paramvalue.append(self.valuewidgets[i].text())
                print("userinput--{}:{}".format(self.labelwidgets[i].text(),self.valuewidgets[i].text()))
            except:
                print("userinput--{}:{}".format(self.labelwidgets[i].text(), self.valuewidgets[i].currentText()))
                self.paramvalue.append(self.valuewidgets[i].currentText())
        #get value according to label
        print(self.getValue("Focus stabilization device:"))

    def getValue(self,keystr):
        #uncomment: get instant value
        #self.saveValue()
        try:
            return self.paramvalue[self.paramkey.index(keystr)]
        except Exception as e:
            print(e)

    

    def ckchange(self,ck):
        #checkbox selected or not
        ckons = ck.objectName().split("_")
        if ck.checkState():
            if ckons[0] == "ck":
                #ck_XXXX
                index = int(ckons[1])
                ks = self.kws[index]
                vs = self.vws[index]
                for i in range(len(ks)):
                    #print(ks[i].text())
                    if vs[i].objectName()=="cb":
                        print('--------------user input-----------------')
                        print(ks[i].text()+vs[i].currentText())
                    else:
                        print(ks[i].text()+vs[i].text())

            elif ckons[0] == "checkbox":
                index = int(ckons[1])
                for i in self.hswidgets[index]:
                    i.setHidden(False)
        else:
            if ckons[0] == "checkbox":
                index = int(ckons[1])
                for i in self.hswidgets[index]:
                    i.setHidden(True)

    

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

        
        
        

viewer = napari.Viewer()
ui = uic(viewer)
napari.run()