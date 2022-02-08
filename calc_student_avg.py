import csv

def main():

    infile = open("Student_Scores.csv", 'r')

    student_file = csv.reader(infile, delimiter=',')


    outfile = open("student_avg.csv", "w")

    for record in student_file:
        FirstName = record [0]
        Grade_1 = record [1]
        Grade_2 = record[2]
        Grade_3 = record[3]
        Average = (float(record[1]) + float(record[2]) + float(record[3]))/3

        outfile.write(FirstName + " " + format(round(Average, 2)) + "\n")

    infile.close()
    outfile.close()

main()