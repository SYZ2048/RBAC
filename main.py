# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from AccessList import AccessList
from user import User


if __name__ == '__main__':
    print('**** Welcome, RBAC ****')

    # test user
    A = User("A", ["Employee1"])
    C = User("C", ["Employee2"])
    M1 = User("M1", ["Manager1"])
    M2 = User("M2", ["Manager2"])
    boss = User("boss", ["Boss"])

    A.print_role()
    if A.is_user_allowed("execute"):
        print("[", A.get_name(), "] Execute is accessible")
    else:
        print("[", A.get_name(), "] Execute is NOT accessible")

    if A.is_user_allowed("new"):
        print("[", A.get_name(), "] New is accessible")
    else:
        print("[", A.get_name(), "] New is NOT accessible")

    A.add_role(["Manager2"])
    A.del_role(["Employee1"])

    A.print_role()
    if A.is_user_allowed("execute"):
        print("[", A.get_name(), "] Execute is accessible")
    else:
        print("[", A.get_name(), "] Execute is NOT accessible")

    if A.is_user_allowed("new"):
        print("[", A.get_name(), "] New is accessible")
    else:
        print("[", A.get_name(), "] New is NOT accessible")


    # alice = User("alice", ["Employee1"])
    # alice.print_role()
    # # alice.add_role(["Boss"])
    #
    # print("alice try to access to file")
    # if alice.is_user_allowed("new"):
    #     print(alice.get_name(), "new is accessible")
    # else:
    #     print(alice.get_name(), "new is NOT accessible")
    # if alice.is_user_allowed("delete"):
    #     print(alice.get_name(), "delete is accessible")
    # else:
    #     print(alice.get_name(), "delete is NOT accessible")
    #
    # alice.add_role(["Boss"])
    # alice.print_role()
    # print("alice try to access to file")
    # if alice.is_user_allowed("new"):
    #     print(alice.get_name(), "new is accessible")
    # else:
    #     print(alice.get_name(), "new is NOT accessible")
    # if alice.is_user_allowed("delete"):
    #     print(alice.get_name(), "delete is accessible")
    # else:
    #     print(alice.get_name(), "delete is NOT accessible")
    #



