import requests
from demo_pydepands_childrepo.sub_main import some_method




def main():
    r = requests.get('https://www.google.ca')
    print(r.status_code)

    print(f"expecting numpy matrix of ones shaped 5x5 sum hence 25")
    print(some_method(shape=(5,5)))

if __name__ == '__main__':
    main()