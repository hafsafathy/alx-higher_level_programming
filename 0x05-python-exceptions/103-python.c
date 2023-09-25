#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int s, i, l;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	s = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", s);
	printf("  trying string: %s\n", str);

	if (s >= 10)
		l = 10;
	else
		l = s + 1;

	printf("  first %ld bytes:", l);

	for (i = 0; i < l; i++)
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);

	printf("\n");
	setbuf(stdout, NULL);
}

/**
 * print_python_float - Prints float
 * @p: Python Object
 * Return: no return
 */
void print_python_float(PyObject *p)
{
	double v;
	char *s;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	v = ((PyFloatObject *)(p))->ob_fval;
	s = PyOS_double_to_string(v, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

	printf("  value: %s\n", s);
	setbuf(stdout, NULL);
}

/**
 * print_python_list - Prints list
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int s, i;
	PyListObject *lst;
	PyObject *ob;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	s = ((PyVarObject *)(p))->ob_size;
	lst = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", lst->allocated);

	for (i = 0; i < s; i++)
	{
		ob = lst->ob_item[i];
		printf("Element %ld: %s\n", i, ((ob)->ob_type)->tp_name);

		if (PyBytes_Check(ob))
			print_python_bytes(ob);
		if (PyFloat_Check(ob))
			print_python_float(ob);
	}
	setbuf(stdout, NULL);
}
