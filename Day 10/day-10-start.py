# Functions with Outputs

def format_name(f_name, l_name):
    if f_name =="" or l_name =="":
        return "You didn't provide valid inputs"
    full_name = f_name.title()+' '+l_name.title()
    return full_name

full_name=format_name(input("Your first name: "), input("Your last name: "))
print(full_name)