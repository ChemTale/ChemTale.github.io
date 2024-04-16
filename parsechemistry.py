import re

found = re.findall(r'\b([A-Z][a-z]{0,2}\d{0,3})+', 'Pure copper occurs rarely in nature. Usually found in sulfides as in chalcopyrite (CuFeS2), coveline (CuS), chalcosine (Cu2S) or oxides like cuprite (Cu2O).')
print(found)