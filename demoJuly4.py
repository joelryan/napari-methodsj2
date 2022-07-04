from os import read
from random import choices
from click import confirm
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




def savejson(dic):
    with open('Output.json', 'w') as fp:
        json.dump(dic, fp)

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

path='/Users/yuexu/Desktop/Napari/napari-ex/demo/abif_axiovert1_.json'
widget_info=['Objective.json',"ExcitationFilter.json","StandardDichroic.json","EmissionFilter.json"]
widget_params={}
for wid in widget_info:
    wid_name=wid[:-5]
    widget_params[wid_name]= read_json(path,wid)
wid_labels=list(widget_params.keys())
wid_options=list(widget_params.values())


@magicgui(
    auto_call=True,
    filter1={'choices':wid_options[0],'label':wid_labels[0],'name':wid_labels[0]},
    filter2={'choices':wid_options[1],'label':wid_labels[1],'name':wid_labels[1]},
    filter3={'choices':wid_options[2],'label':wid_labels[2],'name':wid_labels[2]},
    filter4={'choices':wid_options[3],'label':wid_labels[3],'name':wid_labels[3]},
    isComplete={"widget_type": "CheckBox", "value": False, "name": "complete"})
#give a specific value shown
def filterProperties1(filter1=wid_options[0][0],filter2=wid_options[1][0],filter3=wid_options[2][0],filter4=wid_options[3][0],Exposure_Time='0',Light_source_intensity='0',Binning='0',isComplete: bool=False) -> ImageData:
    global complete1
    complete1= isComplete
@filterProperties1.changed.connect
def store_params():
    container_values = {i.label: i.value for i in filterProperties1._list}
    PARAMS['filer_1']=container_values
    savejson(PARAMS) 



@magicgui(
    auto_call=True,
    filter2={'choices':wid_options[1],'label':wid_labels[1],'name':wid_labels[1]},
    filter3={'choices':wid_options[2],'label':wid_labels[2],'name':wid_labels[2]},
    filter4={'choices':wid_options[3],'label':wid_labels[3],'name':wid_labels[3]},
    isComplete={"widget_type": "CheckBox", "value": False, "name": "complete"})
#give a specific value shown
def filterProperties2(filter2=wid_options[1][0],filter3=wid_options[2][0],filter4=wid_options[3][0],Exposure_Time='0',Light_source_intensity='0',Binning='0',isComplete: bool=False) -> ImageData:
    global complete2
    complete2 = isComplete

@filterProperties2.changed.connect
def store_params():
    container_values = {i.label: i.value for i in filterProperties2._list}
    PARAMS['filer_2']=container_values
    savejson(PARAMS) 

@magicgui(
    auto_call=True,
    filter2={'choices':wid_options[1],'label':wid_labels[1],'name':wid_labels[1]},
    filter3={'choices':wid_options[2],'label':wid_labels[2],'name':wid_labels[2]},
    filter4={'choices':wid_options[3],'label':wid_labels[3],'name':wid_labels[3]},
    isComplete={"widget_type": "CheckBox", "value": False, "name": "complete"})
#give a specific value shown
def filterProperties3(filter2=wid_options[1][0],filter3=wid_options[2][0],filter4=wid_options[3][0],Exposure_Time='0',Light_source_intensity='0',Binning='0',isComplete: bool=False) -> ImageData:
    global complete3
    complete3 = isComplete

@filterProperties3.changed.connect
def store_params():
    container_values = {i.label: i.value for i in filterProperties3._list}
    PARAMS['filer_3']=container_values
    savejson(PARAMS) 

@magicgui(
    filter2={'choices':wid_options[1],'label':wid_labels[1],'name':wid_labels[1]},
    filter3={'choices':wid_options[2],'label':wid_labels[2],'name':wid_labels[2]},
    filter4={'choices':wid_options[3],'label':wid_labels[3],'name':wid_labels[3]},
    isComplete={"widget_type": "CheckBox", "value": False, "name": "complete"})
#give a specific value shown
def filterProperties4(filter2=wid_options[1][0],filter3=wid_options[2][0],filter4=wid_options[3][0],Exposure_Time='0',Light_source_intensity='0',Binning='0',isComplete: bool=False) -> ImageData:
    global complete4
    complete4 = isComplete

@filterProperties4.changed.connect
def store_params():
    container_values = {i.label: i.value for i in filterProperties4._list}
    PARAMS['filer_4']=container_values
    savejson(PARAMS) 

@magicgui(
    filter2={'choices':wid_options[1],'label':wid_labels[1],'name':wid_labels[1]},
    filter3={'choices':wid_options[2],'label':wid_labels[2],'name':wid_labels[2]},
    filter4={'choices':wid_options[3],'label':wid_labels[3],'name':wid_labels[3]},
    isComplete={"widget_type": "CheckBox", "value": False, "name": "complete"})
#give a specific value shown
def filterProperties5(filter2=wid_options[1][0],filter3=wid_options[2][0],filter4=wid_options[3][0],Exposure_Time='0',Light_source_intensity='0',Binning='0',isComplete: bool=False) -> ImageData:
    global complete5
    complete5 = isComplete
@filterProperties5.changed.connect
def store_params():
    container_values = {i.label: i.value for i in filterProperties5._list}
    PARAMS['filer_5']=container_values
    savejson(PARAMS) 


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
    global fn_options
    fn_options= f
    numChannels=dim[2]

    container = Container(widgets=[create_widget(value=dim[i],name=list1[i],options={'max':2**20}) for i in range(len(list1))])    
    viewer.window.add_dock_widget(container,name='Image Dimensions')
    @container.changed.connect
    def update_dim():
        container_values = {i.label: i.value for i in container._list}
        PARAMS['image_dimension']=container_values
        savejson(PARAMS)
        try:
            global numChannels
            numChannels=PARAMS["image_dimension"][ "Number of channels (C): "]
        except:
            pass

    numChannels-=1
    filter1=filterProperties1
    dock_widget1 = viewer.window.add_dock_widget(filter1)
    @filterProperties1.changed.connect
    def complete_check(isComplete:bool):
        if complete1==True:
            viewer.window.remove_dock_widget(dock_widget1)
    if numChannels>0:
        numChannels-=1
        filter2=filterProperties2
        dock_widget2 = viewer.window.add_dock_widget(filter2)
        @filterProperties2.changed.connect
        def complete_check2(isComplete:bool):
            print(complete2)
            if complete2==True:
                viewer.window.remove_dock_widget(dock_widget2)
        if numChannels>0:
            numChannels-=1
            filter3=filterProperties3
            dock_widget3 = viewer.window.add_dock_widget(filter3)
            @filterProperties3.changed.connect
            def complete_check(isComplete:bool):
                if complete3==True:
                    viewer.window.remove_dock_widget(dock_widget3)
            if numChannels>0:
                numChannels-=1
                filter4=filterProperties4
                dock_widget4 = viewer.window.add_dock_widget(filter4)
                @filterProperties4.changed.connect
                def complete_check(isComplete:bool):
                    if complete4==True:
                        viewer.window.remove_dock_widget(dock_widget4)
                if numChannels>0:
                    numChannels-=1
                filter5=filterProperties4
                dock_widget5 = viewer.window.add_dock_widget(filter5)
                @filterProperties5.changed.connect
                def complete_check(isComplete:bool):
                    if complete5==True:
                        viewer.window.remove_dock_widget(dock_widget5)
        
    

        
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



viewer.window.add_dock_widget(fileSelection,name='File Selection')
 

fileSelection.Micro_Meta_App_json_file.changed.connect(update)


napari.run()