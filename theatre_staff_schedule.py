from theatre_rota import TheatreRota
from unfilled_position import UnfilledPositionException
from people.staff import Staff

staff_rota = TheatreRota()
vacant_position = UnfilledPositionException

surgeon = Staff("Dr. Hobnob", "surgeon")
ward_nurse = Staff("Nurse Jammy", "ward nurse")
scrub_nurse = Staff("Nurse Dodger", "scrub nurse")
ward_clerk = Staff(None, None)
# ward_clerk = Staff("Mrs Jaffacake", "ward clerk")
circulating_nurse = Staff("Nurse Custard-Cream", "scrub nurse")
# circulating_nurse = Staff("Nurse Bourbon", "circulating nurse")

try:
    # Assign staff to roles
    staff_rota.assign_staff(surgeon)
    staff_rota.assign_staff(ward_nurse)
    staff_rota.assign_staff(scrub_nurse)
    staff_rota.assign_staff(ward_clerk)
    staff_rota.assign_staff(circulating_nurse)
    print(staff_rota.check_roles())
    # staff_rota.check_and_raise_for_unfilled_roles()
except UnfilledPositionException as ex:
    # print(f"Cataract list cancelled.\nNumber of empty roles: {staff_rota.count_empty_roles()}")
    print(ex)
    print(f"Number of empty roles: {staff_rota.count_empty_roles()}")
finally:
    print("Rota check complete")

# except UnfilledPositionException as ex:
#     print(f"Cataract list cancelled.\nNumber of empty roles: {staff_rota.count_empty_roles()}")
#     print(ex)
# finally:
#     print("Rota check complete")
