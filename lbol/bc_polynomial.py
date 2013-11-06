import constants

def set_coefficients(color_type):
    """Sets the coefficients of the polynomial fit to the proper list
       based on what color the user is supplying

       Args:
           color_type: A string specifying the color combination. Must
               be "BminusV" for B-V, "VminusI" for V-I, or "BminusI" for 
               B-I.
       
       Returns:
           A list containing the coefficients for the polynomial fit which
           correspond to the supplied color, as given in Bersten & Hamuy
           (2009)
       
       Raises:
           TypeError: The argument given is not a string
           ValueError: The argument given is not one of the three valid
               strings.
    """          
    if color_type == "BminusV":
        return constants.coeff_BminusV
    elif color_type == "VminusI":
        return constants.coeff_VminusI
    elif color_type == "BminusI":
        return constants.coeff_BminusI
    elif type(color_type) != str:
        raise TypeError("The argument given is not a string")
    else:
        raise ValueError("The argument given is not a valid color type")


def bc_color(color, coeff, range_min, range_max):
    """Calculates the bolometric correction, using the polynomial fits
       from Bersten & Hamuy (2009)

       Args:
           color: B-V, V-I, or B-I color of the supernova (corrected for
                  reddening and extinction from the host and MWG)
           coeff: polynomial fit coefficients corresponding to the chosen
                  color
           range_min: minimum value of the polynomial's range of validity
                      for the chosen color
           range_max: maximum value of the polynomial's range of validity
                      for the chosen color
       Returns:
           The bolometric correction for use in calculating the bolometric
           luminosity of the supernova, if the color given is within the
           valid range of the polynomial fit.

           None if the color is outside the valid range
    """
    bc_color = 0.0

    if range_min <= color <= range_max:
        for i in range(len(coeff)):
            bc_color += coeff[i] * color**(i)
    else:
        bc_color = None

    return bc_color

class bcColor():

    def __init__(self, color_value, range_minumum, range_maximum):
        self.color_value   = color_value
        self.range_minumum = range_minumum
        self.range_maximum = range_maximum
        self.result        = 0.0

    def calculate_polynomial_fit(self, coefficient_set):
        for order in range(len(coefficient_set)):
            add_term(calculate_term(order, coefficient_set[order]))
        return self.result

    def add_term(self, step):
      self.result += step

    def calculate_term(self, order, coefficient):
      return coefficient * self.color_value**(order)
