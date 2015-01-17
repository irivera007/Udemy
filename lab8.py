def taxon(x):

    if( x==True or x=="T" or x=="F" or x==False):
        return "is Boolean"
    elif x.isdigit():
        return "is Digit 12345.."
    elif x.isalnum():
        return "is Alphanum 124ABDC"
    else:
        return "Type Unknown"


print(taxon('T'))
        