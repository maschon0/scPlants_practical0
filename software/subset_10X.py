import gzip

f1 = gzip.open('../resources/fastq_files/C1_S1_L002_R1_001.fastq.gz', 'rt')
f2 = gzip.open('../resources/fastq_files/C1_S1_L002_R2_001.fastq.gz', 'rt')

o1 = open('../resources/fastq_files/TMM_10X_subset_R1.fastq','w')
o2 = open('../resources/fastq_files/TMM_10X_subset_R2.fastq','w')

whitelist = [line.rstrip() for line in open('../resources/fastq_files/whitelist.txt')]
# blacklist = set([line.rstrip() for line in gzip.open('../resources/fastq_files/blacklist.txt.gz', 'rt') if line.rstrip() not in whitelist])
# ham1set = set()
# ham1set.update(whitelist)
# for w in whitelist:
    # for i in range(len(w)):
        # for n in ['A','C','G','T','N']:
            # seq = w[:i]+n+w[i+1:]
            # if seq not in blacklist:
                # ham1set.add(seq)

# whiteset = ham1set
whiteset = set(whitelist)


l=0
outline1 = ''
outline2 = ''
write = False
for line1,line2 in zip(f1,f2):
    if l % 4 == 0: # Output read
        if write:
            trash = o1.write(outline1)
            trash = o2.write(outline2)
        
        outline1 = ''
        outline2 = ''
    elif l % 4 == 1: # Check if the barcode matches the whitelist
        write = line1[:16] in whiteset
    
    # Add reads to queue
    outline1 += line1
    outline2 += line2
    l += 1

o1.close()
o2.close()
f1.close()
f2.close()
