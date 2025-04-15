def get_details(**kwargs):
    print(kwargs)


get_details(name = "Joy" ,age = 36, city="Mombasa")


def get_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


get_details(name = "Joy" ,age = 36, city="Mombasa")


