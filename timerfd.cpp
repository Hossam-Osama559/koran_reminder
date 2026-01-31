#include <Python.h>

using namespace std;


extern "C"{

    #include<sys/timerfd.h>
    #include<unistd.h>
}


PyObject* create_timerfd(PyObject*self,PyObject*args){

    int initial,interval;


    PyArg_ParseTuple(args,"ii",&initial,&interval);   

    long fd=timerfd_create(CLOCK_REALTIME,0);

    itimerspec timer_spec; 


    timer_spec.it_value={initial,0};

    timer_spec.it_interval={interval,0};


    timerfd_settime(fd,0,&timer_spec,nullptr);

    return PyLong_FromLong(fd);


}


static PyMethodDef MyMethods[] = {
    {"create_timerfd", create_timerfd, METH_VARARGS, "creating a fd for timer "},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef mymodule = {
    PyModuleDef_HEAD_INIT,
    "mymodule",
    "c++ module for creating timer fd",
    -1,
    MyMethods
};

PyMODINIT_FUNC PyInit_timerfd(void) {
    return PyModule_Create(&mymodule);
}





