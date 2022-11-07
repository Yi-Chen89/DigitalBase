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
    
    html_script = '<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script><script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>'
    
    html_split = html_raw.split('</style>')
    html_style = html_split[0] + '</style>'
    html = html_split[1]

    return P_n, html_script, html_style, html