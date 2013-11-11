from lbol.bc_polynomial import calc_bolometric_correction as bc
import lbol.constants as constants
import math

def calc_log_Fbol(color_value, color_type, v_magnitude):
    """Calculates the log10 of the bolometric flux of a Type II-P supernova.

    Args:
        color_value: B-V, V-I, or B-I color of the supernova in 
            magnitudes (corrected for reddening and extinction from 
            the host and MWG)
        color_type: String signifying which color color_value represents.
            Valid values are "BminusV" for B-V, "VminusI" for V-I, and
            "BminusI" for B-I.
        v_magnitude: Photometric magnitude in the V band, corrected for
            host + MWG extinction

    Returns:
        The base-10 logarithm of the bolometric flux used when calculating
        the bolometric luminosity.

        None if the bolometric correction calculated from the color_value
        and color_type is None (which means the observed color is outside
        the range of validity of the polynomial fit.)
    """ 
    bolometric_correction = bc(color_value, color_type)

    if bolometric_correction == None:
        log_Fbol = None
    else:
        log_Fbol = -0.4 * (bolometric_correction + v_magnitude
                       + constants.mbol_zeropoint)
    
    return log_Fbol

def calc_log_4piDsquared(distance):
    """Calculates the log10 of 4*pi*D^2, the proportionality between
       luminosity and flux. Distance is assumed to be in centimeters

    Args:
        distance: The distance to the supernova in centimeters

    Returns:
        The base-10 logarithm of 4*pi*D^2
    """
    log_4piDsquared = math.log(4.0 * math.pi * distance**2.0, 10)
    
    return log_4piDsquared

def calc_log_Lbol(color_value, color_type, v_magnitude, distance):
    """Calculates the bolometric luminosity of a Type II-P Supernova using
       the method of Bersten & Hamuy (2009)

    Args:
        color_value: B-V, V-I, or B-I color of the supernova in 
            magnitudes (corrected for reddening and extinction from 
            the host and MWG)
        color_type: String signifying which color color_value represents.
            Valid values are "BminusV" for B-V, "VminusI" for V-I, and
            "BminusI" for B-I.
        v_magnitude: Photometric magnitude in the V band, corrected for
            host + MWG extinction
        distance: The distance to the supernova in centimeters
 
    Returns:
        The value of the base-10 logarithm of the bolometric luminosity in
        ergs per second

        None if the bolometric correction is None (which means the      
        observed color value is outside the range of vaidity of the 
        polynomial fit used to determine the bolometric correction.)

    """
    log_Fbol = calc_log_Fbol(color_value, color_type, v_magnitude)
    log_4piDsquared = calc_log_4piDsquared(distance)
    
    if log_Fbol == None:
        log_Lbol = None
    else:
        log_Lbol = log_Fbol + log_4piDsquared

    return log_Lbol
