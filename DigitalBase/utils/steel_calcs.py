# AISC 360-16 Chapter D -----------------------------------------------------------------------
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