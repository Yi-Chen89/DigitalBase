import math


# AISC 360-16 Chapter D -----------------------------------------------------------------------
# DESIGN OF MEMBERS FOR TENSION ---------------------------------------------------------------
def tension_yield(F_y, A_g):
    # AISC 360-16 Chapter D D2 (a)
    phi_t = 0.9
    P_n = F_y * A_g

    return phi_t * P_n

def tension_rupture(F_u, A_e):
    # AISC 360-16 Chapter D D2 (b)
    phi_t = 0.75
    P_n = F_u * A_e

    return phi_t * P_n

def tension(F_y, A_g, F_u, A_e):
    phi_P_n_yeild = tension_yield(F_y, A_g)
    phi_P_n_rupture = tension_rupture(F_u, A_e)

    if phi_P_n_yeild <= phi_P_n_rupture:
        return phi_P_n_yeild
    else:
        return phi_P_n_rupture


# AISC 360-16 Chapter E -----------------------------------------------------------------------
# DESIGN OF MEMBERS FOR COMPRESSION -----------------------------------------------------------
def compression_FB_nonslender(E, F_y, A_g, r, L_c):
    # E3 FLEXURAL BUCKLING OF MEMBERS WITHOUT SLENDER ELEMENTS
    phi_c = 0.9

    F_e = (math.pi**2 * E) / (L_c / r)**2
    if F_y / F_e <= 2.25:
        F_cr = 0.658**(F_y/F_e) * F_y
    else:
        F_cr = 0.877 * F_e

    P_n = F_cr * A_g

    return phi_c * P_n


# AISC 360-16 Chapter F -----------------------------------------------------------------------
# DESIGN OF MEMBERS FOR FLEXURE ---------------------------------------------------------------
def flexure_yielding(F_y, Z_x):
    # Resistance Factor for Flexure, phib
    phi_b = 0.90

    # Calculate Nominal Flexural Strength, Mn
    # (F2-1)
    M_p = F_y * Z_x
    M_n = M_p

    # Return Design Flexural Strength, phib*Mn
    return phi_b * M_n


# AISC 360-16 Chapter G -----------------------------------------------------------------------
# Design of Members for Shear -----------------------------------------------------------------
def shear_web_no_tensionfield(F_y, d, t_w):
    # assume phi_v and C_v1
    phi_v = 1.00
    C_v1 = 1.0

    # Calculate Area of Web, Aw
    A_w = d * t_w

    # Calculate Nominal Shear Strength, Vn
    # (G2-1)
    V_n = 0.6 * F_y * A_w * C_v1

    # Return Design Shear Strength, phiv*Vn
    return phi_v * V_n