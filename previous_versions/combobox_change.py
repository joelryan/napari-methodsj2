from napari.types import ImageData
from magicgui import magicgui
from skimage import filters, morphology
import numpy as np
import napari


# option set defines the possible options, the key gives the option list of first combobox, 
# and elements of option_set[key] defines following suboptions when the option is selected in first combobox, and is shown in the second combobox
option_set={'None':['None'],
'option a':['suboption a1','suboption a2','suboption a3'],
'option b':['suboption b1','suboption b2','suboption b3'],
'option c':['suboption c1','suboption c2','suboption c3']}

#We have several options. (1) show widget 1 and 2, and set both default values to 'None', change the options of widget 2 if widget 1 is selected(we are using it now)
#(2) only show widget 2 when a valid option is selected from widget 2 (we also can do it)
#the widget name is defined as filter_widget, and it can be changed to any other names(as long as we replace all filter widget)
@magicgui(
    auto_call=True,
    first_option={
        'choices': list(option_set.keys()),
        'label': 'Filter Choice:',
    },
    second_option={'choices': ['None'], 'label': 'Next Choice'},
)
def filter_widget(
    image: ImageData, first_option='None', second_option='None'
) -> ImageData:
    return

# note, we now use the name `filter_widget` to refer to the widget itself
# and subwidgets are available at `widget.sub_widget`
# no change if the first selection is still "None", which is default value
# otherwise, a series of options will be given in second widget, according to option_set
@filter_widget.first_option.changed.connect
def change_label(event):
    options_selected=event.value
    if event.value != 'None':
        filter_widget.second_option.choices = option_set[options_selected]
    
viewer = napari.Viewer()
viewer.window.add_dock_widget(filter_widget)
napari.run()