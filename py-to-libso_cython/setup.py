from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
    #                           .so name, [.pyx files,.pyx files]
    ext_modules = [Extension("helloworld", ["HWorld.pyx"])]

    )
