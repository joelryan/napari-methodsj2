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

with open('/Users/yuexu/Desktop/Napari/napari-ex/widget_params.json') as json_file:
    data = json.load(json_file)
    settings=data[ "settings"]


# MJ2_structure_file_URL = 'https://github.com/joelryan/napari-methodsj2/blob/demo/widget_params.json'
# page_to_retrieve = urlopen(MJ2_structure_file_URL)
# settingsDialogJSON = json.load(page_to_retrieve)
# settings = settingsDialogJSON['settings']


list1=get_blurb_info("Image dimensions",settings)
list2=get_blurb_info("Objective",settings)



PARAMS={}



def autosave(dic):
    file = open("./output.txt", "w") 
    # show pixels and objectives only for demo
    pixels=dic["image_dimensions"]['o1']
    objective_selected= dic['add_options']['options']
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


with open('/Users/yuexu/Desktop/Napari/napari-ex/data.json') as json_file:
    data = json.load(json_file)
    options=data['fruit']

#setting range
@magicgui(
    auto_call=True,
    fn={'mode': 'r'}, 
    call_button='Run',
    layout='vertical'
)
#give a specific value shown
def gaussian_blur(layer: ImageData,  fn =  pathlib.Path.home()) -> ImageData:
    """Apply a gaussian blur to ``layer``."""

    try:
        global fn_options 
        fn_options= read_json(fn)
    except:
        fn_options=None

@magicgui(
    auto_call=True,
    wid={"max": 800, "min": 100}, 
    layout='vertical'
)

#give a specific value shown
def gaussian(layer: ImageData, wid: float = 500.0) -> ImageData:
    return None

def update(f: str):
    if len(gaussian_blur) > 2:
        del gaussian_blur[1]
    if fn_options != None:
        gaussian_blur.insert(6,ComboBox(name='n1',label='objective option',choices=fn_options))
        viewer.window.add_dock_widget(image_dimensions)
        viewer.window.add_dock_widget(add_options)
        # print(gaussian_blur.n1.value)



@magicgui(
    call_button='confirm',
    # width={'label':'width option'}, 
    o1={'label':str(list1[0])},
    o2={'label':str(list1[1])},
    o3={'label':str(list1[2])},
    o4={'label':str(list1[3])},
    o5={'label':str(list1[4])},
    layout='vertical'
)
#give a specific value shown
def image_dimensions(o1:float = None,o2:float = None,o3:float = None,o4:float = None,o5:float = None) -> ImageData:
# def image_dimensions(layer: ImageData,lens_option='c') -> ImageData:
    """Apply a gaussian blur to ``layer``."""
    pass


@image_dimensions.changed.connect
def store_params(event):
    widget = event.value
    PARAMS[widget.name] = {
        n: p.default for n, p in widget.__signature__.parameters.items()
    }


@magicgui(

    options={'choices':list2,'label':"Select objective: "},
    call_button='Run',
    layout='vertical'
)
#give a specific value shown
def add_options(options=list2[0]) -> ImageData:
# def image_dimensions(layer: ImageData,lens_option='c') -> ImageData:
    """Apply a gaussian blur to ``layer``."""
    pass

@add_options.changed.connect
def store_params(event):
    widget = event.value
    PARAMS[widget.name] = {
        n: p.default for n, p in widget.__signature__.parameters.items()
    }
    print(PARAMS)
    autosave(PARAMS)



# create a viewer and add some images
viewer = napari.Viewer()
viewer.window.add_dock_widget(gaussian_blur)

gaussian_blur.changed.connect(update)

napari.run()
