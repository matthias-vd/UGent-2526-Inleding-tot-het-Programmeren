def calculate_current_ratio(vlottende_activa, vorderingen_meer_dan_1_jaar, schulden_ten_hoogste_1_jaar, overlopende_rekeningen_passiva):
    teller = vlottende_activa - vorderingen_meer_dan_1_jaar
    noemer = schulden_ten_hoogste_1_jaar + overlopende_rekeningen_passiva
    ratio = round(teller / noemer, 2)
    return f"De current ratio van de onderneming bedraagt: {ratio}"

def calculate_acid_test_ratio(vlottende_activa, vorderingen_meer_dan_1_jaar, schulden_ten_hoogste_1_jaar, voorraden_en_bestellingen):
    teller = vlottende_activa - vorderingen_meer_dan_1_jaar - voorraden_en_bestellingen
    noemer = schulden_ten_hoogste_1_jaar
    acid = round(teller / noemer, 2)
    return f"De acid test ratio van de onderneming bedraagt: {acid}"