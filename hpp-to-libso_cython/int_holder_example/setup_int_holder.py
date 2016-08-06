from distutils.core import setup, Extension
from Cython.Distutils import build_ext
import pkg_resources

data_dir = pkg_resources.resource_filename("autowrap", "data_files") # needed by autowrap

ext =  Extension(
    "py_int_holder",                 # name of extension -> In python code: import <name>
    ["py_int_holder.cpp"],     # filename of our Cython source. Pyx has the declarations of the h(pp) for the cpp
    language="c++",              # this causes Cython to create C++ source
    include_dirs=[data_dir],          # usual stuff
    #libraries="stdc++",             # libraries=["stdc++", ...], Could use stdc++11,14, etc
    #extra_link_args=[...],       # if needed
    )

setup(
    name = 'Py Int Holder Example',
    version = '0.1',
    cmdclass = {'build_ext': build_ext},
    ext_modules = [ext]
)
