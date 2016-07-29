ext = Extension(
    "Subscriber",                 # name of extension
    ["Subscriber.pyx", "Subscriber.cpp"],     # filename of our Cython source. Pyx has the declarations of the h(pp) for the cpp
    language="c++",              # this causes Cython to create C++ source
    #include_dirs=[...],          # usual stuff
    libraries="stdc++",             # libraries=["stdc++", ...], Could use stdc++11,14, etc
    #extra_link_args=[...],       # if needed
    cmdclass = {'build_ext': build_ext}
    )
