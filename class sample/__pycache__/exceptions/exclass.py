import sys
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("Exception raised from D !!")
    except C:
        print("Exception raised from C !!")
    except B:
        print("Unexpected error:", sys.exc_info()[0])
        print("Exception raised from B !!")