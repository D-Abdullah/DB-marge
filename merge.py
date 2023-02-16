# Open the first SQL file and read its contents
with open("eslam.sql", "r") as file1:
    file1_contents = file1.read()

# Open the second SQL file and read its contents
with open("update.sql", "r") as file2:
    file2_contents = file2.read()

# Concatenate the contents of the two files
merged_contents = file1_contents + "\n" + file2_contents

# Write the merged contents to a new file
with open("new.sql", "w") as merged_file:
    merged_file.write(merged_contents)