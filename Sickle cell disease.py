def translate(dna_sequence):
    
    arr_list=[]
    dnaLength = len(dna_sequence)             
    dnaCodeRange = dnaLength/3
 
    for i in range(0,dnaCodeRange): 
		
        x = 3 * i
        y = x + 3
 
		
        dnaCode = dna_sequence[x:y]
        if dnaCode == "ATT" or dnaCode == "ATC" or dnaCode == "ATA":
            slc = "I"
        elif dnaCode == "CTT" or dnaCode == "CTC" or dnaCode == "CTA" or dnaCode == "CTG" or dnaCode == "TTA" or dnaCode == "TTG":
            slc = "L"
        else:
            slc = "X"

        arr_list.append(slc)
        slc_output ="".join(arr_list)
    return slc_output


inputCodon = raw_input("Enter a DNA codon:")
if inputCodon != "GTGCACCTGACTCCTGTG":
    translatedCode = translate(inputCodon)
    print(translatedCode)
else:
    print("This DNA sequence translates to sickle cell disease!")
