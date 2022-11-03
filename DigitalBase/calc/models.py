from django.db import models



class SteelType(models.Model):
    name = models.CharField(
        max_length = 50)

    def __str__(self):
        return self.name


class SteelGrade(models.Model):
    name = models.CharField(
        max_length = 16)
    type = models.ForeignKey(
        SteelType,
        on_delete = models.CASCADE)
    F_y = models.IntegerField()
    F_u = models.IntegerField()
    E = models.IntegerField()
    
    def __str__(self):
        return self.name


class SteelSectionType(models.Model):
    name = models.CharField(
        max_length = 4)
    preferred_steel = models.ForeignKey(
        SteelGrade,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class SteelSection(models.Model):
    name = models.CharField(
        max_length = 8)
    type = models.ForeignKey(
        SteelSectionType,
        on_delete = models.CASCADE)
    W = models.DecimalField(
        max_digits = 5,
        decimal_places = 2)
    A = models.DecimalField(
        max_digits = 6,
        decimal_places = 3)
    d = models.DecimalField(
        max_digits = 4,
        decimal_places = 2)
    b_f = models.DecimalField(
        max_digits = 4,
        decimal_places = 2)
    t_w = models.DecimalField(
        max_digits = 4,
        decimal_places = 3)
    t_f = models.DecimalField(
        max_digits = 4,
        decimal_places = 3)
    k_des = models.DecimalField(
        max_digits = 4,
        decimal_places = 3)
    I_x = models.DecimalField(
        max_digits = 6,
        decimal_places = 1)
    Z_x = models.DecimalField(
        max_digits = 6,
        decimal_places = 2)
    S_x = models.DecimalField(
        max_digits = 6,
        decimal_places = 2)
    r_x = models.DecimalField(
        max_digits = 4,
        decimal_places = 2)
    I_y = models.DecimalField(
        max_digits = 6,
        decimal_places = 2)
    Z_y = models.DecimalField(
        max_digits = 5,
        decimal_places = 2)
    S_y = models.DecimalField(
        max_digits = 5,
        decimal_places = 2)
    r_y = models.DecimalField(
        max_digits = 4,
        decimal_places = 3)
    J = models.DecimalField(
        max_digits = 8,
        decimal_places = 4)
    C_w = models.DecimalField(
        max_digits = 8,
        decimal_places = 1)
    W_no = models.DecimalField(
        max_digits = 5,
        decimal_places = 2)
    S_w1 = models.DecimalField(
        max_digits = 6,
        decimal_places = 2)
    Q_f = models.DecimalField(
        max_digits = 5,
        decimal_places = 2)
    Q_w = models.DecimalField(
        max_digits = 6,
        decimal_places = 2)
    r_ts = models.DecimalField(
        max_digits = 4,
        decimal_places = 3)
    h_o = models.DecimalField(
        max_digits = 4,
        decimal_places = 2)
    P_A = models.DecimalField(
        max_digits = 4,
        decimal_places = 1)
    P_B = models.DecimalField(
        max_digits = 4,
        decimal_places = 1)

    def __str__(self):
        return self.name