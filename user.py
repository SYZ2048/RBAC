# role：Employee1,Employee2,Manager1,Manager2,Boss
# 给每个user分配一个或0多个角色
from GlobalVar import acc_lst


class User(object):
    def __init__(self, name, role):
        # self._user_id = uid # unique number for each user
        self._role = [i for i in set(role)]  # 创建一个无序不重复元素集
        self._name = name

    def print_role(self):   # print the user's all roles
        print("[", self._name, "] role:", self._role)

    def get_name(self):     # return the user's name
        return self._name

    def get_role(self):     # return the user's all roles
        return self._role

    def add_role(self, role):   # add role to the user
        self._role.extend(role)
        self._role = [i for i in set(self._role)]

    def del_role(self, role):   # delete role to the user
        for i in role:
            if i in self._role:
                self._role.remove(i)

    def is_user_allowed(self, operation):   # judge whether the user is allowed to do certain operation
        for r in self._role:
            if acc_lst.is_role_allowed(r, operation):
                return True
        return False



# # test code
# t = User("alice", ["manager", "Employee"])
# t.print_role()
# t.add_role(["Boss"])
# t.print_role()
# t.del_role(["manager"])
# t.del_role(["a"])












