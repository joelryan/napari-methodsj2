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
from magicgui.widgets import Label, ComboBox, create_widget, Container
from superqt import sliders
import pickle
import json
from urllib.request import urlopen
import json
import cv2
from aicsimageio import AICSImage
from xml.etree import ElementTree as et
from urllib import request
import pprint



# July 7 2022 - napari accelerator showcase demo!





PARAMS = {}


def savejson(dic):
    with open('Output.json', 'w') as fp:
        json.dump(dic, fp)


def read_json(fn, target):
    with open(fn) as json_file:
        data = json.load(json_file)
        data_new = data['components']
        fn_options = []
        for sample in data_new:
            if sample.get('Schema_ID') == target:
                fn_options.append(sample['Name'])
            else:
                pass
    return fn_options


def read_json_stand_att(fn, target, attributes):
    with open(fn) as json_file:
        data = json.load(json_file)
        data_new = data['MicroscopeStand']
        fn_options = []
        if data_new.get('Schema_ID') == target:
            for attribute in attributes:
                fn_options.append(data_new[attribute])
        else:
            pass
    return fn_options


def read_json_components_att(fn, target, attributes):
    with open(fn) as json_file:
        data = json.load(json_file)
        data_new = data['components']
        fn_options = []
        for sample in data_new:
            if sample.get('Schema_ID') == target:
                for attribute in attributes:
                    fn_options.append(sample[attribute])
            else:
                pass
    return fn_options



def read_json_attributes(fn, userinput, attributes):
    with open(fn) as json_file:
        data = json.load(json_file)
        data_new = data['components']
        fn_options = []
        for sample in data_new:
            if sample.get('Name') == userinput:
                for attribute in attributes:
                    fn_options.append(sample[attribute])
            else:
                pass
    return fn_options








#path = '/Users/yuexu/Desktop/Napari/napari-ex/demo/abif_axiovert1_.json'

path=r'C:\Users\joelr\Desktop\MethodsJ2-main\abif_axiovert1_.json'

widget_info = ['Objective.json', "ExcitationFilter.json", "StandardDichroic.json", "EmissionFilter.json"]
widget_params = {}
for wid in widget_info:
    wid_name = wid[:-5]
    widget_params[wid_name] = read_json(path, wid)
wid_labels = list(widget_params.keys())
wid_options = list(widget_params.values())


@magicgui(
    auto_call=True,
    filter1={'choices': wid_options[0], 'label': wid_labels[0], 'name': wid_labels[0]},
    filter2={'choices': wid_options[1], 'label': wid_labels[1], 'name': wid_labels[1]},
    filter3={'choices': wid_options[2], 'label': wid_labels[2], 'name': wid_labels[2]},
    filter4={'choices': wid_options[3], 'label': wid_labels[3], 'name': wid_labels[3]},
    isComplete={"widget_type": "CheckBox", "value": False, "name": "complete"})
# give a specific value shown
def filterProperties1(filter1=wid_options[0][0], filter2=wid_options[1][0], filter3=wid_options[2][0],
                      filter4=wid_options[3][0], Exposure_Time_ms='0', Light_source_intensity='0', Binning='1x1',
                      Fluorophore='', isComplete: bool = False) -> ImageData:
    global complete1
    complete1 = isComplete


@filterProperties1.changed.connect
def store_params():
    container_values = {i.label: i.value for i in filterProperties1._list}
    PARAMS['filter_1'] = container_values
    savejson(PARAMS)


@magicgui(
    auto_call=True,
    filter2={'choices': wid_options[1], 'label': wid_labels[1], 'name': wid_labels[1]},
    filter3={'choices': wid_options[2], 'label': wid_labels[2], 'name': wid_labels[2]},
    filter4={'choices': wid_options[3], 'label': wid_labels[3], 'name': wid_labels[3]},
    isComplete={"widget_type": "CheckBox", "value": False, "name": "complete"})
# give a specific value shown
def filterProperties2(filter2=wid_options[1][0], filter3=wid_options[2][0], filter4=wid_options[3][0],
                      Exposure_Time_ms='0', Light_source_intensity='0', Binning='1x1', Fluorophore='',
                      isComplete: bool = False) -> ImageData:
    global complete2
    complete2 = isComplete


@filterProperties2.changed.connect
def store_params():
    container_values = {i.label: i.value for i in filterProperties2._list}
    PARAMS['filter_2'] = container_values
    savejson(PARAMS)


@magicgui(
    auto_call=True,
    filter2={'choices': wid_options[1], 'label': wid_labels[1], 'name': wid_labels[1]},
    filter3={'choices': wid_options[2], 'label': wid_labels[2], 'name': wid_labels[2]},
    filter4={'choices': wid_options[3], 'label': wid_labels[3], 'name': wid_labels[3]},
    isComplete={"widget_type": "CheckBox", "value": False, "name": "complete"})
# give a specific value shown
def filterProperties3(filter2=wid_options[1][0], filter3=wid_options[2][0], filter4=wid_options[3][0],
                      Exposure_Time_ms='0', Light_source_intensity='0', Binning='1x1', Fluorophore='',
                      isComplete: bool = False) -> ImageData:
    global complete3
    complete3 = isComplete


@filterProperties3.changed.connect
def store_params():
    container_values = {i.label: i.value for i in filterProperties3._list}
    PARAMS['filter_3'] = container_values
    savejson(PARAMS)


@magicgui(
    filter2={'choices': wid_options[1], 'label': wid_labels[1], 'name': wid_labels[1]},
    filter3={'choices': wid_options[2], 'label': wid_labels[2], 'name': wid_labels[2]},
    filter4={'choices': wid_options[3], 'label': wid_labels[3], 'name': wid_labels[3]},
    isComplete={"widget_type": "CheckBox", "value": False, "name": "complete"})
# give a specific value shown
def filterProperties4(filter2=wid_options[1][0], filter3=wid_options[2][0], filter4=wid_options[3][0],
                      Exposure_Time_ms='0', Light_source_intensity='0', Binning='1x1', Fluorophore='',
                      isComplete: bool = False) -> ImageData:
    global complete4
    complete4 = isComplete


@filterProperties4.changed.connect
def store_params():
    container_values = {i.label: i.value for i in filterProperties4._list}
    PARAMS['filter_4'] = container_values
    savejson(PARAMS)


@magicgui(
    filter2={'choices': wid_options[1], 'label': wid_labels[1], 'name': wid_labels[1]},
    filter3={'choices': wid_options[2], 'label': wid_labels[2], 'name': wid_labels[2]},
    filter4={'choices': wid_options[3], 'label': wid_labels[3], 'name': wid_labels[3]},
    isComplete={"widget_type": "CheckBox", "value": False, "name": "complete"})
# give a specific value shown
def filterProperties5(filter2=wid_options[1][0], filter3=wid_options[2][0], filter4=wid_options[3][0],
                      Exposure_Time_ms='0', Light_source_intensity='0', Binning='1x1', Fluorophore='',
                      isComplete: bool = False) -> ImageData:
    global complete5
    complete5 = isComplete


@filterProperties5.changed.connect
def store_params():
    container_values = {i.label: i.value for i in filterProperties5._list}
    PARAMS['filter_5'] = container_values
    savejson(PARAMS)


@magicgui(
    auto_call=True,
    Micro_Meta_App_json_file={'mode': 'r'},
    call_button='Run',
    layout='vertical'
)
# give a specific value shown
def fileSelection(Image: ImageData, Micro_Meta_App_json_file=pathlib.Path.home()) -> ImageData:
    try:
        fn_options = read_json(Micro_Meta_App_json_file)
    except:
        fn_options = None


def update(f: str):
    global fn_options
    fn_options = f
    numChannels = dim[2]

    container = Container(
        widgets=[create_widget(value=dim[i], name=list1[i], options={'max': 2 ** 20}) for i in range(len(list1))])
    viewer.window.add_dock_widget(container, name='Image Dimensions')

    @container.changed.connect
    def update_dim():
        container_values = {i.label: i.value for i in container._list}
        PARAMS['image_dimension'] = container_values
        savejson(PARAMS)
        try:
            global numChannels
            numChannels = PARAMS["image_dimension"]["Number of channels (C): "]
        except:
            pass

    numChannels -= 1
    filter1 = filterProperties1
    dock_widget1 = viewer.window.add_dock_widget(filter1, name="Filter 1")

    @filterProperties1.changed.connect
    def complete_check(isComplete: bool):
        if complete1 == True:
            viewer.window.remove_dock_widget(dock_widget1)

    if numChannels > 0:
        numChannels -= 1
        filter2 = filterProperties2
        dock_widget2 = viewer.window.add_dock_widget(filter2, name="Filter 2")

        @filterProperties2.changed.connect
        def complete_check2(isComplete: bool):
            print(complete2)
            if complete2 == True:
                viewer.window.remove_dock_widget(dock_widget2)

        if numChannels > 0:
            numChannels -= 1
            filter3 = filterProperties3
            dock_widget3 = viewer.window.add_dock_widget(filter3, name="Filter 3")

            @filterProperties3.changed.connect
            def complete_check(isComplete: bool):
                if complete3 == True:
                    viewer.window.remove_dock_widget(dock_widget3)

            if numChannels > 0:
                numChannels -= 1
                filter4 = filterProperties4
                dock_widget4 = viewer.window.add_dock_widget(filter4, name="Filter 4")

                @filterProperties4.changed.connect
                def complete_check(isComplete: bool):
                    if complete4 == True:
                        viewer.window.remove_dock_widget(dock_widget4)

                if numChannels > 0:
                    numChannels -= 1
                filter5 = filterProperties4
                dock_widget5 = viewer.window.add_dock_widget(filter5, name="Filter 5")

                @filterProperties5.changed.connect
                def complete_check(isComplete: bool):
                    if complete5 == True:
                        viewer.window.remove_dock_widget(dock_widget5)


#######################Microscope descriptor
@magicgui(
    call_button='confirm',
    Microscope_descriptor={
        'choices': ['None', 'Camera (widefield, TIRF, spinning disk)', 'PMT (confocal, multiphoton)']})
# give a specific value shown
def microscopeProperties(Microscope_descriptor='None') -> ImageData:
    pass


@microscopeProperties.changed.connect
def store_params(event):
    widget = event.value
    PARAMS[widget.name] = {
        n: p.default for n, p in widget.__signature__.parameters.items()
    }
    if PARAMS[widget.name]['Microscope_descriptor'] == 'Camera (widefield, TIRF, spinning disk)':
        if len(scanningProperties) >= 1:
            # viewer.window.remove_dock_widget(scanningProperties)
            scanningProperties.pop(0).native.close()
            viewer.window.add_dock_widget(channelProperties, name='Channel Properties')
        else:
            viewer.window.add_dock_widget(channelProperties, name='Channel Properties')

    if PARAMS[widget.name]['Microscope_descriptor'] == 'PMT (confocal, multiphoton)':
        if len(channelProperties) >= 1:
            channelProperties.pop(0).native.close()
            viewer.window.add_dock_widget(scanningProperties, name='Scanning Properties')
        else:
            viewer.window.add_dock_widget(scanningProperties, name='Scanning Properties')

    savejson(PARAMS)


@magicgui(
    call_button='confirm',
    exposureTime={'label': 'Exposure time'},
    lightSource={'label': "Light source intensity"},
    Binning={'choices': ['1x1', '2x2', '4x4']},
    layout='vertical')
# give a specific value shown
def channelProperties(exposureTime: float = None, lightSource: float = None, Binning='1x1') -> ImageData:
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
    Dwell_Time={'label': 'Dwell Time'},
    averaging={'label': "Averaging"},
    gain={'label': "Gain"},
    pinhole={'label': "Pinhole"},
    layout='vertical')
# give a specific value shown
def scanningProperties(Dwell_Time: float = 1, averaging: float = 1, gain: float = 800, pinhole: float = 1) -> ImageData:
    pass


@scanningProperties.changed.connect
def store_params(event):
    widget = event.value
    PARAMS[widget.name] = {
        n: p.default for n, p in widget.__signature__.parameters.items()
    }
    savejson(PARAMS)


viewer = napari.Viewer()
dim = [512, 512, 1, 1, 1]
list1 = ['Image width in pixels (X): ', 'Image height in pixels (Y): ', 'Number of channels (C): ',
         'Number of slices (Z): ', 'Number of frames (T): ']


@viewer.layers.events.inserted.connect
def _on_insert(event):
    img_path = viewer.layers[0].source.path
    im = AICSImage(img_path)
    meta_dim = list(im.dims['X', 'Y', 'C', 'Z', 'T'])
    pixel_sizes = list(im.physical_pixel_sizes)
    for i in range(len(dim)):
        dim[i] = meta_dim[i]
    PARAMS['image_dimension'] = dim
    PARAMS['pixel_size_x'] = pixel_sizes[2]
    PARAMS['pixel_size_y'] = pixel_sizes[1]


viewer.window.add_dock_widget(fileSelection, name='File Selection')

fileSelection.Micro_Meta_App_json_file.changed.connect(update)

napari.run()





########################################
########################################
########################################
########################################
########################################






with open(path) as json_file:
    data = json.load(json_file)

components = data['components']

for i in range(0, len(components)):


    if components[i].get('DIC') == True:
        components[i]['DIC'] = 'DIC'
    if components[i].get('DIC') == False:
        components[i]['DIC'] = ''
    if components[i].get('CorrectionCollar', '') == True:
        components[i]['CorrectionCollar'] = "(with a correction collar for " + components[i].get(
            'CorrectionCollarType', '') + ")"
    if components[i].get('CorrectionCollar', '') == False:
        components[i]['CorrectionCollar'] = ''
    if components[i].get('ContrastModulation') == "None":
        components[i]['ContrastModulation'] = ''




def read_json_components_att_2(json_dict, target, attributes):

    data_new = json_dict
    fn_options = []
    for sample in data_new:
        if sample.get('Schema_ID') == target:
            for attribute in attributes:
                fn_options.append(sample[attribute])
        else:
            pass
    return fn_options



def read_json_attributes_2(json_dict, userinput, attributes):
    data_new = json_dict
    fn_options = []
    for sample in data_new:
        if sample.get('Name') == userinput:
            for attribute in attributes:
                fn_options.append(sample[attribute])
        else:
            pass
    return fn_options







blurb = ""
#basic_text = "images were acquired with a " + obj + " objective."
#print(basic_text)

#print(read_json(path, "AcquisitionSoftware.json"))

# stand

#read_json_stand_att(fn, target, attributes)

obj_att = read_json_stand_att(path, "InvertedMicroscopeStand.json", [
                "Model",
                "Type",
                "Origin",
                "Manufacturer"
            ])

blurb += "Images were acquired on a %s %s %s inverted microscope (%s)" % tuple(obj_att)



obj_att = read_json_components_att_2(components, "AcquisitionSoftware.json", [
                "Name",
                "Version",
                "Developer"
            ])

blurb += " controlled with %s software (%s, %s)," % tuple(obj_att)



obj = (PARAMS['filter_1'].get('Objective'))

obj_att = read_json_attributes_2(components, obj, [
                "Magnification",
                "LensNA",
                "Correction",
                "ContrastModulation",
                "DIC",
                "ImmersionType",
                "CorrectionCollar",
                "Manufacturer"
            ])

blurb += " equipped with a %sx NA %s %s %s %s %s objective %s (%s)." % tuple(obj_att)

blurb += "\n"

dim_x = (PARAMS['image_dimension'].get("Image width in pixels (X): "))
blurb +=  " Images had a width of %s" % dim_x


dim_y = (PARAMS['image_dimension'].get("Image height in pixels (Y): "))
blurb += " and a height of %s pixels," % (dim_y)

dim_c = (PARAMS['image_dimension'].get("Number of channels (C): "))
blurb += " %s channels," % (dim_c)

dim_z = (PARAMS['image_dimension'].get("Number of slices (Z): "))
blurb += " %s planes (z)," % (dim_z)

dim_t = (PARAMS['image_dimension'].get("Number of frames (T): "))
blurb += " %s timepoints." % (dim_t)


pixel_size_x = PARAMS.get('pixel_size_x')
blurb += " Voxels had a lateral size of %.3f um." % (pixel_size_x)




# ch1

#channels = ['filter_1', 'filter_2', 'filter_3']

#for channel in channels:

blurb += "\n"

fluoro = (PARAMS['filter_1'].get('Fluorophore'))
blurb += "%s was excited with " % (fluoro)


light_source = read_json_components_att(path, "Fluorescence_LightSource_LightEmittingDiode.json",  [
                "Model",
                "Manufacturer"
            ])

blurb += " a %s light source (%s)" % tuple(light_source)


light_source_int = (PARAMS['filter_1'].get("Light source intensity"))

blurb += " set to %s percent" % (light_source_int)



exFilt = (PARAMS['filter_1'].get('ExcitationFilter'))

exFilt_att = read_json_attributes(path, exFilt, [
                "Model",
                "Manufacturer"
            ])

blurb += " and wavelength selection was carried out with a %s excitation filter (%s), " % tuple(exFilt_att)



beamsplit = (PARAMS['filter_1'].get('StandardDichroic'))
beamsplit_att = read_json_attributes(path, beamsplit, [
                "Model",
                "Manufacturer"
            ])

blurb +=  "a %s dichroic mirror (%s) " % tuple(beamsplit_att)

emFilt = (PARAMS['filter_1'].get('EmissionFilter'))
emFilt_att = read_json_attributes(path, emFilt, [
                "Model",
                "Manufacturer"
            ])

blurb += " and a %s emission filter (%s). " % tuple(emFilt_att)


detector = read_json_components_att(path, "CCD.json",  [
                "Model",
                "Schema_ID",
                "Manufacturer"
            ])
blurb += "Images were acquired on a %s %s (%s)" % tuple(detector)


exposureTime = (PARAMS['filter_1'].get('Exposure Time ms'))
blurb += " with an exposure time of %s ms" % (exposureTime)


binning = (PARAMS['filter_1'].get('Binning'))

blurb += " and %s binning." % (binning)



######## ch2

blurb += "\n"
fluoro = (PARAMS['filter_2'].get('Fluorophore'))
blurb += "%s was excited with " % (fluoro)


light_source = read_json_components_att(path, "Fluorescence_LightSource_LightEmittingDiode.json",  [
                "Model",
                "Manufacturer"
            ])

blurb += " a %s light source (%s)" % tuple(light_source)


light_source_int = (PARAMS['filter_2'].get("Light source intensity"))

blurb += " set to %s percent" % (light_source_int)



exFilt = (PARAMS['filter_2'].get('ExcitationFilter'))

exFilt_att = read_json_attributes(path, exFilt, [
                "Model",
                "Manufacturer"
            ])

blurb += " and wavelength selection was carried out with a %s excitation filter (%s), " % tuple(exFilt_att)



beamsplit = (PARAMS['filter_2'].get('StandardDichroic'))
beamsplit_att = read_json_attributes(path, beamsplit, [
                "Model",
                "Manufacturer"
            ])

blurb +=  "a %s dichroic mirror (%s) " % tuple(beamsplit_att)

emFilt = (PARAMS['filter_2'].get('EmissionFilter'))
emFilt_att = read_json_attributes(path, emFilt, [
                "Model",
                "Manufacturer"
            ])

blurb += "and a %s emission filter (%s). " % tuple(emFilt_att)




detector = read_json_components_att(path, "CCD.json",  [
                "Model",
                "Schema_ID",
                "Manufacturer"
            ])
blurb += "Images were acquired on a %s %s (%s)" % tuple(detector)


exposureTime = (PARAMS['filter_2'].get('Exposure Time ms'))
blurb += " with an exposure time of %s ms" % (exposureTime)


binning = (PARAMS['filter_2'].get('Binning'))

blurb += " and %s binning." % (binning)



######## ch3

blurb += "\n"
fluoro = (PARAMS['filter_3'].get('Fluorophore'))
blurb += "%s was excited with " % (fluoro)


light_source = read_json_components_att(path, "Fluorescence_LightSource_LightEmittingDiode.json",  [
                "Model",
                "Manufacturer"
            ])

blurb += " a %s light source (%s)" % tuple(light_source)


light_source_int = (PARAMS['filter_3'].get("Light source intensity"))

blurb += " set to %s percent" % (light_source_int)


exFilt = (PARAMS['filter_3'].get('ExcitationFilter'))

exFilt_att = read_json_attributes(path, exFilt, [
                "Model",
                "Manufacturer"
            ])

blurb += " and wavelength selection was carried out with a %s excitation filter (%s), " % tuple(exFilt_att)



beamsplit = (PARAMS['filter_3'].get('StandardDichroic'))
beamsplit_att = read_json_attributes(path, beamsplit, [
                "Model",
                "Manufacturer"
            ])

blurb +=  "a %s dichroic mirror (%s) " % tuple(beamsplit_att)

emFilt = (PARAMS['filter_3'].get('EmissionFilter'))
emFilt_att = read_json_attributes(path, emFilt, [
                "Model",
                "Manufacturer"
            ])

blurb += "and a %s emission filter (%s). " % tuple(emFilt_att)




detector = read_json_components_att(path, "CCD.json",  [
                "Model",
                "Schema_ID",
                "Manufacturer"
            ])
blurb += "Images were acquired on a %s %s (%s)" % tuple(detector)


exposureTime = (PARAMS['filter_3'].get('Exposure Time ms'))
blurb += " with an exposure time of %s ms" % (exposureTime)


binning = (PARAMS['filter_3'].get('Binning'))

blurb += " and %s binning." % (binning)





def textCleanUp(string):
	string = string.replace('CCD.json', 'CCD camera')
	string = string.replace('CMOS.json', 'sCMOS camera')
	string = string.replace('IntensifiedCamera.json', 'intensified CCD camera')
	string = string.replace('gain set to and', '')
	string = string.replace(', with the assistance of . (', '. (')
	string = string.replace('(RRID: ).', '')
	string = string.replace('.json', '')
	string = string.replace('wide field', 'widefield')
	string = string.replace('Mineral Oil', 'oil')
	string = string.replace('  ', ' ')
	string = string.replace('  ', ' ')
	string = string.replace('..', '.')
	string = string.replace('The time interval between frames was n/a s','')


	return (string)


#pp = pprint.PrettyPrinter(width = 80)
print("\n")

print(textCleanUp(blurb))

with open("output_methods_text.txt", "w") as text_file:
    text_file.write(textCleanUp(blurb))


#pp.pprint(textCleanUp(blurb))







################ settings dict #######################
#
#
# settings_dict = {
#     "settings": [
#         {
#
#             "Information": "MicroscopeStand",
#             "Schema_ID": "InvertedMicroscopeStand.json",
#             "attributes": [
#                 "Model",
#                 "Type",
#                 "Origin",
#                 "Manufacturer"
#             ],
#             "blurb": "Images were acquired on a %s %s %s inverted microscope (%s) "
#         },
#         {
#             "Dialog_Box": "Microscope description",
#             "Schema_ID": "AcquisitionSoftware.json",
#             "attributes": [
#                 "Name",
#                 "Version",
#                 "Developer"
#             ],
#             "blurb": "controlled with %s software (%s, %s),"
#         },
#         {
#             "Dialog_Type": "addChoice",
#             "category": "core",
#             "Dialog_Box": "Objective",
#             "Setting": "Select objective: ",
#             "Add_to_same_row": 0,
#             "CheckHardwareJSON": 1,
#             "Schema_ID": "Objective.json",
#             "attributes": [
#                 "Magnification",
#                 "LensNA",
#                 "Correction",
#                 "ContrastModulation",
#                 "DIC",
#                 "ImmersionType",
#                 "CorrectionCollar",
#                 "Manufacturer"
#             ],
#             "metadata value": "",
#             "blurb": "equipped with a %sx NA %s %s %s %s %s objective %s (%s)."
#         },
#         {
#             "Dialog_Box": "Image dimensions",
#
#             "Setting": "Image width in pixels (X): ",
#
#             "metadata key": "getPixelsSizeX",
#             "metadata value": "",
#             "blurb": "Images had a width of %s"
#         },
#         {
#             "Dialog_Box": "Image dimensions",
#             "Setting": "Image height in pixels (Y): ",
#             "metadata key": "getPixelsSizeY",
#             "metadata value": "",
#             "blurb": "and a height of %s pixels,"
#         },
#         {
#             "Dialog_Box": "Image dimensions",
#             "Setting": "Number of slices (Z): ",
#             "conditional_value": "",
#             "metadata key": "getPixelsSizeZ",
#             "metadata value": "",
#             "blurb": "%s planes (z),"
#         },
#         {
#             "Dialog_Box": "Image dimensions",
#             "Setting": "Number of channels (C): ",
#             "metadata key": "getPixelsSizeC",
#             "metadata value": "",
#             "blurb": "%s channels,"
#         },
#         {
#             "Dialog_Box": "Image dimensions",
#             "Setting": "Number of frames (T): ",
#             "conditional_value": "",
#             "metadata key": "getPixelsSizeT",
#             "metadata value": "",
#             "blurb": "%s timepoints,"
#         },
#         {
#             "Dialog_Box": "Image dimensions",
#             "Setting": "Dimension order: ",
#             "metadata key": "getPixelsDimensionOrder",
#             "metadata value": "",
#             "blurb": "with dimensional order %s."
#         },
#         {
#             "Dialog_Box": "Image dimensions",
#             "Setting": "Pixel size XY (micron): ",
#             "metadata key": "getPixelsPhysicalSizeX",
#             "metadata value": "",
#             "blurb": "Voxels had a lateral size of %s um"
#         },
#         {
#             "Dialog_Box": "Image dimensions",
#
#             "Setting": "Voxel size Z (micron): ",
#             "conditional_setting": "Number of slices (Z): ",
#             "metadata key": "getPixelsPhysicalSizeZ",
#             "metadata value": "",
#             "blurb": "and a depth of %s um."
#         },
#         {
#             "Dialog_Box": "Image dimensions",
#             "category": "core",
#             "Setting": "Time interval: ",
#             "Add_to_same_row": 0,
#             "Dialog_Type": "addStringField",
#             "conditional_setting": "Number of frames (T): ",
#             "conditional_value": "True",
#             "metadata key": "frameInterval",
#             "metadata value": "",
#             "blurb": "The time interval between frames was %s s."
#         },]
# }
#
#

#print(settings_dict["settings"][1]["Schema_ID"])


#print("===========================================")

