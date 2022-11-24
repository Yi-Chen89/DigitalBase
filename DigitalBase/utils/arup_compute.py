import arupcomputepy


def arup_compute_tension_yielding(F_y, A_g, jobNumber='07601755'):
    jobNumber = jobNumber
    connection = arupcomputepy.Connection(jobNumber)

    # Yielding
    # Calculate nominal tensile yielding strength

    calcID = 6581591

    variables = {
        'ID': 12345678,
        'F_y': F_y, # Yield strength (ksi)
        'A_g': A_g # Area gross (in^2)
    }

    response = arupcomputepy.MakeCalculationRequest(connection, calcID, isBatch=False, variables=variables, resultType='simple')

    P_n = response['P_nyld']
    
    html_raw = response.arupComputeReport_HTML
    
    html_split = html_raw.split('</style>')
    html_style = html_split[0] + '</style>'
    html = html_split[1]

    return P_n, html_style, html


def arup_compute_flexure_strength(F_y, Z_x, r_y, L_b, S_x, J, h_o, I_y, I_x, b_f, t_f, k_des, d, t_w, jobNumber='07601755'):
    jobNumber = jobNumber
    connection = arupcomputepy.Connection(jobNumber)

    # Flexure Strength
    # Calculates the LRFD moment capacity of doubly symmetric rolled I-shaped members bent about their major axis

    calcID = 6785211

    variables = {
        'ID': 87654321,
        'M_r': 0,
        'F_y': F_y,
        'Z_x': Z_x,
        'r_y': r_y,
        'L_b': L_b,
        'S_x': S_x,
        'C_b': 1,
        'J': J,
        'h_o': h_o,
        'I_y': I_y,
        'I_x': I_x,
        'b_f': b_f,
        't_f': t_f,
        'k_des': k_des,
        'd': d,
        't_w': t_w,
    }

    response = arupcomputepy.MakeCalculationRequest(connection, calcID, isBatch=False, variables=variables, resultType='simple')

    # Available output values:
    M_c = response['M_c'] # Moment capacity (kip-ft)
    U_f = response['U_f'] # Utilization ratio for flexure
    
    html_raw = response.arupComputeReport_HTML
    
    html_split = html_raw.split('</style>')
    html_style = html_split[0] + '</style>'
    html = html_split[1]

    return M_c, html_style, html