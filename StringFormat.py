
inputString = """transaction,po
jan_20,50
feb_20,56
mar_20,0
transaction,so
jan_20,1
feb_20,100
mar_20,0
transaction,inv
jan_20,123
feb_20,120
mar_20,98
master,customer
jan_20,1
feb_20,4
mar_20,7
master,supplier
jan_20,2
feb_20,5
mar_20,8
master,supplierSite
jan_20,3
feb_20,6
mar_20,9"""

def wrap_by_word(s, n):
    a = s.split(",")
    ret = ''
    for i in range(0, len(a), n):
        ret += ','.join(a[i:i+n]) + '\n'
    return ret

m_c_t=3 #configure for months of report on Transactions
m_c_m=3 #configure for months of report on Master
t1="transaction"
t2=""
m1=",master"
m2=""
editedInputString = inputString.replace(",","\n")
list=editedInputString.split("\n")
index=0
indexForModule=len(list)/2
print("\n")
for j in list:
    if index<indexForModule:
        if index % 2 == 0:
            if j=="transaction":
                index=index+1
                continue
            else:
                index=index+1
                if m_c_t>0:
                    t1=",".join((t1, j))
                    m_c_t=m_c_t-1
                    continue
        else:
            t2=",".join((t2, j))
            index=index+1
            continue
            
    elif index>=indexForModule:
        if index % 2 == 0:
            if j=="master":
                index=index+1
                continue
            else:
                index=index+1
                if m_c_m>0:
                    m1=",".join((m1, j))
                    m_c_m=m_c_m-1
                    continue
        else:
            m2=",".join((m2, j))
            index=index+1
            continue


output_string=t1 + t2 + m1 + m2

formattedOutputString = wrap_by_word(output_string,4)
print(formattedOutputString)







