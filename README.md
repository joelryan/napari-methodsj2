# cellpose-napari <img src="docs/_static/favicon.ico" width="50" title="cellpose" alt="cellpose" align="right" vspace = "50">


a napari plugin script of imageJ2 adaptation to Napari

----------------------------------

This is the repository for Napari-ImageJ2, a integration of the original ImageJ and Napari software for multidimensional image data, with a focus on scientific imaging. Its central goal is to broaden the paradigm of ImageJ beyond the limitations of the original ImageJ application, to support a wider range of multidimensional scientific image data.???

To ensure backwards compatibility, ImageJ2 has been designed to fully integrate into the original ImageJ user interface. This allows users to keep using ImageJ in familiar ways, while providing the ability to migrate toward more powerful new features as needed.0

Under the hood, ImageJ2 completely isolates the image processing logic from the graphical user interface (UI), allowing ImageJ2 commands to be used in many contexts, including headless in the cloud or on a server such as OMERO, from within another Java application such as KNIME or Icy, or even from Python-based applications such as CellProfiler and napari via PyImageJ.


The plugin code was written in Python 3, and the ImageJ2-Napari was developed as an napari version of ImageJ2. To learn about ImageJ2, read the [**paper**](https://www.biorxiv.org/content/10.1101/2021.06.23.449674v1).


## Installation

Install an [Anaconda](https://www.anaconda.com/download/) distribution of Python -- Choose **Python 3** and your operating system. Note you might need to use an anaconda prompt if you did not add anaconda to the path.

Install `napari` with pip: `pip install napari[all]`. Then run `xxxxx` by via:

    python3 deme.py
    
 Or run the script file in python environment.

<!-- If install fails in your base environment, create a new environment:
1. Download the [`environment.yml`](https://github.com/MouseLand/cellpose-napari/blob/master/environment.yml?raw=true) file from the repository. You can do this by cloning the repository, or copy-pasting the text from the file into a text document on your local computer.
2. Open an anaconda prompt / command prompt with `conda` for **python 3** in the path
3. Change directories to where the `environment.yml` is and run `conda env create -f environment.yml`
4. To activate this new environment, run `conda activate cellpose-napari`
5. You should see `(cellpose-napari)` on the left side of the terminal line. 

If you have **issues** with pcellpose installation, see the [cellpose docs](https://cellpose.readthedocs.io/en/latest/installation.html) for more details, and then if the suggestions fail, open an issue. -->
<!-- 
### Upgrading software

You can upgrade the plugin with
~~~
pip install cellpose-napari --upgrade
~~~

and you can upgrade cellpose with
~~~
pip install cellpose --upgrade
~~~

### GPU version (CUDA) on Windows or Linux

If you plan on running many images, you may want to install a GPU version of *torch* (if it isn't already installed).

Before installing the GPU version, remove the CPU version:
~~~
pip uninstall torch
~~~

Follow the instructions [here](https://pytorch.org/get-started/locally/) to determine what version to install. The Anaconda install is recommended along with CUDA version 10.2. For instance this command will install the 10.2 version on Linux and Windows (note the `torchvision` and `torchaudio` commands are removed because cellpose doesn't require them):

~~~
conda install pytorch cudatoolkit=10.2 -c pytorch
~~~~

When upgrading GPU Cellpose in the future, you will want to ignore dependencies (to ensure that the pip version of torch does not install):
~~~
pip install --no-deps cellpose --upgrade
~~~

### Installation of github version -->
<!-- 
Follow steps from above to install the dependencies. In the github repository, run `pip install -e .` and the github version will be installed. If you want to go back to the pip version of cellpose-napari, then say `pip install cellpose-napari`. -->


## Running the software


Open napari with the ImageJ2-napari dock widget open
```
napari -w cellpose-napari
```

There is sample data in the File menu, or get started with your own images!

### Detailed usage [documentation](https://cellpose-napari.readthedocs.io/).

## Contributing

Contributions are very welcome. Tests are run with pytest.

## License

Distributed under the terms of the [BSD-3] license,
"cellpose-napari" is free and open source software.

## Dependencies
cellpose-napari relies on the following excellent packages (which are automatically installed with conda/pip if missing):
- [napari](https://napari.org)
- [magicgui](https://napari.org/magicgui/)

cellpose relies on the following excellent packages (which are automatically installed with conda/pip if missing):
- [torch](https://pytorch.org/)
- [numpy](http://www.numpy.org/) (>=1.16.0)
- [numba](http://numba.pydata.org/numba-doc/latest/user/5minguide.html)
- [scipy](https://www.scipy.org/)
- [natsort](https://natsort.readthedocs.io/en/master/)
- [tifffile](https://pypi.org/project/tifffile/)
- [opencv](https://opencv.org/)

This [napari] plugin would be packaged generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
