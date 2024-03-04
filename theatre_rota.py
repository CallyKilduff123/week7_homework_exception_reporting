from unfilled_position import UnfilledPosition


class TheatreRota:
    def __init__(self):
        # Initialize roles with None to indicate they are initially unassigned
        # the dictionary stores the different roles as keys
        self.roles = {
            'surgeon': None,
            'ward nurse': None,
            'circulating nurse': None,
            'scrub nurse': None,
            'ward clerk': None
        }

    # staff: This is the parameter passed to the method when it's called.
    # It represents a staff member, which is an object created from a class.
    # This object contains at least one attribute, role, which describes the staff member's job or position.

    # Check if the staff's role exists in the rota:
    # This line checks if the role attribute of the staff object exists within the self.roles dictionary.
    # The self.roles dictionary is part of the same class as this method, storing different roles as keys.

    # Assign the staff member to their role:
    # If the staff's role is found in self.roles dictionary, this assigns the staff object to its corresponding role
    # in the dictionary. i.e. that role is filled with the specific staff member provided.
    def assign_staff(self, staff):
        if staff.role in self.roles:
            self.roles[staff.role] = staff
        else:
            return f"Role {staff.role} is not filled."

    # The check_roles method is  to ensure that every role in the self.roles dictionary has been assigned to someone.
    # If any role hasn't been filled (i.e. still None), the method will raise an exception to signal this issue.
    # Otherwise, it confirms that all roles are filled.
    def check_roles(self):
        # This is a list comprehension, a concise way to create a new list.
        # This line creates a list of all the roles that are unfilled.
        # It goes through each item in the self.roles dictionary and checks if the member for each role is None
        # For every role where the member is None, that role's name is added to the empty_roles list.
        empty_roles = [role for role, member in self.roles.items() if member is None]
        if empty_roles:
            # if empty_roles list is True i.e. not empty
            # If there are any empty roles, this line raises an UnfilledPosition exception, signaling an error condition
            # "Empty roles found:" lists the roles in the dictionary that are empty, joining them w/ a comma and space
            raise UnfilledPosition(f"Cataract list cancelled.\nEmpty roles found: {', '.join(empty_roles)}")

        else:
            return "Rota complete. All roles are filled.\nCataract list scheduled."

        # This is a list comprehension, a concise way to create a new list.
        # self.roles.values(): This gets all the values from the self.roles dictionary.
        # It goes through each item in the roles' values, 
        # and it includes the item in the new list only if value is None. 
        # it builds a list of all unassigned (empty) roles.

    def count_empty_roles(self):
        return len([member for member in self.roles.values() if member is None])

    # def count_empty_roles(self):
    #     # Initialise a counter at 0
    #     empty_count = 0
    #
    #     # Iterate over each item in the roles dictionary
    #     for item in self.roles.values():
    #         # Check if the role's value is empty (not filled)
    #         if item is None:
    #             # Increment the counter
    #             empty_count += 1
    #     # Return the total count of empty roles
    #     return empty_count
