# Simple function to facilitate Dynamically receiving arguments
# *args parameter is to receive n-number of positional arguments
# **kwargs parameter is to receive n-number of key-value pairs
def dynamic_para(*args,a, b, c, **kwargs):
    return f"{a=}, {b=},{c=},{args=}, {kwargs=}"

# The positional arguments should start first while passing arguments
# The keyword arguments can start first, but only be followed by keyword arguments only
print(dynamic_para(10, 20, 30, 40, 50, a=60, b=70, c=50, dd=80, ee=90, ff=100))





