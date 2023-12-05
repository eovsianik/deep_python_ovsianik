#include <Python.h>

#include "cjson/cJSON.h"

static void replace_tabs(char *str) {
    char *p = str;
    while (*p) {
        if (*p == '\t') {
            *p = ' ';
        } else {
            p++;
        }
    }
}

static void remove_newlines(char **str) {
    if (str == NULL || *str == NULL || **str == '\0') {
        return;
    }

    size_t len = strlen(*str);
    size_t count = 0;
    char *p = *str;
    while (*p) {
        if (*p == '\n') {
            count++;
        }
        p++;
    }

    char *new_str = malloc(len - count + 1);
    if (new_str == NULL) {
        return;
    }

    p = *str;
    char *q = new_str;
    while (*p) {
        if (*p != '\n') {
            *q++ = *p;
        }
        p++;
    }
    *q = '\0';

    free(*str);
    *str = new_str;
}

PyObject *cjson_loads(PyObject *self, PyObject *args) {
    char *json_str;
    if (!PyArg_ParseTuple(args, "s", &json_str)) {
        return NULL;
    }

    cJSON *json = cJSON_Parse(json_str);
    if (json == NULL) {
        PyErr_Format(PyExc_TypeError, "Expected object or value");
        return NULL;
    }

    PyObject *dict = PyDict_New();
    cJSON *item = NULL;
    cJSON_ArrayForEach(item, json) {
        PyObject *key = Py_BuildValue("s", item->string);
        if (item->type == cJSON_String) {
            PyObject *value = Py_BuildValue("s", item->valuestring);
            PyDict_SetItem(dict, key, value);
        } else if (item->type == cJSON_Number) {
            PyObject *value = Py_BuildValue("d", item->valuedouble);
            PyDict_SetItem(dict, key, value);
        }
    }

    cJSON_Delete(json);
    return dict;
}

PyObject *cjson_dumps(PyObject *self, PyObject *args) {
    PyObject *dict;
    if (!PyArg_ParseTuple(args, "O", &dict)) {
        return NULL;
    }

    cJSON *json = cJSON_CreateObject();
    PyObject *key, *value;
    Py_ssize_t pos = 0;
    while (PyDict_Next(dict, &pos, &key, &value)) {
        if (value == Py_None) {
            cJSON_AddItemToObject(json, PyUnicode_AsUTF8(key), cJSON_CreateNull());
        } else if (PyLong_Check(value)) {
            cJSON_AddItemToObject(json, PyUnicode_AsUTF8(key), cJSON_CreateNumber(PyLong_AsLong(value)));
        } else if (PyFloat_Check(value)) {
            cJSON_AddItemToObject(json, PyUnicode_AsUTF8(key), cJSON_CreateNumber(PyFloat_AsDouble(value)));
        } else if (PyUnicode_Check(value)) {
            cJSON_AddItemToObject(json, PyUnicode_AsUTF8(key), cJSON_CreateString(PyUnicode_AsUTF8(value)));
        } else {
            PyErr_Format(PyExc_TypeError, "Unsupported value type");
            return NULL;
        }
    }

    char *json_str = cJSON_Print(json);
    remove_newlines(&json_str);

    // remove first char
    const size_t idxToDel = 1;
    memmove(&json_str[idxToDel], &json_str[idxToDel + 1], strlen(json_str) - idxToDel);

    replace_tabs(json_str);
    PyObject *result = Py_BuildValue("s", json_str);
    cJSON_Delete(json);
    cJSON_free(json_str);
    return result;
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