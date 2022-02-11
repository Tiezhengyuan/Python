import re
import requests
import json
import sys


class car:
    url = 'http://localhost:3000/posts'

    def check_server(self) -> bool:
        try:
            response = requests.head(self.url)
            response.raise_for_status()
            return True
        except requests.exceptions.HTTPError as e:
            print("HTTP error: db is not working")
            return False

    def enter_id(self):
    # allows user to enter car's ID and checks if it's valid;
    # valid ID consists of digits only;
    # returns int or None (if user enters an empty line);
        while True:
            cid = input("Car ID: ")
            if cid == "":
                return None
            try:
                cid = int(cid)
                return cid
            except:
                print("warning: cid should be digits.")
    
    def validate_name(self, name) -> bool:
        # checks if name (brand or model) is valid;
        # valid name is non-empty string containing
        # digits, letters and spaces;
        if isinstance(name, str) and re.findall(r"[^\w| ]", name) == []:
            return True
        return False

    def enter_brand(self):
    # allows user to enter car's name (brand or model) and checks if it's valid;
    # uses name_is_valid() to check the entered name;
    # returns string or None  (if user enters an empty line);
    # argument describes which of two names is entered currently ('brand' or 'model');
        while True:
            brand = input("Car brand: ")
            if brand == "":
                return None
            if self.validate_name(brand):
                return brand
            else:
                print("brand should include at least one digit, letter and whitespace")

    def enter_model(self):
        while True:
            model = input("Car model: ")
            if model == "":
                return None
            if self.validate_name(model):
                return model
            else:
                print("model should include at least one digit, letter and whitespace")

    def enter_production_year(self):
    # allows user to enter car's production year and checks if it's valid;
    # valid production year is an int from range 1900..2000;
    # returns int or None  (if user enters an empty line);
        while True:
            yr = input("Car production year (1900-2000): ")
            if yr == "":
                return None
            try:
                yr = int(yr)
                if 1900<= yr <= 2000:
                    return yr
            except:
                print("warning: cid should be digits.")    

    def enter_convertible(self) -> bool:
    # allows user to enter Yes/No answer determining if the car is convertible;
    # returns True, False or None  (if user enters an empty line);
        isconvert = input("Is this car convertible (Y/N):")
        if isconvert == "":
            return None
        elif isconvert in ("y", "Y"):
            return "Y"
        else:
            return "N"

    def input_car_data(self):
    # lets user enter car data;
    # argument determines if the car's ID is entered (True) or not (False);
    # returns None if user cancels the operation or a dictionary of the following structure:
    # {'id': int, 'brand': str, 'model': str, 'production_year': int, 'convertible': bool }
        cid = self.enter_id()
        cbrand = self.enter_brand()
        cmodel = self.enter_model()
        cyear = self.enter_production_year()
        isconvert = self.enter_convertible()
        payload = {"id":cid} if cid else {}
        if cid:
            payload["brand"] = cbrand
        if cmodel:
            payload["model"] = cmodel
        if cyear:
            payload["year"] = cyear
        if isconvert:
            payload["isConvertible"] = isconvert
        return payload

    def get_car(self, cid):
        try:
            response = requests.get(f"{self.url}/{cid}")
            response.raise_for_status()
            car = json.dumps(response.text)
            return car
        except requests.exceptions.HTTPError as e:
            print("HTTP error")
            return None

    def list_cars(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            cars = json.loads(response.text)
            #print("Get list of cars: ", cars)
            return cars
        except requests.exceptions.HTTPError as e:
            print("HTTP error", e.response.status_code)

    def add_car(self):
    # invokes input_car_data(True) to gather car's info and adds it to the database;
        payload = self.input_car_data()
        try:
            response = requests.post(self.url,data=payload)
            response.raise_for_status()
            print(response.status_code)
            print(response.text)
            return True
        except requests.exceptions.HTTPError as e:
            print("HTTP error", e.response.status_code)
            return False

    def delete_car(self):
        # asks user for car's ID and tries to delete it from database;
        cid = input("Enter cid of the car for deletion: ")
        try:
            response = requests.delete(f"{self.url}/{cid}")
            response.raise_for_status()
            return True
        except requests.exceptions.HTTPError as e:
            print("HTTP error: no deletion", e.response.status_code)
            return False

    def update_car(self):
    # invokes enter_id() to get car's ID if the ID is present in the database;
    # invokes input_car_data(False) to gather new car's info and updates the database;
        payload = self.input_car_data()
        cid = payload['id']
        print(payload)
        try:
            response = requests.patch(f"{self.url}/{cid}", data=payload)
            response.raise_for_status()
            return True
        except requests.exceptions.HTTPError as e:
            print("HTTP error: no updates", e.response.status_code)
            return False

    def print_menu(self):
        print("MENU", "=====", sep="\n")
        menu = ['list cars', 'add new car', "delete car", "update car"]
        for i,v in enumerate(menu):
            print(f"{i+1}. {v}")
        print("0. Exist")

    def print_header(self, cars):
        header_format = "{:4s}\t{:8s}\t{:8s}\t{:8s}\t{:8s}"
        print(header_format.format("id", "Brand", 
            "Model", "Year", "Is convertible"))
        for c in cars:
            print(header_format.format(
                str(c.get('id')), str(c.get('brand')), 
                str(c.get('model')), str(c.get('year')),
                str(c.get('isConvertible'))
            ))

    def print_car(self, car):
        # prints one car's data in a way that fits the header;
        self.print_header([car])

    def is_empty(self):
        cars = self.list_cars()
        if len(cars)>0:
            print("Number of cars in database: ", len(cars))
            return True
        else:
            print("*** Database is empty ***")
            return False

    def read_user_choice(self):
        select = -1
        while select == -1:
            self.print_menu()
            select = input("Enter your choice (0..4): ")
            try:
                select = int(select)
            except:
                select = -1
            if select<0 or select>4:
                select = -1
            print
        #self.is_empty()
        return select



if __name__ == "__main__":
    v = car()
    if not v.check_server():
        print("Server is not responding - quitting!")
        sys.exit(1)

    while True:
        choice = v.read_user_choice()
        if choice == 0:
            print("Bye!")
            sys.exit(0)
        elif choice == 1:
            cars = v.list_cars()
            v.print_header(cars)
        elif choice == 2:
            v.add_car()
        elif choice == 3:
            v.delete_car()
        elif choice == 4:
            v.update_car()
