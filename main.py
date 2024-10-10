# Author: Thales Lima Oliveira ©2023

import math
import numpy as np


# Function to calculate the constants A, B, and tp (peak time) based on the input parameters
def CalcAB(iPico, tPico, tMetade, amp):
    # Calculate B using logarithmic expression based on the peak current (iPico) and peak time (tPico)
    B = math.log(1.0 - iPico / amp) / tPico

    # Calculate exponential of B * tMetade
    ebtm = math.exp(B * tMetade)

    # Calculate A using logarithmic expression involving iPico, amp, and ebtm
    A = math.log(iPico / (2 * amp) + ebtm) / tMetade

    # Calculate tp (peak time) using logarithmic expression involving A and B
    tp = math.log(B / A) / (A - B)

    # Return the calculated values of A, B, and tp
    return A, B, tp


def main():
    # Initial conditions for tPico (peak time), tMetade (half-life), and iPico (peak current)
    tPico = 1.2e-6  # in seconds
    tMetade = 50e-6  # in seconds
    iPico = 10000  # in amperes

    # Initial guess for the peak amplitude (Amp0)
    amp0 = iPico * 1.02

    # Calculate the initial values of A, B, and tp using the CalcAB function
    A, B, tp = CalcAB(iPico, tPico, tMetade, amp0)

    # Adjusted peak time for iterations
    tPicoAjust = tPico

    # Iterative process to refine the values of A, B, and tp
    while abs(tp - tPico) / tPico > 1e-4:
        # Adjust the peak time in each iteration
        tPicoAjust *= tPico / tp

        # Recalculate A, B, and tp based on the adjusted tPicoAjust
        A, B, tp = CalcAB(iPico, tPicoAjust, tMetade, amp0)

    # Print the final results for Amp, A, and B
    print(f'Amp = {amp0:.0f}\nA = {A:.0f}\nB = {B:.0f}')


if __name__ == "__main__":
    main()
