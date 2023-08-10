students = ["Punit", "Graham", "Alex", "Karen", "Van",
 "Falwinder", "Gurpreet", "Jasper", "Lyle",
 "Nega", "Amandeep", "Pawandeep", "Daman",
 "Pruthviraj", "Beau", "Thilini", "Jashandeep",
 "Ritesh", "Sahilpreet", "Onkar", "Sourav",
 "Harkamalpreet", "Talwinder"]

def invitation(name):
    print(f"""
    
    Dear {name},
We are happy to invite you to our Student Work Exhibition,
happening on Thursday, 21 September 2023,
at the Whitecliffe campus (67 Symonds Street, Auckland)
from 10:00 AM to 1:00 PM.
Join us in celebrating the remarkable achievements of our students
and the outstanding work they've accomplished this term.
We look forward to seeing you at the exhibition!
Best regards,
Ying, Marina, Rashid, John, Pinal """)

for student in students:
    invitation(student)
