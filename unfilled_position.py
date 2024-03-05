class UnfilledPositionException(Exception):
    pass


#  pass is a placeholder - it means do nothing.
#  It is there so that it can be identified by its type when caught in an exception handling block.

# class UnfilledPositionException(Exception):
#     def __init__(self, empty_roles):
#         self.empty_roles = empty_roles
#
#     def get_empty_roles(self):
#         return f"Cataract list cancelled.\nInsufficient staff"

# class UnfilledPositionException(Exception):
#     def __init__(self, unfilled_count, unfilled_role, message="Unfilled roles detected"):
#         self.unfilled_count = unfilled_count
#         super().__init__(f"{message}: {unfilled_count}\n{', '.join(unfilled_role)}")
