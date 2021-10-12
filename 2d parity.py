def testing(reciever,div=5):
    
    message=str()
    length=len(reciever)
    #removing last column parity
    col = reciever[length-div:]
    reciever = reciever[:length-div]
    
    #checking error at parity in rows(added in middle by sender) and then removing
    row=[]
    row_count=0
    while(reciever):
        chunk = reciever[:div]
        old_parity=int(reciever[div])
        reciever = reciever[div+1:]
        message+=chunk
        
        sum_chunk=0
        for i in range(div):
            sum_chunk += int(chunk[i])
        if old_parity != (sum_chunk%2):
            row.append(row_count)
        row_count+=1
        
    print("Error in row_parity at",row)      
    
    #checking parity in columns
    col_len=len(message)//div
    col_parity=[]
    for j in range(div):
        sum_chunk=0
        for i in range(col_len):
            sum_chunk += int(message[i*div+j])
        if int(col[j]) != (sum_chunk%2):
            col_parity.append(j)
            
    print("Error in col_parity at",col_parity)        
    print("message received",message)
    
def addingParity(string,div=5):
    message=str()
    #adding parity in rows format
    while(string):
        chunk = string[:div]
        string = string[div:]
        message+=chunk
        
        sum_chunk=0
        if len(chunk)==div:
            for i in range(div):
                sum_chunk += int(chunk[i])
            #parity adding
            message+=str(sum_chunk%2) 
        else:
            for i in range(div-len(chunk)): #padding zeros
                message+='0'
            for i in range(len(chunk)):
                sum_chunk += int(chunk[i])
            #parity adding  
            message +=str(sum_chunk%2)
            
    #adding parity in columns format
    column_len=len(message)//(div+1)
    for i in range(div):
        sum_column=0
        for j in range(column_len):
            sum_column += int(message[i+(div+1)*j])
        message += str(sum_column%2)
    return message

if __name__=='__main__':

    input_message=input("\nEnter binary code for sending a message ")

    sender_message=addingParity(input_message)
    print("sender message ",sender_message)
    input_test=input("\nEnter binary code for testing of message ")

#     reciever_message=addingParity(input_test)
#     print("reciever message ",reciever_message)  
    print("\nTesting result is here.......")
#     test(sender_message,reciever_message)
    testing(input_test)    