from src.algorithm import erratic_search

def main() -> None:

    search = input("Enter the misspelled word: ")
    
    instances = erratic_search(search)

    print(f"{search} not found, did you meant : {[guess for guess in instances]}?")
    
if __name__ == "__main__":
    main()