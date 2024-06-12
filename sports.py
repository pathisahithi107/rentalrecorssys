#sports equipment rental records system
class Equipment:
    def __init__(self, equipment_id, name, condition):
        self.equipment_id = equipment_id
        self.name = name
        self.condition = condition

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

class RentalRecord:
    def __init__(self, record_id, equipment, student, rental_date, return_date=None):
        self.record_id = record_id
        self.equipment = equipment
        self.student = student
        self.rental_date = rental_date
        self.return_date = return_date

class EquipmentRentalSystem:
    def __init__(self):
        self.equipments = {}
        self.students = {}
        self.rental_records = {}
        self.next_equipment_id = 1
        self.next_student_id = 1
        self.next_record_id = 1

    # CRUD operations for Equipment
    def add_equipment(self, name, condition):
        equipment_id = self.next_equipment_id
        self.next_equipment_id += 1
        equipment = Equipment(equipment_id, name, condition)
        self.equipments[equipment_id] = equipment
        return equipment

    def get_equipment(self, equipment_id):
        return self.equipments.get(equipment_id)

    def update_equipment(self, equipment_id, name=None, condition=None):
        equipment = self.equipments.get(equipment_id)
        if equipment:
            if name:
                equipment.name = name
            if condition:
                equipment.condition = condition
            return equipment
        return None

    def delete_equipment(self, equipment_id):
        return self.equipments.pop(equipment_id, None)

    # CRUD operations for Students
    def add_student(self, name):
        student_id = self.next_student_id
        self.next_student_id += 1
        student = Student(student_id, name)
        self.students[student_id] = student
        return student

    def get_student(self, student_id):
        return self.students.get(student_id)

    def update_student(self, student_id, name):
        student = self.students.get(student_id)
        if student:
            student.name = name
            return student
        return None

    def delete_student(self, student_id):
        return self.students.pop(student_id, None)

    # Rental Operations
    def rent_equipment(self, equipment_id, student_id, rental_date):
        equipment = self.equipments.get(equipment_id)
        student = self.students.get(student_id)
        if equipment and student:
            record_id = self.next_record_id
            self.next_record_id += 1
            rental_record = RentalRecord(record_id, equipment, student, rental_date)
            self.rental_records[record_id] = rental_record
            return rental_record
        return None

    def return_equipment(self, record_id, return_date, condition):
        rental_record = self.rental_records.get(record_id)
        if rental_record:
            rental_record.return_date = return_date
            rental_record.equipment.condition = condition
            return rental_record
        return None

    def get_rental_record(self, record_id):
        return self.rental_records.get(record_id)

# Example usage
if __name__ == "__main__":
    system = EquipmentRentalSystem()

    # Add equipment
    equipment1 = system.add_equipment("Basketball", "New")
    equipment2 = system.add_equipment("Soccer Ball", "Used")

    # Add student
    student1 = system.add_student("John Doe")
    student2 = system.add_student("Jane Smith")

    # Rent equipment
    rental1 = system.rent_equipment(equipment1.equipment_id, student1.student_id, "2024-06-01")
    rental2 = system.rent_equipment(equipment2.equipment_id, student2.student_id, "2024-06-02")

    # Return equipment
    returned1 = system.return_equipment(rental1.record_id, "2024-06-10", "Used")

    # Print rental records
    for record in system.rental_records.values():
        print(f"Record ID: {record.record_id}, Equipment: {record.equipment.name}, Student: {record.student.name}, Rental Date: {record.rental_date}, Return Date: {record.return_date}, Condition: {record.equipment.condition}")