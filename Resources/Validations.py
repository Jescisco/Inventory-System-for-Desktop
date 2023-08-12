class Validations():

    def validate_entrys(self, *args):
        for entry in args:
            status=False if (entry=="" or entry=="S" or entry=="Sele") else True
            if status==False:
                return False
        return status

    def validate_len(self, entry, limit):
        if len(entry)<=int(limit):
            return True
        elif entry=="":
            return True
        else:
            return False

    def validate_len_and_alphanumerics(self, entry, limit):
        if all(char.isalnum() or char.isspace() for char in entry) and len(entry)<=int(limit):
            return True
        elif entry=="":
            return True
        else:
            return False

    def validate_len_and_numerics(self, entry, limit):
        if entry.isdigit() and len(entry)<=int(limit):
            return True
        elif entry=="":
            return True
        else:
            return False

    def validate_len_and_alpha(self, entry, limit):
        if all(char.isalpha() or char.isspace() for char in entry) and len(entry)<=int(limit):
            return True
        elif entry=="":
            return True
        else:
            return False