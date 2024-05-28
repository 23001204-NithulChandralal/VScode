"""
Write a main program that reads a wavelength and calls a function with 
the wavelength as a parameter. The function returns the result which is 
displayed by the main program.
"""
"""
program that reads a wavelength and reports its colour.
"""
def main():
    wavelength = int(input("Enter the wavelength :"))
    if wavelength >= 380 and wavelength < 450 :
        print("Violet")
    elif wavelength >= 450 and wavelength < 495:
        print ("Blue")
    elif wavelength >= 495 and wavelength < 570:
        print ("Green")
    elif wavelength >= 570 and wavelength < 590:
        print ("Yellow")
    elif wavelength >= 590 and wavelength < 620:
        print ("Orange")
    elif wavelength >= 620 and wavelength < 750:
        print ("Red")
    else:
        print ("Wavelength entered is outside of the spectrum")
    
    
main()

