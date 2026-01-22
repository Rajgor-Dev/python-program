'''
 Type Casting is the process of converting one data type to another data type.
 In Python, we can perform type casting using built-in functions like 
 int(), float(), str(), bool(), etc.
''' 
# Integer -> other types
x = 10
int_to_float = float(x)
int_to_str = str(x)
int_to_bool = bool(x)  # 0 -> False, any non-zero -> True
print("int -> float:", int_to_float, type(int_to_float))
print("int -> str:", int_to_str, type(int_to_str))
print("int -> bool:", int_to_bool, type(int_to_bool))

# Float -> other types
f = 15.7
float_to_int = int(f)  # truncates toward zero
float_to_str = str(f)
float_to_bool = bool(f)  # 0.0 -> False, others -> True
print("float -> int:", float_to_int, type(float_to_int))
print("float -> str:", float_to_str, type(float_to_str))
print("float -> bool:", float_to_bool, type(float_to_bool))

# String -> other types
num_str = "30"
str_to_int = int(num_str)
str_to_float = float(num_str)
str_to_bool = bool(num_str)  # non-empty -> True,empty -> False
print("str -> int:", str_to_int, type(str_to_int))
print("str -> float:", str_to_float, type(str_to_float))
print("str -> bool:", str_to_bool, type(str_to_bool))

# Boolean -> other types
flag = False
bool_to_int = int(flag)
bool_to_float = float(flag)
bool_to_str = str(flag)
print("bool -> int:", bool_to_int, type(bool_to_int))
print("bool -> float:", bool_to_float, type(bool_to_float))
print("bool -> str:", bool_to_str, type(bool_to_str))

# None -> other types
none_val = None
none_to_str = str(none_val)
none_to_bool = bool(none_val)  # None -> False
print("None -> str:", none_to_str, type(none_to_str))
print("None -> bool:", none_to_bool, type(none_to_bool))

# Notes:
'''
Not all conversions are valid:
- Converting a non-numeric string to int/float raises ValueError.
- Converting None to int or float raises TypeError.
- Converting None to bool returns False.
'''