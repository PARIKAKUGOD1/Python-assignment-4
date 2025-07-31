text = input("Enter text to write to the file:")
file1 = open("output.txt", "w")
file1.write(text)
print("Data successfully written to output.txt")
file1.close()

text = input("\nEnter additional text to append:")
file1 = open("output.txt", "a")
file1.write("\n" + text)
print ("Data successfully appended.")
file1.close()

print("\nFinal content of output.txt:")
file1 = open("output.txt", "r")
reading_file = file1.read()
print(reading_file)

