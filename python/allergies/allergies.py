allergies  = {'eggs': 1, 'peanuts': 2, 'shellfish': 4, 
    'strawberries': 8, 'tomatoes': 16, 'chocolate': 32, 
    'pollen': 64, 'cats': 128}

class Allergies(object):



    def __init__(self, score=0):
        self.score = score
        self.personal_allergy = []
        

    def is_allergic_to(self, item):
        message = "Charles isn't allergic to anything"

        if item in allergies:
            self.personal_allergy.append(item)
            self.score += allergies[item]
            message = "Charles is allergic to: {} with a score of: {}".format(self.personal_allergy, self.score)
        
        return message

    def give_allergen_score(self, allergen):
        res = []
        sorted_allergy_val = sorted(allergies.values(), reverse=True)
        for x in sorted_allergy_val:
            if allergen >= x:
                allergen = x - allergen
                res.append(x)
        return res
        

if __name__ == "__main__":
    x = Allergies()
    print(x.give_allergen_score(128))
    # x.is_allergic_to("peanuts")
    # print(x.is_allergic_to("chocolate"))
    # print(x.is_allergic_to("tomatoes"))
    

    # print(x.is_allergic_to("eggs"))
    

