from cProfile import label
from matplotlib import widgets
from napari.types import ImageData
from magicgui import magicgui
from skimage import filters, morphology
import numpy as np
import napari
from magicgui.widgets import LineEdit, SpinBox, Container,ComboBox,Label
from superqt import spinbox
from read_file_test import *
import json
from qtpy.QtWidgets import QTreeView, QDirModel
import napari


 # setting file path
viewer = napari.Viewer()

# create view and model
tree = QTreeView()
model = QDirModel()
tree.setModel(model)

# just some styling
tree.setColumnHidden(1, True)
tree.setColumnHidden(2, True)
tree.setColumnHidden(3, True)
tree.resize(640, 480)

# set up callbacks whenever the selection changes
selection = tree.selectionModel()
@selection.currentChanged.connect
def _on_change(current, previous):
    path = model.filePath(current)

    if path.endswith('.json'):
        viewer.window.add_dock_widget(new_widget2)
        viewer.window.add_dock_widget(new_widget3)



# reading widgets information from selected files
list1=['Image width in pixels (X): ', 'Image height in pixels (Y): ', 'Number of slices (Z): ', 'Number of channels (C): ', 'Number of frames (T): ']
#select: objective
list2=[
                "Magnification",
                "LensNA",
                "Correction",
                "ContrastModulation",
                "DIC",
                "ImmersionType",
                "CorrectionCollar",
                "Manufacturer"
            ]
with open('/Users/yuexu/Desktop/Napari/napari-ex/widget_params.json') as json_file:
    data = json.load(json_file)
    # fn_options=data['fruit']
    settings=data[ "settings"]
dialog_dic={"Image dimensions":[]}


#image dimension widget
@magicgui(
    o1={'label':str(list1[0])},
    o2={'label':str(list1[1])},
    o3={'label':str(list1[2])},
    o4={'label':str(list1[3])},
    o5={'label':str(list1[4])},
    call_button='Run',
    layout='vertical'
)
#give a specific value shown
def image_dimensions(o1:float = None,o2:float = None,o3:float = None,o4:float = None,o5:float = None) -> ImageData:
    pass

#option widget
@magicgui(
    options={'choices':list2,'label':"Select objective: "},
    call_button='Run',
    layout='vertical'
)
#give a specific value shown
def add_options(options=list2[0]) -> ImageData:
    pass

new_widget3=add_options





@magicgui(
    auto_call=False,
    filter_method={
        'choices': ['None', 'median', 'gaussian', 'bilateral', 'TV'],
        'label': 'Filter Choice:',
    },
    value_slider={'widget_type': 'FloatSlider', 'max': 4},
    lens_option={'choices':['a','b','c'],'label':'file option'},
    call_button='confirm'
)
def filter_widget(
    image: ImageData, filter_method='None', value_slider=1, lens_option='a'
) -> ImageData:
    if image is None:
        return
    if lens_option is None:
        return
    if filter_method == 'median':
        tmp_img = image.copy()
        for curr_stack in range(np.shape(tmp_img)[0]):
            tmp_img[curr_stack] = filters.median(
                tmp_img[curr_stack], morphology.disk(value_slider)
            )
        return tmp_img






viewer = napari.Viewer()
viewer.window.add_dock_widget(tree)
global fn_options
thisdict = {
  "a": ["Ford",'b'],
  "b": ["Mustang",'sd'],
}
#first widget
table_widget = filter_widget
#second widget
new_widget2= image_dimensions


viewer.window.add_dock_widget(table_widget)



napari.run()