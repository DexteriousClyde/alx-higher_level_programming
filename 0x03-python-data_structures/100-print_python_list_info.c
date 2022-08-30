#include "Python.h"

/**
 * print_python_list_info - Main
 * @p: PyObject
 * Return: void
*/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size;
	PyObject *t;
	const char *type;
	PyListObject *cast;

	cast = (PyListObject *)p;
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", (int) size);
	printf("[*] Allocated = %d\n", (int) cast->allocated);
	for (i = 0; i < size; i++)
	{
		t = PyList_GetItem(p, i);
		type = Py_TYPE(t)->tp_name;
		printf("Element %d: %s\n", (int) i, type);
	}
}
