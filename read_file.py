try:
    file1=open("sample.txt", "r")
    line_number=1
    print("Reading file content:")
    for line in file1:
        line = line.replace("\n", "")
        print("Line" , str(line_number) + ":", line)
        line_number += 1
    file1.close()
except FileNotFoundError:
    print("Error: The File 'sample.txt' was not found.")

