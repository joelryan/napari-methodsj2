#ninstruments = m.getInstrumentCount()
# im_X = m.getPixelsSizeX(0)
# 	dim_Y = m.getPixelsSizeY(0)
# 	dim_C = int(str(m.getPixelsSizeC(0)))  ### java-element thing? -> to integer...
# 	dim_Z = m.getPixelsSizeZ(0)
# 	dim_T = m.getPixelsSizeT(0)
# 	dim_order = m.getPixelsDimensionOrder(0)

#pxx_microns = "{:.2f}".format(m.getPixelsPhysicalSizeX(0).value(UNITS.MICROMETER))

'''
#Bioformats
import javabridge
import bioformats
javabridge.start_vm(class_path=bioformats.JARS)
'''
from aicsimageio import AICSImage

tif_path='/Users/yuexu/Desktop/Napari/napari-ex/demo/demo_image_phalloidin.tif'
czi_path='/Users/yuexu/Desktop/Napari/MethodsJ2-main/BPAE_3color_30p-200ms_63xOil_003_diffExp_Int__.czi'
img = AICSImage(czi_path)
def read_image(img):
    img_data={}
    img_data['npArray']=img.data  # returns 5D TCZYX numpy array
    img_data['xArray']=img.xarray_data  # returns 5D TCZYX xarray data array backed by numpy
    img_data['dim']=img.dims  # returns a Dimensions object
    img_data['dimNum']=img.dims.order  # returns string "TCZYX"
    img_data['Xdim']=img.dims.X  # returns size of X dimension
    img_data['shape']=img.shape  # returns tuple of dimension sizes in TCZYX order
    img_data['CZYX']=img.get_image_data("CZYX", T=0)  # returns 4D CZYX numpy array
    return img_data

# print(read_image(img))

# print(img.physical_pixel_sizes)
# img.metadata  # returns the metadata object for this file format (XML, JSON, etc.)
data=img.metadata
print(data)
print(data[0].get('ScalingComponent', default=None))
for child in data[0][2]:
    print(child.tag, child.attrib)
# print([elem.tag for elem in data[0].iter()])
# print(data[0].attrib['RunMode'])

# print([elem.attrib for elem in data[0].iter()])
# print(data.getroot())
# img.channel_names  # returns a list of string channel names found in the metadata
# img.physical_pixel_sizes.Z  # returns the Z dimension pixel size as found in the metadata
# img.physical_pixel_sizes.Y  # returns the Y dimension pixel size as found in the metadata
# img.physical_pixel_sizes.X  # returns the X dimension pixel size as found in the metadata

# import javabridge
# import bioformats
# javabridge.start_vm(class_path=bioformats.JARS)