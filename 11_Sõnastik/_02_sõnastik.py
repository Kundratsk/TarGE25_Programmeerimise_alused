from _01_Sõnastik import est_eng_dict, est_ita_dict


est_ita_dict["üks"] = "uno"
est_eng_dict["kolm"] = "three"
est_eng_dict["üks"] = "one"
est_ita_dict["kolm"] = "tre"



if __name__ == '__main__':
    print(f"Tere -> inglise keeles: {est_eng_dict ["tere"]}, itaalia keeles: {est_ita_dict ["tere"]}")
    print(f"auto -> itaalia keeles: {est_ita_dict ["auto"]}")
    print(f"kass -> inglise keeles: {est_eng_dict ["kass"]}")
    print(f"üks -> itaalia keeles: {est_ita_dict ["üks"]}")
    print(f"Kolm -> inglise keeles: {est_eng_dict ["kolm"]}")

