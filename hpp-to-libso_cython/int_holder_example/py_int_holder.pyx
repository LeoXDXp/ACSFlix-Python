#cython: c_string_encoding=ascii  # for cython>=0.19
from  libcpp.string  cimport string as libcpp_string
from  libcpp.set     cimport set as libcpp_set
from  libcpp.vector  cimport vector as libcpp_vector
from  libcpp.pair    cimport pair as libcpp_pair
from  libcpp.map     cimport map  as libcpp_map
from  smart_ptr cimport shared_ptr
from  AutowrapRefHolder cimport AutowrapRefHolder
from  libcpp cimport bool
from  libc.string cimport const_char
from cython.operator cimport dereference as deref, preincrement as inc, address as address
from int_holder cimport IntHolder as _IntHolder
cdef extern from "autowrap_tools.hpp":
    char * _cast_const_away(char *) 

cdef class IntHolder:

    cdef shared_ptr[_IntHolder] inst

    def __dealloc__(self):
         self.inst.reset()

    
    property i_:
    
        def __set__(self,  i_):
        
            self.inst.get().i_ = (<int>i_)
        
    
        def __get__(self):
            cdef int _r = self.inst.get().i_
            py_result = <int>_r
            return py_result
    
    def __copy__(self):
       cdef IntHolder rv = IntHolder.__new__(IntHolder)
       rv.inst = shared_ptr[_IntHolder](new _IntHolder(deref(self.inst.get())))
       return rv
    
    def __deepcopy__(self, memo):
       cdef IntHolder rv = IntHolder.__new__(IntHolder)
       rv.inst = shared_ptr[_IntHolder](new _IntHolder(deref(self.inst.get())))
       return rv
    
    def _init_0(self,  i ):
        assert isinstance(i, (int, long)), 'arg i wrong type'
    
        self.inst = shared_ptr[_IntHolder](new _IntHolder((<int>i)))
    
    def _init_1(self, IntHolder i ):
        assert isinstance(i, IntHolder), 'arg i wrong type'
    
        self.inst = shared_ptr[_IntHolder](new _IntHolder((deref(i.inst.get()))))
    
    def __init__(self, *args):
        if (len(args)==1) and (isinstance(args[0], (int, long))):
             self._init_0(*args)
        elif (len(args)==1) and (isinstance(args[0], IntHolder)):
             self._init_1(*args)
        else:
               raise Exception('can not handle type of %s' % (args,))
    
    def add(self, IntHolder o ):
        assert isinstance(o, IntHolder), 'arg o wrong type'
    
        cdef int _r = self.inst.get().add((deref(o.inst.get())))
        py_result = <int>_r
        return py_result 
