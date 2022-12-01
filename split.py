def splait(string,div=" "):
    if type(string)!=str or type(div)!=str or len(div)>1:
        print("pinshi tonto, una entrada esta mal (string!=str or div!=chr)")
        return None
    start=0
    array=[]
    for i in range(len(string)):
        if string[i]==div:
            if i-start>0:
                array.append(string[start:i])
            start=i+1
    if start<len(string):
        array.append(string[start:])
    return array



def main() -> None :
    palabritas = "Hola mundo"  
    print(splait(palabritas," "))  



if __name__ == '__main__':
    main()