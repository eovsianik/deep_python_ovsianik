#include <Python.h>

#include "cjson/cJSON.h"

PyObject *cjson_loads(PyObject *self, PyObject *args) {
    char *json_str;
    if (!PyArg_ParseTuple(args, "s", &json_str)) {
        return NULL;
    }
}

PyObject *cjson_dumps(PyObject *self, PyObject *args) {
    PyObject *dict;
    if (!PyArg_ParseTuple(args, "O", &dict)) {
        return NULL;
    }
}

static PyMethodDef methods[] = {
    {"loads", cjson_loads, METH_VARARGS},
    {"dumps", cjson_dumps, METH_VARARGS},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef module_cjson =
    {PyModuleDef_HEAD_INIT, "cjson", NULL, -1, methods};

PyMODINIT_FUNC PyInit_cjson() {
    return PyModule_Create(&module_cjson);
}