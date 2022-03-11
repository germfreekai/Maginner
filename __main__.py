import maginner

def main():
    str = input("Give me a str: ")

    if maginner.maginner(str):
        print("Success")
    else:
        print("Could not load banner")

if __name__ == '__main__':
    main()
