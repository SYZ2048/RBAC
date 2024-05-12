# 给每种role分配权限
class AccessList(object):
    def __init__(self):
        self._new = []
        self._delete = []
        self._read = []
        self._alter = []
        self._execute = []

    def print_permission(self): # print all role-permission relations
        print("**** current role-permission relation ****")
        print("new:", self._new)
        print("delete:", self._delete)
        print("read:", self._read)
        print("alter:", self._alter)
        print("execute", self._execute)

    def add_permissoion(self, role, operation):     # add certain permission to certain role
        if operation == "new":
            if role not in self._new:
                self._new.append(role)
        elif operation == "delete":
            if role not in self._delete:
                self._delete.append(role)
        elif operation == "read":
            if role not in self._read:
                self._read.append(role)
        elif operation == "alter":
            if role not in self._alter:
                self._alter.append(role)
        elif operation == "execute":
            if role not in self._execute:
                self._execute.append(role)

    def del_permissoion(self, role, operation):     # delete certain permission to certain role
        if operation == "new":
            if role in self._new:
                self._new.remove(role)
        elif operation == "delete":
            if role in self._delete:
                self._delete.remove(role)
        elif operation == "read":
            if role in self._read:
                self._read.remove(role)
        elif operation == "alter":
            if role in self._alter:
                self._alter.remove(role)
        elif operation == "execute":
            if role in self._execute:
                self._execute.remove(role)

    def is_role_allowed(self, role, operation):     # judge whether certain role is allowed to do certain operation
        if operation == "new":
            if role in self._new:
                return True
            else:
                return False
        elif operation == "delete":
            if role in self._delete:
                return True
            else:
                return False
        elif operation == "read":
            if role in self._read:
                return True
            else:
                return False
        elif operation == "alter":
            if role in self._alter:
                return True
            else:
                return False
        elif operation == "execute":
            if role in self._execute:
                return True
            else:
                return False
