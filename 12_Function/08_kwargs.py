# **kwargs
def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="rohit",power="brain",enemy="Dr. jackeel")