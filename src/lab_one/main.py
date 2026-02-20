from lab_one.formulas import calculate_linar_function, calculate_curved_function, calculate_cyclic


def main():
    print(calculate_linar_function(a=4, c=5, x= 6))
    print(calculate_curved_function(a=4, c=5, p=6, k=3))
    print(calculate_cyclic(a=[1,4,6], b=[2,5,7]))




if __name__ == "__main__":
    main()