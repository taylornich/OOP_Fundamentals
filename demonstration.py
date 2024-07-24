from vehicle import Vehicle

def main():
    car1 = Vehicle("D04FS1", "Truck", "Ted Mosby")
    car2 = Vehicle("CQR34J", "Sedan", "Barney Stinson")

    car2.update_owner("Blitz Doe")
    print(f"Vehicle 1 has not changed: Registration Number: {car1.registration_number}, Type: {car1.type}, Owner: {car1.owner}")
    print(f"Updated vehicle 2: Registration Number: {car2.registration_number}, Type: {car2.type}, Owner: {car2.owner}")


if __name__ == "__main__":
    main()