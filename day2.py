'''Write a function called convert_add that takes
a list of strings as an argument and converts it
to integers and sums the list.
For example [‘1’, ‘3’, ‘5’]
should be converted to [1, 3, 5]
and summed to 9. '''

def convert_add(arguments):
    sum_ = 0
    convert = []
    for item in arguments:
        convert.append(int(item))
        sum_ += int(item)

    return(sum_ ,convert)

#I'm gonn' try to write the same function,
#But using the list compression concept


def using_list_compression(args):
    convert_ = [int(x) for x in args]
    add = 0 
    for i in convert_:
        add += i

    return (convert_, add)
print(convert_add(['1','23','434','55456','3232']))
print(using_list_compression(['1','23','434','55456','3232']))
        
            
