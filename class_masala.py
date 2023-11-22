# Book klass
# xususiyatlari: nomi, aftir, pages, narx, book_id 
# methods: get_name(), get_narx(), get_info(), get_id()


# University klass
# xususiyatlari: name, fakultet, students, teachers, address
# methods: get_name_fakultet(), get_all_students(), 
# get_teachers(), get_address()

class University:
    def __init__(self, name, fakultet, students, teachers, address):
        self.name = name

    def get_name_fakultet(self):
        return f"{self.name} {self.fakultet}"










