from AccessList import AccessList


def init_employee1():
    global acc_lst
    acc_lst.add_permissoion("Employee1", "read")
    acc_lst.add_permissoion("Employee1", "execute")


def init_employee2():
    global acc_lst
    acc_lst.add_permissoion("Employee2", "new")
    acc_lst.add_permissoion("Employee2", "read")
    acc_lst.add_permissoion("Employee2", "alter")


def init_manager1():
    global acc_lst
    acc_lst.add_permissoion("Manager1", "delete")
    acc_lst.add_permissoion("Manager1", "read")
    acc_lst.add_permissoion("Manager1", "execute")


def init_manager2():
    global acc_lst
    acc_lst.add_permissoion("Manager2", "new")
    acc_lst.add_permissoion("Manager2", "delete")
    acc_lst.add_permissoion("Manager2", "read")
    acc_lst.add_permissoion("Manager2", "alter")


def init_boss():
    global acc_lst
    acc_lst.add_permissoion("Boss", "new")
    acc_lst.add_permissoion("Boss", "delete")
    acc_lst.add_permissoion("Boss", "read")
    acc_lst.add_permissoion("Boss", "alter")
    acc_lst.add_permissoion("Boss", "execute")


global acc_lst
acc_lst = AccessList()
init_employee1()
init_employee2()
init_manager1()
init_manager2()
init_boss()
acc_lst.print_permission()


