from os import read
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
import json
from urllib.request import urlopen
import json


PARAMS={}




def savejson(dic):
    with open('data.json', 'w') as fp:
        json.dump(dic, fp)

def read_json(fn,target):
    with open(fn) as json_file:
        data = json.load(json_file)
        # print(data)
        data_new = data['components']
        global fn_options
        fn_options=[]
        for sample in data_new:
            if sample.get('Schema_ID')== target:
                fn_options.append(sample['Name'])
            else:
                pass
    return fn_options

# searching for each of the following schema_id in the hardware json file:
path='/Users/yuexu/Desktop/Napari/napari-ex/demo/abif_axiovert1_.json'
widget_info=["ExcitationFilter.json","StandardDichroic.json","EmissionFilter.json"]
widget_params={}
for wid in widget_info:
    wid_name=wid[:-5]
    widget_params[wid_name]= read_json(path,wid)

list1=['Image width in pixels (X): ', 'Image height in pixels (Y): ', 'Number of slices (Z): ', 'Number of channels (C): ', 'Number of frames (T): ']


@magicgui(
    call_button='confirm',
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
    savejson(PARAMS)


viewer = napari.Viewer()
viewer.window.add_dock_widget(image_dimensions)
# insert three widgets similar to the Objectives widget:"ExcitationFilter.json""StandardDichroic.json""EmissionFilter.json"
for i in range(len(widget_params)):
    wid_labels=list(widget_params.keys())[i]
    wid_choices=widget_params[wid_labels]
    wid_name=wid_labels
    image_dimensions.insert(i+6,ComboBox(name=wid_name,label=wid_labels,choices=wid_choices))



napari.run()