
# Lightning Discharge Modeling

This repository contains a Python implementation for modeling atmospheric discharge currents based on the equation:

\[
i(t) = Amp \times \left( e^{At} - e^{Bt} \right)
\]

## Overview

The equation above is commonly used in the modeling of lightning discharges. It describes the current \( i(t) \) at a given time \( t \), where:

- \( Amp \) is the peak amplitude of the current,
- \( A \) and \( B \) are constants that define the behavior of the exponential decay and rise of the current.

The current follows a typical lightning discharge profile, which starts with a rapid increase in current followed by an exponential decay. The constants \( A \) and \( B \) are crucial to capturing this behavior, and their accurate determination is essential for realistic simulations.

## Code Description

This Python code calculates the constants \( A \) and \( B \) and adjusts the peak current based on the provided input values for the time of the peak current \( t_{pico} \), half-life \( t_{meia} \), and the peak current \( i_{pico} \). The calculation is done iteratively to achieve a precise match for the desired discharge characteristics.

### Key Components:

- **`CalcAB(iPico, tPico, tMetade, amp)`**:
  This function calculates the constants \( A \), \( B \), and the time \( t_p \) when the current reaches its peak.

- **Iterative Adjustment**:
  The peak time \( t_p \) is adjusted iteratively to refine the values of \( A \) and \( B \) until the desired precision is achieved.

### Example Usage:

```python
def main():
    tPico = 1.2e-6  # Peak time in seconds
    tMetade = 50e-6  # Half-life in seconds
    iPico = 10000  # Peak current in amperes
    
    amp0 = iPico * 1.02  # Initial guess for the amplitude
    A, B, tp = CalcAB(iPico, tPico, tMetade, amp0)
    
    while abs(tp - tPico) / tPico > 1e-4:
        tPicoAjust *= tPico / tp
        A, B, tp = CalcAB(iPico, tPicoAjust, tMetade, amp0)
    
    print(f'Amp = {amp0:.0f}\nA = {A:.0f}\nB = {B:.0f}')
```

This script allows you to compute the values of \( A \) and \( B \) iteratively, ensuring an accurate model of the lightning current over time.

## Credits

This program was originally presented by **Thales Lima de Oliveira** during a class available on YouTube, which you can watch [here](https://youtu.be/UyKbuHZT-eI?si=w3ZbA-HtUhxSS8tB). Thales developed this solution to model the current of a lightning discharge and provided valuable insights into its application during the class.
