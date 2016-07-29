# Original int_holder.hpp
#class IntHolder {
#    public:
#        int i_;
#        IntHolder(int i): i_(i) { };
#        IntHolder(const IntHolder & i): i_(i.i_) { };
#        int add(const IntHolder & other) {
#            return i_ + other.i_;
#        }
#};

# Remove all ;
cdef extern from "int_holder.hpp" : # Insert "file_name"
    cdef cppclass  IntHolder: # Replace class <ClassName> { 
# Ignore public:
        int i_
        IntHolder(int i)
        IntHolder(IntHolder & i) # Delete any const declaration as they dont exist on Python
        int add(IntHolder o)
