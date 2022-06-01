
import napari
from napari.types import ImageData
from magicgui import magicgui
import pathlib
from magicgui.widgets import ComboBox
import json



#save user input
def savejson(dic):
    with open('data.json', 'w') as fp:
        json.dump(dic, fp)
#read hardware json file
def read_json(fn,target):
    with open(fn) as json_file:
        data = json.load(json_file)
        data_new = data['components']
        global fn_options
        fn_options=[]
        for sample in data_new:
            if sample.get('Schema_ID')== target:
                fn_options.append(sample['Name'])
            else:
                pass
    return fn_options


# load parameters
PARAMS={}
path='/Users/yuexu/Desktop/Napari/napari-ex/demo/abif_axiovert1_.json'
img_dim_widget_info=['Objective.json',"ExcitationFilter.json","StandardDichroic.json","EmissionFilter.json"]
widget_params={}
for wid in img_dim_widget_info:
    wid_name=wid[:-5]
    widget_params[wid_name]= read_json(path,wid)
img_dim=['Image width in pixels (X): ', 'Image height in pixels (Y): ', 'Number of slices (Z): ', 'Number of channels (C): ', 'Number of frames (T): ']




@magicgui(
    auto_call=True,
    Micro_Meta_App_json_file={'mode': 'r'},
    call_button='Run',
    layout='vertical'
)

#select micro meta app json file
def fileSelection(Image: ImageData,  Micro_Meta_App_json_file =  pathlib.Path.home()) -> ImageData:
    try:
        global fn_options
    except:
        fn_options=None

#schema_id matching,show widgets once path given
def update(f: str):
    if fn_options != None:
        viewer.window.add_dock_widget(image_dimensions,name='Image Dimensions')
        for i in range(len(widget_params)):
            wid_labels=list(widget_params.keys())[i]
            wid_choices=widget_params[wid_labels]
            wid_name=wid_labels
            image_dimensions.insert(i+6,ComboBox(name=wid_name,label=wid_labels,choices=wid_choices))
        viewer.window.add_dock_widget(channelProperties,name='Channel Properties')


@magicgui(
    o1={'label':str(img_dim[0])},
    o2={'label':str(img_dim[1])},
    o3={'label':str(img_dim[2])},
    o4={'label':str(img_dim[3])},
    o5={'label':str(img_dim[4])},
    layout='vertical'
)
def image_dimensions(o1:float = 512,o2:float = 512,o3:float = 1,o4:float = 1,o5:float = 1) -> ImageData:
    pass


@image_dimensions.changed.connect
def store_params(event):
    widget = event.value
    PARAMS[widget.name] = {
        n: p.default for n, p in widget.__signature__.parameters.items()
    }
    savejson(PARAMS)

@magicgui(
    call_button='confirm',
    exposureTime={'label':'Exposure time'},
    lightSource={'label':"Light source intensity"},
    Binning={'choices':['1x1', '2x2', '4x4']},
    layout='vertical'
)
def channelProperties(exposureTime:float = None,lightSource:float = None,Binning='1x1') -> ImageData:
    pass

@channelProperties.changed.connect
def store_params(event):
    widget = event.value
    PARAMS[widget.name] = {
        n: p.default for n, p in widget.__signature__.parameters.items()
    }
    savejson(PARAMS)



viewer = napari.Viewer()
viewer.window.add_dock_widget(fileSelection,name='File Selection')
fileSelection.Micro_Meta_App_json_file.changed.connect(update)
napari.run()