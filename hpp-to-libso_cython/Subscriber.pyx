# no namespace on Subscriber.hpp, so no namespace in cdef block
cdef extern from "Subscriber.hpp" 
    cdef cppclass Subscriber:
        #private


        #public
