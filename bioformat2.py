import javabridge as jv
import bioformats as bf
from xml.etree import ElementTree as et
import json
import xmltodict

jv.start_vm(class_path=bf.JARS, max_heap_size='8G')
