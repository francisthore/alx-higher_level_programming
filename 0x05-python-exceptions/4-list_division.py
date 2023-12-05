#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    try:
        res_list = []
        for i in range(list_length):
            result = 0
            try:
                result = my_list_1[i] / my_list_2[i]
                res_list.append(result)
            except TypeError:
                res_list.append(result)
                print("wrong type")
            except ZeroDivisionError:
                res_list.append(result)
                print("division by 0")
            except IndexError:
                res_list.append(result)
                print("out of range")

    except Exception:
        pass
    finally:
        return res_list
