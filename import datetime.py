import datetime

class Appointment:
    def __init__(self, day, start_hour, client_name, client_phone, appointment_type):
        self.day = day
        self.start_hour = start_hour
        self.client_name = client_name
        self.client_phone = client_phone
        self.appointment_type = appointment_type
        
        class AppointmentManager:
            def __init__(self):
                self.appointments =[]
                
                def schedule_appointment(self, day, start_hour, client_name, client_phone, appointment_type):
                    appointment = Appointment(day, start_hour, client_name, client_phone, appointment_type)
                    self.appointments.append(appointment)
                    print(f"OK, {client_name}'s appointment is scheduled!")
                    
                    def display_menu(self):
                        print("Jojo's Hair Salon Appointment Manager")
                        print("1) Schedule an appointment")
                        print("2) Find appointment by name")
                        print("3) Print calendar for a specific day")
                        print("4) Cancel an appointment")
                        print("9) Exit the system")
                        
                        def run(self):
                            while True:
                                self.display_menu()
                                selection = input("Enter your selection: ")
                                if selection =='1':
                                    day = input("What day: ")
                                    int(input("Enter start hour (24 hour clock): "))
                                    client_name = input("Client Name: ")
                                    client_phone = input("Client Phone: ")
                                    print("Appointment types\n1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120")
                                    appointment_type = int(input("Type of Appointment: "))
                                    
                                    self.schedule_appointment(day, start_hour, client_name, client_phone, appointment_type)
                                elif selection =='9':
                                    print("Existing the system.")
                                    break
                                
                                if __name__ == "__main__":
                                    salon_manager = AppointmentManager()
                                    salon_manager.run()
                                    
                                    class AppointmentManager:
                                        
                                        def print_calendar_for_day(self, day):
                                            print(f"Appointments for {day.capitalise()}")
                                            print("{:<20} {:<15} {:<5} {:<5} {:<5} {:<10}". format("Client Name", "Phone", "Day", "Start", "End", "Type"))
                                            for appointment in self.appointments:
                                                if appointment.day.lower() == day.lower():
                                                    print("{:<20} {:<15} {:<5} {:<5} {:<5} {:<10}".format(
                                                         appointment.client_name,
                                                         appointment.client_phone,
                                                         appointment.day,
                                                         
                                                         appointment.start_hour,
                                                         appointment.start_hour + 1,
                                                         appointment.appointment_type))
                                        def run(self):
                                            while True:
                                                self.display_menu()
                                                selection = input("Enter your selection: ")
                                        if selection == '1':
                                            day = input("Enter day of week: ")
                                            self.print_calendar_for_day(day)
                                            
                                        elif selection =='3':
                                            day = input("Enter day of week: ")
                                            self.print_calendar_for_day(day)
                                            
                                        elif selection == '9':
                                            print("Existing the system.")
                                        
                                        if __name__ == "__main__":
                                            salon_manager = AppointmentManager()
                                            salon_manager.run()                                                        