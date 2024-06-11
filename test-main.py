def main() -> None:
    print()
    MyClass = type("", (), {})
    my_obj = MyClass()
    print(type(my_obj))
    

if __name__ == '__main__':
    main()