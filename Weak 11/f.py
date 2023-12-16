import numpy as np

# Create a dictionary for Ali's course marks
ali_marks = {
    'Math': {'total': 100, 'obtained': 90},
    'Physics': {'total': 100, 'obtained': 85},
    'Chemistry': {'total': 100, 'obtained': 92},
    'Biology': {'total': 100, 'obtained': 88}
}

# Save the dictionary to a text file
text_file_path = 'ali_marks.txt'
with open(text_file_path, 'w') as text_file:
    for course, marks in ali_marks.items():
        text_file.write(f"{course}: {marks['obtained']} out of {marks['total']}\n")

# Save the dictionary to a NumPy binary file
numpy_file_path = 'ali_marks.npy'
np.save(numpy_file_path, ali_marks)

# Print the saved paths
print(f"Text file saved to: {text_file_path}")
print(f"NumPy file saved to: {numpy_file_path}")
