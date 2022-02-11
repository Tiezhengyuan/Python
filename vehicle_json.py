import json

class Vehicle:
    def __init__(self):
        self._car = {
            "registration_number": '',
            "year_of_production": 0,
            "passenger": True,
            "mass": 0
        }
        
    @property
    def reg(self):
        return self._car["registration_number"]
    @reg.setter
    def reg(self, reg):
        self._car["registration_number"] = reg

    @property
    def yr(self):
        return self._car["year_of_production"]
    @yr.setter
    def yr(self, yr):
        self._car["year_of_production"] = yr
        
    @property
    def passenger(self):
        return self._car["passenger"]
    @passenger.setter
    def passenger(self, p):
        if p in ("Y", "y"):
            self._car["passenger"] = True
        else:
            self._car["passenger"] = False
        
    @property
    def mass(self):
        return self._car["mass"]
    @mass.setter
    def mass(self, mass):
        self._car["mass"] = mass
        
    def get_json_str(self):
        self.reg = input("Registration number: ")
        self.yr = input("Year of production: ")
        self.passenger = input("Passenger [y/n]: ")
        self.mass = input("vehicle mass: ")
        print("Resulting JSON string is: ", json.dumps(self._car))
        return json.dumps(self._car)
    
    def decode_json_str(self):
        v_str = input("Enter vehicle JSON string: ")
        print(v_str)
        self._car = json.loads(v_str)
        print(self._car)
        return self._car

if __name__ == "__main__":
    print("What can I do for your?")
    print("1- produce a JSON string describing a vehicle")
    print("2- decode a JSON string into vehicle data")
    task = input('Your choice: ')
    if task == '1':
        Vehicle().get_json_str()
    elif task == "2":
        Vehicle().decode_json_str()
    print("Done")

#{"registration_number":45433,"year_of_production":2009,"passenger":false,"mass":234}