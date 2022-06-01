

A Napari plugin script of imageJ2 adaptation to Napari

----------------------------------

This is the repository for Napari-methodsJ2, an integration of the original ImageJ2 software and Napari software for multidimensional image data, with a focus on scientific imaging. Its central goal is enable users to access it through Napari software and to broaden the use of ImageJ2.

Napari-ImageJ2 will keep most function of imageJ2 to helps users write a materials and methods text for microscopy experiments by sourcing experiment information from metadata, as well as information from a microscope hardware configuration file generated in Micro-Meta App.  It integrates the image processing logic with graphical user interface (UI), users could modify pictures and enter information at the same time.

The original imageJ2 written in Python2. The plugin code is written in Python 3 for convenience of future maintenance and upgrade, and the Napari-methodsJ2 was developed as an napari version of ImageJ2. To learn about ImageJ2, read the [**paper**](https://www.biorxiv.org/content/10.1101/2021.06.23.449674v1).


## Installation

Install an [Anaconda](https://www.anaconda.com/download/) distribution of Python -- Choose **Python 3** and your operating system. Note you might need to use an anaconda prompt if you did not add anaconda to the path.

Install `napari` with pip: `pip install napari[all]`. Then run `demo.py` by via:

    python3 demo.py

 Or run the script file in python environment.



## Running the software

The Napari software will automatically open when running the script.

The script displays dialog boxes wherein users can directly input information as text, or select the appropriate options from a drop-down menu assembled from the microscopy hardware specifications file generated in Micro-Meta App. User input and selections are then used to "fill in the blanks" in blocks of text designed to generate a draft of a experimental methods section.
To begin with, the users would be asked to select the micro meta json file:

![Welcome page](https://github.com/joelryan/napari-methodsj2/blob/main/demo0.png)

After selecting a json file, information would be automatically read and corresponding widgets would show:

![Demo Widgets](https://github.com/joelryan/napari-methodsj2/blob/main/demo2.png)

![Montage_BPAE__8bit_Montage](https://user-images.githubusercontent.com/64212264/120518327-77ad6200-c39f-11eb-9a6c-5a49c5aca810.png)
> Demo image (BPAE_3color_30p-200ms_63xOil_003_diffExp_Int__.czi).

There is sample data in the File menu, or get started with your own images!

For the demo image and [Micro-Meta App](https://github.com/WU-BIMAC/MicroMetaApp-Electron/releases/tag/1.2.2-b1-1) hardware specifications file displayed above, the output of Napari-MethodsJ2 should look like this:
```

The selected image has a width of 519.0 pixels, a height of 528.0 pixels, 10.0 channel(s), 6.0 slice(s), and 7.0 frame(s)The excitation and emission filter were BP 450-490 - GFP excitation filter and BP 445/50 - DAPI emission filter and the exposure time was 8.0.
```

## Contributing

Contributions are very welcome. Tests are run with pytest.

## License

Distributed under the terms of the [BSD-3] license,
"Napari-methodsJ2" is free and open source software.

## Dependencies
Napari-methodsJ2 relies on the following excellent packages (which are automatically installed with conda/pip if missing):
- [napari](https://napari.org)
- [magicgui](https://napari.org/magicgui/)

This [napari] plugin would be packaged generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
