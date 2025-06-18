with open('hospital.txt', 'r') as file:
    lines = file.readlines() 

hospital_names = []

medical_college_contact = None

for line in lines:
    parts = [part.strip() for part in line.strip().split('|')]

    if len(parts) >= 2:
        hospital_names.append(parts[1])

    if 'medical college' in line.lower():
        medical_college_contact = parts[-1]

print("Hospital Names:")
for name in hospital_names:
    print("-", name)

if medical_college_contact:
    with open('contact.txt', 'w') as contact_file:
        contact_file.write(medical_college_contact)
    print(f"\nThe contact number for 'Medical College'has been saved to contact.txt")

