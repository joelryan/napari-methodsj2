from random import choices
import napari
import skimage.data
import skimage.filters
from napari.types import ImageData
import json
from magicgui import magicgui
import numpy
import pathlib
from typing import Sequence
from magicgui.widgets import Label
from magicgui.widgets import ComboBox
from superqt import sliders
import pickle
from read_params import *
import json
from urllib.request import urlopen

PARAMS={}


# MJ2_structure_file_URL = 'https://github.com/joelryan/napari-methodsj2/blob/main/widget_params.json'
# page_to_retrieve = urlopen(MJ2_structure_file_URL)
# settingsDialogJSON = json.load(page_to_retrieve)
# settings = settingsDialogJSON['settings']

with open('/Users/yuexu/Desktop/Napari/napari-ex/widget_params.json') as json_file:
    data = json.load(json_file)
    settings=data[ "settings"]
list1=get_blurb_info("Image dimensions",settings)
list2=get_blurb_info("Objective",settings)

def read_json(fn):
    with open(fn) as json_file:
        data = json.load(json_file)
        data_new = data['components']
        global fn_options
        fn_options=[]
        for sample in data_new:
            if sample.get('Schema_ID')== 'Objective.json':
                fn_options.append(sample['Name'])
            else:
                pass
    return fn_options
    
# list1=['Image width in pixels (X): ', 'Image height in pixels (Y): ', 'Number of slices (Z): ', 'Number of channels (C): ', 'Number of frames (T): ']
# #select: objective
# list2=[
#                 "Magnification",
#                 "LensNA",
#                 "Correction",
#                 "ContrastModulation",
#                 "DIC",
#                 "ImmersionType",
#                 "CorrectionCollar",
#                 "Manufacturer"
#             ]

def autosave(dic):
    file = open("./output.txt", "w") 
    # show pixels and objectives only for demo
    pixels=dic["image_dimensions"]['o1']
    objective_selected=dic['gaussian_blur']['n1']
    # objective_selected= dic['add_options']['options']
    file.write(f'The image pixels is {pixels},Select objective is {objective_selected}') 
    file.close() 
    print(file)
    return None


def read_json(fn):
    with open(fn) as json_file:
        data = json.load(json_file)
        # print(data)
        data_new = data['components']
        global fn_options
        fn_options=[]
        for sample in data_new:
            if sample.get('Schema_ID')== 'Objective.json':
                fn_options.append(sample['Name'])
            else:
                pass
    return fn_options


@magicgui(
    auto_call=True,
    # width={'label':'width option'}, 
    o1={'label':str(list1[0])},
    o2={'label':str(list1[1])},
    o3={'label':str(list1[2])},
    o4={'label':str(list1[3])},
    o5={'label':str(list1[4])},
    layout='vertical'
)
#give a specific value shown
def image_dimensions(o1:float = 512,o2:float = 512,o3:float = 512,o4:float = 0,o5:float = 0) -> ImageData:
# def image_dimensions(layer: ImageData,lens_option='c') -> ImageData:
    """Apply a gaussian blur to ``layer``."""
    pass


#setting range
@magicgui(
    auto_call=True,
    Micro_Meta_App_json_file={'mode': 'r'}, 
    call_button='Run',
    layout='vertical'
)

#give a specific value shown
def gaussian_blur(layer: ImageData,  Micro_Meta_App_json_file =  pathlib.Path.home()) -> ImageData:
    """Apply a gaussian blur to ``layer``."""

    try:
        global fn_options 
        fn_options= read_json(Micro_Meta_App_json_file)
    except:
        fn_options=None


def update(f: str):
    if len(gaussian_blur) > 2:
        del gaussian_blur[1]
    if fn_options != None:
        gaussian_blur.insert(3,ComboBox(name='n1',label='Select Objective',choices=fn_options))
        viewer.window.add_dock_widget(image_dimensions)
      

@gaussian_blur.changed.connect
def store_params(event):
    widget = event.value
    PARAMS[widget.name] = {
        n: p.default for n, p in widget.__signature__.parameters.items()
    }


@image_dimensions.changed.connect
def store_params(event):
    widget = event.value
    PARAMS[widget.name] = {
        n: p.default for n, p in widget.__signature__.parameters.items()
    }
    autosave(PARAMS)

viewer = napari.Viewer()
viewer.window.add_dock_widget(gaussian_blur)

gaussian_blur.changed.connect(update)

napari.run()