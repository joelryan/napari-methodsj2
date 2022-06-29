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
from magicgui.widgets import Label,ComboBox,create_widget,Container
from superqt import sliders
import pickle
import json
from urllib.request import urlopen
import json
import cv2
from aicsimageio import AICSImage
from xml.etree import ElementTree as et
from urllib import request
PARAMS={}

global fn_options 



def savejson(dic):
    with open('data.json', 'w') as fp:
        json.dump(dic, fp)

def read_json(fn,target):
    with open(fn) as json_file:
        data = json.load(json_file)
    # print(data)
        data_new = data['components']
        fn_options=[]
        for sample in data_new:
            if sample.get('Schema_ID')== target:
                fn_options.append(sample['Name'])
            else:
                pass
    return fn_options



# searching for each of the following schema_id in the hardware json file:
# MJ2_structure_file_URL = 'https://github.com/ABIF-McGill/MethodsJ2/blob/main/abif_axiovert1_.json'
# # with request.urlopen(MJ2_structure_file_URL) as url:
# #     data = json.loads(url.read())
# #     print(data)
# response = urlopen(MJ2_structure_file_URL)


# with open(response, 'r') as j:
#      contents = json.loads(j.read())
#      print(contents)
path='/Users/yuexu/Desktop/Napari/napari-ex/demo/abif_axiovert1_.json'
widget_info=['Objective.json',"ExcitationFilter.json","StandardDichroic.json","EmissionFilter.json"]
widget_params={}
for wid in widget_info:
    wid_name=wid[:-5]
    widget_params[wid_name]= read_json(path,wid)
wid_labels=list(widget_params.keys())

wid_options=list(widget_params.values())

@magicgui(
    call_button='confirm',
    filter1={'choices':wid_options[0],'label':wid_labels[0],'name':wid_labels[0]},
    filter2={'choices':wid_options[1],'label':wid_labels[1],'name':wid_labels[1]},
    filter3={'choices':wid_options[2],'label':wid_labels[2],'name':wid_labels[2]},
    filter4={'choices':wid_options[3],'label':wid_labels[3],'name':wid_labels[3]})
#give a specific value shown
def filterProperties1(filter1=wid_options[0][0],filter2=wid_options[1][0],filter3=wid_options[2][0],filter4=wid_options[3][0]) -> ImageData:
    pass

@filterProperties1.changed.connect
def store_params(event):
    widget = event.value
    PARAMS[widget.name] = {
        n: p.default for n, p in widget.__signature__.parameters.items()
    }

@magicgui(
    call_button='confirm',
    filter2={'choices':wid_options[1],'label':wid_labels[1],'name':wid_labels[1]},
    filter3={'choices':wid_options[2],'label':wid_labels[2],'name':wid_labels[2]},
    filter4={'choices':wid_options[3],'label':wid_labels[3],'name':wid_labels[3]})
#give a specific value shown
def filterProperties2(filter2=wid_options[1][0],filter3=wid_options[2][0],filter4=wid_options[3][0]) -> ImageData:
    pass

@filterProperties2.changed.connect
def store_params(event):
    widget = event.value
    PARAMS[widget.name] = {
        n: p.default for n, p in widget.__signature__.parameters.items()
    }

@magicgui(
    call_button='confirm',    
    filter2={'choices':wid_options[1],'label':wid_labels[1],'name':wid_labels[1]},
    filter3={'choices':wid_options[2],'label':wid_labels[2],'name':wid_labels[2]},
    filter4={'choices':wid_options[3],'label':wid_labels[3],'name':wid_labels[3]})
#give a specific value shown
def filterProperties3(filter2=wid_options[1][0],filter3=wid_options[2][0],filter4=wid_options[3][0]) -> ImageData:
    pass

@filterProperties3.changed.connect
def store_params(event):
    widget = event.value
    PARAMS[widget.name] = {
        n: p.default for n, p in widget.__signature__.parameters.items()
    }

@magicgui(
    call_button='confirm',
    filter2={'choices':wid_options[1],'label':wid_labels[1],'name':wid_labels[1]},
    filter3={'choices':wid_options[2],'label':wid_labels[2],'name':wid_labels[2]},
    filter4={'choices':wid_options[3],'label':wid_labels[3],'name':wid_labels[3]})
#give a specific value shown
def filterProperties4(filter2=wid_options[1][0],filter3=wid_options[2][0],filter4=wid_options[3][0]) -> ImageData:
    pass

@filterProperties4.changed.connect
def store_params(event):
    widget = event.value
    PARAMS[widget.name] = {
        n: p.default for n, p in widget.__signature__.parameters.items()
    }

@magicgui(
    call_button='confirm',
    filter2={'choices':wid_options[1],'label':wid_labels[1],'name':wid_labels[1]},
    filter3={'choices':wid_options[2],'label':wid_labels[2],'name':wid_labels[2]},
    filter4={'choices':wid_options[3],'label':wid_labels[3],'name':wid_labels[3]})
#give a specific value shown
def filterProperties5(filter2=wid_options[1][0],filter3=wid_options[2][0],filter4=wid_options[3][0]) -> ImageData:
    pass

@filterProperties5.changed.connect
def store_params(event):
    widget = event.value
    PARAMS[widget.name] = {
        n: p.default for n, p in widget.__signature__.parameters.items()
    }



@magicgui(
    auto_call=True,
    Micro_Meta_App_json_file={'mode': 'r'}, 
    call_button='Run',
    layout='vertical'
)


#give a specific value shown
def fileSelection(Image: ImageData,  Micro_Meta_App_json_file =  pathlib.Path.home()) -> ImageData:
    try:
        fn_options= read_json(Micro_Meta_App_json_file)
    except:
        fn_options=None

def update(f: str):
    fn_options= f

    filterProperty=[filterProperties1,filterProperties2,filterProperties3,filterProperties4,filterProperties5]

    # if fn_options != None:
    container = Container(widgets=[create_widget(value=dim[i],name=list1[i],options={'max':2**20}) for i in range(len(list1))])
    viewer.window.add_dock_widget(container,name='Image Dimensions')
    numChannels=dim[2]
    for i in range(numChannels):
        viewer.window.add_dock_widget(filterProperty[i])
    viewer.window.add_dock_widget(microscopeProperties,name='Microscope Descriptors')

 #######################Microscope descriptor
@magicgui(
    call_button='confirm',
    Microscope_descriptor={'choices':['None','Camera (widefield, TIRF, spinning disk)', 'PMT (confocal, multiphoton)']})
#give a specific value shown
def microscopeProperties(Microscope_descriptor='None') -> ImageData:
    pass

@microscopeProperties.changed.connect
def store_params(event):
    widget = event.value
    PARAMS[widget.name] = {
        n: p.default for n, p in widget.__signature__.parameters.items()
    }
    if PARAMS[widget.name]['Microscope_descriptor']=='Camera (widefield, TIRF, spinning disk)':
        if len(scanningProperties) >= 1:
            # viewer.window.remove_dock_widget(scanningProperties) 
            scanningProperties.pop(0).native.close()
            viewer.window.add_dock_widget(channelProperties,name='Channel Properties')
        else:
            viewer.window.add_dock_widget(channelProperties,name='Channel Properties')


    if PARAMS[widget.name]['Microscope_descriptor']=='PMT (confocal, multiphoton)':
        if len(channelProperties) >= 1:
            channelProperties.pop(0).native.close()
            viewer.window.add_dock_widget(scanningProperties,name='Scanning Properties')
        else:
            viewer.window.add_dock_widget(scanningProperties,name='Scanning Properties')


    savejson(PARAMS)   


@magicgui(
    call_button='confirm',
    exposureTime={'label':'Exposure time'},
    lightSource={'label':"Light source intensity"},
    Binning={'choices':['1x1', '2x2', '4x4']},
    layout='vertical')
#give a specific value shown
def channelProperties(exposureTime:float = None,lightSource:float = None,Binning='1x1') -> ImageData:
# def image_dimensions(layer: ImageData,lens_option='c') -> ImageData:
    """Apply a gaussian blur to ``layer``."""
    pass

@channelProperties.changed.connect
def store_params(event):
    widget = event.value
    PARAMS[widget.name] = {
        n: p.default for n, p in widget.__signature__.parameters.items()
    }
    savejson(PARAMS)


#####################Scanning properties
@magicgui(
    call_button='confirm',
    Dwell_Time={'label':'Dwell Time'},
    averaging={'label':"Averaging"},
    gain={'label':"Gain"},
    pinhole={'label':"Pinhole"},
    layout='vertical')
#give a specific value shown
def scanningProperties(Dwell_Time:float = 1,averaging:float = 1,gain:float = 800,pinhole:float = 1) -> ImageData:
    pass

@scanningProperties.changed.connect
def store_params(event):
    widget = event.value
    PARAMS[widget.name] = {
        n: p.default for n, p in widget.__signature__.parameters.items()
    }
    savejson(PARAMS)



viewer = napari.Viewer()
dim=[512,512,1,1,1]
list1=['Image width in pixels (X): ', 'Image height in pixels (Y): ',  'Number of channels (C): ', 'Number of slices (Z): ','Number of frames (T): ']
@viewer.layers.events.inserted.connect
def _on_insert(event):
    img_path=viewer.layers[0].source.path
    im = AICSImage(img_path)
    meta_dim=list(im.dims[ 'X','Y','C','Z','T'])
    for i in range(len(dim)):
        dim[i]=meta_dim[i] 
    PARAMS['image_dimensions']=dim
    savejson(PARAMS)
  
    layer = event.value






viewer.window.add_dock_widget(fileSelection,name='File Selection')
 

fileSelection.Micro_Meta_App_json_file.changed.connect(update)


napari.run()