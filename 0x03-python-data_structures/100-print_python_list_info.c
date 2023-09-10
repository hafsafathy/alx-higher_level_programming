#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - function that returns a
 * tuple with the length of a string and its first character.
 * @p: PyObject
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
	long int s, i;
	PyListObject *lst;
	PyObject *t;

	s = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", s);

	lst = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", lst->allocated);

	for (i = 0; i < s; i++)
	{
		t = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(t)->tp_name);
	}
}
