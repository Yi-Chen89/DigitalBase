export interface SteelType {
  id: number;
  name: string;
}
  
export interface SteelGrades {
  id: number;
  name: string;
}

export interface SteelGrade {
  id: number;
  name: string;
  type: SteelType;
  F_y: number;
  F_u: number;
}

export interface SteelSectionType {
  id: number;
  name: string;
  preferred_steel: SteelGrade;
}

export interface SteelSections {
  id: number;
  name: string;
}

export interface SteelSection {
  id: number;
  type: SteelSectionType;
  name: string;
  W: number;
  A: number;
  d: number;
  b_f: number;
  t_w: number;
  t_f: number;
  k_des: number;
  I_x: number;
  Z_x: number;
  S_x: number;
  r_x: number;
  I_y: number;
  Z_y: number;
  S_y: number;
  r_y: number;
  J: number;
  C_w: number;
  W_no: number;
  S_w1: number;
  Q_f: number;
  Q_w: number;
  r_ts: number;
  h_o: number;
  P_A: number;
  P_B: number;
}