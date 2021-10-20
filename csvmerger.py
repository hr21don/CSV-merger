import csv

def merge_csv(csv_list, output_path):
    # build list with all fieldnames

    fieldnames = list()#empty list
    for file in csv_list: #opens up all the files in the input list of csv files to merge
        with open(file, 'r') as input_csv: 
            fn = csv.DictReader(input_csv).fieldnames # using csv module dictreader to extract all field names from each file
            fieldnames.extend(x for x in fn if x not in fieldnames)# add them to the fieldnames list if they're not already in there

    #write data to output file based on field names
    with open(output_path, 'w', newline='') as output_csv: #context manager to open the output file
        writer = csv.DictWriter(output_csv, fieldnames = fieldnames)# use the csv module to create a new Dictwriter object to pass in the list of field names created
        writer.writeheader()#writing the first header row to the output file
        for file in csv_list:#for loop to iterate all the csv files
            with open(file,'r') as input_csv:
                reader = csv.DictReader(input_csv) #creating new DictReader
                for row in reader: #iterating each record within that input file and write it to output file
                    writer.writerow(row)
                
