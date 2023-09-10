#include "Python.h"
#include <stdlib.h>

/**
 * print_python_list_info - function that prints some basic info
 * about Python lists.
 * @p: in
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = NULL;
	size_t l = 0, i = 0;
	const char *type = NULL;

	l = PyList_Size(p);
	list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", l);
	printf("[*] Allocated = %ld\n", (signed long)(list->allocated));
	for  (; i < l; i++)
	{
		type = Py_TYPE(list->ob_item[i])->tp_name;
		printf("Element %ld: %s\n", i, type);
	}
}
