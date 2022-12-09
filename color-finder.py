import pandas as pd
import sys
import logging
import random

df = pd.DataFrame()

def main():
    args = sys.argv[1:]
    if len(args) == 4 and args[0] == '-input' and args[2] == '-count' and args[3].isnumeric():
        try:
            global df
            df = pd.read_csv(filepath_or_buffer=args[1], delimiter=';')
            df = df[["0.1","0.2","0.3"]]
            for i in range(int(args[3])):
                print(find_color())
        except BaseException:
            logging.exception("incorrect -input path")
    else:
        print("input format: python color-finder -input <path> -count <num>")


def find_color():
    global df
    found_unique = False
    while not found_unique:
        R = random.randint(0,255)
        G = random.randint(0,255)
        B = random.randint(0,255)
        lookup = df.loc[(df["0.1"]==R)&(df["0.2"]==G)&(df["0.2"]==B)]
        if lookup.empty:
            found_unique = True
    
    df.loc[len(df.index)] = [R,G,B]
    return str(R)+";"+str(G)+";"+str(B)

if __name__ == "__main__":
    main()