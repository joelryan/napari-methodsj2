

import javabridge as jv
import bioformats as bf
from xml.etree import ElementTree as et
import json
import xmltodict



jv.start_vm(class_path=bf.JARS, max_heap_size='8G')


### path to change

md = bf.get_omexml_metadata(r'C:\Users\joelr\Documents\GitHubRepositories\BPAE_3color_30p-200ms_63xOil_003_diffExp_Int__.czi')
print(md)

mdroot = et.fromstring(md.encode('utf-8'))

print('_____md.encode(utf-8)')

blah = str(md.encode('utf-8'))




for a in mdroot[2]:
    print(a.tag)
    print(a.attrib)

    #if a.tag.endswith('Microscope'):
     #   print(a.attrib)

lens_na = None

for i in mdroot[1]:
    lens_na = None
    if i.tag.endswith('Objective'):
        lens_na = i.attrib['LensNA']

    print(lens_na)



print('blah')

print(mdroot[2].tag)
print(mdroot[2].attrib)


print('mdroot 0')
for a in mdroot[0]:
    print(a.tag)
    print(a.attrib)

print('mdroot 1')
for a in mdroot[1]:
    print(a.tag)
    print(a.attrib)

print('mdroot 2')
for a in mdroot[2]:
    print(a)
    print(a.tag)
    print(a.attrib)
    if str(a.tag).endswith('Pixels'):
        print(a.attrib['DimensionOrder'])

# print('mdroot 3')
# for a in mdroot[3]:
#     print(a.tag)
#     print(a.attrib)
print(mdroot[2][5].attrib['PhysicalSizeX'])




