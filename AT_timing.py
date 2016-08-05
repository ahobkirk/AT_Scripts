
def createOutFileName(base_file_name, class_of_subject):
    return 'M:\DECIDE.01\Analysis\Behavioral\combined_AT_files\AT_Timing_2016_0805\\'+base_file_name+'_'+class_of_subject+'<replace_me>.txt'

read_only = "r"
Lookup='M:\DECIDE.01\Analysis\Behavioral\AT_combine_lookup_full.txt'
file = open(Lookup, "r")
file_in=list()
for line in file.readlines():
    line_split = line.split("\t")
    file_in.append('M:\DECIDE.01\Analysis\Behavioral\combined_AT_files\AT_'+line_split[0]+'_combined.txt')

for name in file_in:
    #text = open(name, read_only)
    base_file_name = name[name.rindex('\\')+1:name.rindex("_")]
    #print "full path : " + name
    #print "base name " + base_file_name
    base_ambig_file_name = createOutFileName(base_file_name,'Ambig')
    output_Ambig= open(base_ambig_file_name.replace('<replace_me>', '_1'), "w")
    base_risky_file_name = createOutFileName(base_file_name, 'Risky')
    output_Risky = open(base_risky_file_name.replace('<replace_me>', '_1'), "w")
    base_risky25_file_name = createOutFileName(base_file_name, 'Risky25')
    output_Risky25 = open(base_risky25_file_name.replace('<replace_me>', '_1'), "w")
    base_risky50_file_name = createOutFileName(base_file_name, 'Risky50')
    output_Risky50 = open(base_risky50_file_name.replace('<replace_me>', '_1'), "w")
    base_risky75_file_name = createOutFileName(base_file_name, 'Risky75')
    output_Risky75 = open(base_risky_file_name.replace('<replace_me>', '_1'), "w")

    subjectfile = open(name, "r")
    counter = 0
    firstline = True
    starttime = float(0)
    for line in subjectfile.readlines():
        # Ambiguous Trials
        #skip header line
        if firstline:
            firstline = False
            continue

        #break up tabs
        line_split = line.split("\t")

        if counter % 40 == 0:
            if counter != 0:
                output_Ambig.close()
                output_Risky.close()
                output_Risky25.close()
                output_Risky50.close()
                output_Risky75.close()
                if counter != 120:
                    output_Ambig = open(base_ambig_file_name.replace('<replace_me>', '_' + str((counter / 40) + 1)), 'w')
                    output_Risky = open(base_risky_file_name.replace('<replace_me>', '_' + str((counter / 40) + 1)), 'w')
                    output_Risky25 = open(base_risky25_file_name.replace('<replace_me>', '_' + str((counter / 40) + 1)),
                                          'w')
                    output_Risky50 = open(base_risky50_file_name.replace('<replace_me>', '_' + str((counter / 40) + 1)),
                                          'w')
                    output_Risky75 = open(base_risky75_file_name.replace('<replace_me>', '_' + str((counter / 40) + 1)),
                                          'w')
            starttime = float(line_split[0])
        correctstart = float(line_split[0])-starttime
        #put ambigous trials into its file
        if "4" in line_split[2]:
            #print line_split[0] + "\t" + line_split[1] + "\t1\n"
            output_Ambig.write(str(correctstart) + "\t" + line_split[1] + "\t1\n")
        if "3" in line_split[2]:
            output_Risky.write(str(correctstart) + "\t" + line_split[1] + "\t1\n")

        if "3" in line_split[2] and "0.25" in line_split[5]:
            output_Risky25.write(str(correctstart) + "\t" + line_split[1] + "\t1\n")
        elif "3" in line_split[2] and "0.50" in line_split[5]:
            output_Risky50.write(str(correctstart) + "\t" + line_split[1] + "\t1\n")
        elif "3" in line_split[2] and "0.75" in line_split[5]:
            output_Risky75.write(str(correctstart) + "\t" + line_split[1] + "\t1\n")
        #every 40 records needs to be split up regardless of type

        counter += 1
# for Text = open("file_in", "r")
# outfile = open("'line_split[0]+'_timing.txt", "w")
#


        #file = open("AT_xxxx_combined.txt", "r")