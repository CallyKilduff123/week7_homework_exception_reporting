from people.person import Person


class Staff(Person):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role

