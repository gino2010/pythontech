# 
# author gino
# created on 2018/7/29


def checkio(password: str) -> bool:
    upper_flag = False
    lower_flag = False
    digit_flag = False
    if len(password) >= 10:
        for char in password:
            if not upper_flag and str.isupper(char):
                upper_flag = True
            if not lower_flag and str.islower(char):
                lower_flag = True
            if not digit_flag and str.isdigit(char):
                digit_flag = True
            if upper_flag and lower_flag and digit_flag:
                return True
        return False
    else:
        return False
