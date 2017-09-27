def hello_world():
    print("- - - - Hello World Academy - - - - ");
    print("- - - - - - - - - - - - - - - - - - ");
    print("- - - - - - - Exercises - - - - - - ");
    print("------------------------------------");
    print("                                    ");
    print("---------- 1 - Fibonacci  -----------");
    index=5;
    print ("Position: %d" % (index))
    lista=fib(index);
    print (lista);
    print("------------------------------------");
    print("                                    ");
    print("----------  2 - Reverse list -------");
    original_list = [1,2,3,4,5,6];
    salida=[]
    print("Original List:")
    print(original_list);
    lista = reverse_list(original_list);
    print("Reverse List:")
    print(lista);
    print("------------------------------------");
    print("                                    ");
    print("-------- 3 - Cumulative_sum --------");
    original_list = [1, 2, 3, 4, 5, 6];
    print("Original List:")
    print(original_list);
    lista = cumulative_sum(original_list);
    print("Cumulative List:")
    print(lista);
    print("------------------------------------");
    print("                                    ");
    print("------ 4 - Cumulative_product ------");
    original_list = [1, 2, 3, 4, 5, 6];
    print("Original List:")
    print(original_list);
    lista = cumulative_product(original_list);
    print("Cumulative Produc:")
    print(lista);
    print("------------------------------------");
    print("                                    ");
    print("------- 5 - Unique_elements --------");
    original_list = [1,'a','b',2,3,4,5,'b',6,4,3,2,1];
    print("Original List:");
    print(original_list);
    lista = unique_list(original_list);
    print("unique elements:")
    print(lista);
    print("------------------------------------");
    print("                                    ");
    print("------- 6 - Duplicate_elements -----");
    original_list = [1,'a', 3, 4, 5, 6,'a', 3, 2, 1];
    print("Original List:");
    print(original_list);
    lista = duplicate_list(original_list);
    print("Duplicate elements:")
    print(lista);
    print("------------------------------------");
    print("                                    ");
    print("---------- 7- group list -----------");
    original_list = [1, 'a', 3, 4, 5, 6, 'a', 3, 2, 1];
    print("Original List:");
    print(original_list);
    lista = group(original_list,4);
    print("Duplicate elements:")
    print(lista);
    print("------------------------------------");


def fib(n):
    if n == 0:                         #case 0
        return [0]
    elif n == 1:                       #case 1
        return [0, 1]
    else:
        lst = fib(n-1)                 #case 3 or more
        lst.append(lst[-1] + lst[-2])  #we add list a lass value
        return lst



def reverse_list(o_list):
    lst = [];                            #final list
    con=-1;                              #inverse counter
    for item in o_list:                  #loop
        position= int(len(o_list)+con)   #get inverse position
        lst.append(o_list[position])     #add to final list
        con=con-1                        #move
    return lst                           #return


def cumulative_sum(o_list):
    lst=[];                              #final list
    total=0;                             #total
    for item in o_list:                  #loop
        total += item;                   #box
        lst.append(total);               #add box
    return lst                           #return

def cumulative_product(o_list):
    lst=[];                             #final list
    total=1;                            #total
    for item in o_list:                 #loop
        total = total * item;           #box
        lst.append(total);              #add box

    return lst

def unique_list(o_list):
    elements = o_list #set(o_list) #AttributeError: 'set' object has not attribute 'count'
    final_list=[x for x in elements if (elements).count(x) == 1]
    #         loop elements origin        condition    item into element =1
    return final_list

def duplicate_list(o_list):
    elements = o_list #set(o_list) #AttributeError: 'set' object has not attribute 'count'
    final_list=set([x for x in elements if (elements).count(x) >= 2])
    #         loop elements origin        condition    item into element =2

    return final_list

def group(o_list,num):
    tem=[]
    final=[]
    con=0;
    for item in o_list:
       tem.append(item)

    final.append(tem);


hello_world();