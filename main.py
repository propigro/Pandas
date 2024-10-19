import pandas as pd
teachers = pd.DataFrame({
    "F.I.Sh": ["Xalilov. D. A", "Jalilov .M", "Araboyev . A", "Aloydinov.M", "Qadamova. Z","Jorayeva. G","Xontorayev. S", "Abdullayeva. M", "Turdimatov.M" ],
    "Fan": ["Suniy intlekt asoslari","Kompyuterni tashkil etish","Kibrxavsizlik asoslari", "Kompyuterni tashkil etish", "Suniy intlekt asoslari", "Eliktronika sixemalar", "Malumotlar tuz va algo", "Malumotlar tuz va algo", "Kibrxavsizlik asoslari"],
    "Turi": ["Maruza", "Maruza", "Amaliy","Amaliy","Amaliy","Amaliy, Maruza","Maruza", "Amaliy", "Maruza" ]           
})
print(teachers) #sss
teachers.to_excel("teachers.xlsx")