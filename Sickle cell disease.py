def translate(dna_sequence):
    
    arr_list=[]
    dnaLength = len(dna_sequence)             
    dnaCode = dna_len/3
 
    for i in range(0,codon_num): 
		
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








ofile = open("normalDNA.txt", "w")
f = open("DNA.txt", "r+")
for list in f:
    list = list.replace('a', 'A')
    translatedNormalCode = translate(list)
    ofile.write(translatedNormalCode)
f.close()
ofile.close()
 
 
 
ofile = open("mutatedDNA.txt", "w")
f = open("DNA.txt", "r+")
for list in f:
    list = list.replace('a', 'T')
    translatedMutatedCode = translate(list)
    ofile.write(translatedMutatedCode)
f.close()
ofile.close()

