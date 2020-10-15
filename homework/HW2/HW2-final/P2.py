def dna_complement(dnastring):
    if len(dnastring)==0:
        return 'None'
    output=''
    for letter in dnastring:
        letter=letter.upper()
        
        if letter=='A':
            output+='T'
        elif letter=='T':
            output+='A'
        elif letter=='C':
            output+='G'
        elif letter=='G':
            output+='C'
        else:
            return 'None'
    return(output)
            
print("Input1:",'acgCt')
output1=dna_complement('acgCt')
print("Output1:",output1)

print("Input2:",'Xyzzy')
output2=dna_complement('Xyzzy')
print("Output2:",output2)
