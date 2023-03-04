class Plate:
    def __init__(plate, color,metarial,size):
        plate.color = color
        plate.metarial = metarial
        plate.size = size
        plate.clean = True

    def wash(plate):
        if plate.clean == False :
            plate.clean = True
            print(f"{plate.color} {plate.metarial} {plate.size} Plate is clear now.")
        else:
            print(f"{plate.color} {plate.metarial} {plate.size} Plate is already clear.")

    def check_breakage(plate):
        if plate.clean == False:
            print(f"Care! Dirty {plate.color} {plate.metarial} {plate.size} plate is cracked!")
        else:
            print(f"{plate.color} {plate.metarial} {plate.size} Plate is good!")


plate1=Plate("Blue", "Granite", "16inc")

plate1.wash() #plate is cleaning.
plate1.check_breakage() # plate is checking is good or not.