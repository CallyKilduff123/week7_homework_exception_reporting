from theatre_rota import TheatreRota
from unfilled_position import UnfilledPosition
from people.staff import Staff

# Create some staff members
surgeon = Staff("Dr. Hobnob", "surgeon")
ward_nurse = Staff("Nurse Jammy", "ward nurse")
scrub_nurse = Staff("Nurse Dodger", "scrub nurse")
ward_clerk = Staff("Mrs Jaffacake", "ward clerk")
circulating_nurse = Staff("Nurse Custard-Cream", "scrub nurse")
# circulating_nurse = Staff("Nurse Bourbon", "circulating nurse")

# Additional staff members as needed...

# Initialize the CataractList
staff_rota = TheatreRota()
vacant_position = UnfilledPosition

# Assign staff to roles
staff_rota.assign_staff(surgeon)
staff_rota.assign_staff(ward_nurse)
staff_rota.assign_staff(scrub_nurse)
staff_rota.assign_staff(ward_clerk)
staff_rota.assign_staff(circulating_nurse)


# Check for any empty roles and count them
try:
    print(staff_rota.check_roles())
except vacant_position as e:
    print(e)

print(f"Number of empty roles: {staff_rota.count_empty_roles()}")