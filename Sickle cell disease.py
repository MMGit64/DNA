def translate(dna_sequence):
    
    arr_list=[]
    dnaLength = len(dna_sequence)             
    dnaCode = dna_len/3				# This reads what is contained in the length within 6 characters before reading next set of 6.
 
    for i in range(0,codon_num): 
		
        x = 3 * i					# Allows UPTO 6 general characters IN ENTIRE length to be read for quantity of y within x	
        y = x + 3					# READS exactly 3 characters within x.
 
		
        dnaCode = dna_sequence[x:y]
        if dnaCode == "ATT" or dnaCode == "ATC" or dnaCode == "ATA":
            slc = "I"
        elif dnaCode == "CTT" or dnaCode == "CTC" or dnaCode == "CTA" or dnaCode == "CTG" or dnaCode == "TTA" or dnaCode == "TTG":
            slc = "L"
        else:
            slc = "X"

        arr_list.append(slc)						#Appends the slc letter codes.
        slc_output ="".join(arr_list)					#Joins the letters into a sequence
    return slc_output


inputCodon = raw_input("Enter a DNA codon:")
if inputCodon != "GTGCACCTGACTCCTGTG":
    translatedCode = translate(inputCodon)
    print(translatedCode)
else:
    print("This DNA sequence translates to sickle cell disease!")
