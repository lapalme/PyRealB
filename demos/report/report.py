#  simple demonstration of using pyrealb for generating English and French texts
#  from a single structure
#  This is a simplistic approach, but it illustrates some bilingual features of pyrealb
#  Two methods are used
#    - with word dictionaries indexed by language for cases where
#      the phrase structure are strictly parallel
#    - with a basic realizer and two language specific subclasses
#      which allows different phrase structure in both languages

from datetime import datetime,timedelta
from pyrealb import *

from English import English
from Francais import Francais

# add names to the English and French lexica
for loadF in [loadEn,loadFr]:
    loadF()
    addToLexicon({"Alice":{ "N": { "g": "f", "tab": "nI" } }})
    addToLexicon({"Bob":{ "N": { "g": "m", "tab": "nI" } }})
    addToLexicon({"Eve":{ "N": { "g": "f", "tab": "nI" } }})

# text parameterization with words dictionaries indexed by language
participants = ["Alice", "Eve", "Bob"]
conj         = {"en":"and",     "fr":"et"}
prep         = {"en":"at",      "fr":"à"}
det          = {"en":"a",       "fr":"un"}
copula       = {"en":"be",       "fr":"être"}
attribute    = {"en":"present",  "fr":"présent"}
individual   = {"en":"person",   "fr":"personne"}
dateOptions  = {"minute":False,"second":False}

# compare day of date with the day of the reference
def tense(date, reference):
    o = date.toordinal()
    ref_o = reference.toordinal()
    return "p" if o == ref_o else "f" if o > ref_o else "ps"

def report(event, persons, date, lang):
    loadEn() if lang=="en" else loadFr()
    meeting = PP(P(prep[lang]), NP(D(det[lang]),N(event)))
    return S(CP(C(conj[lang]), [N(person) for person in persons]),
             NP(NO(len(persons)).nat(), N(individual[lang])).ba("("),  # show number of persons
             VP(V(copula[lang]),
                A(attribute[lang]),
                meeting,
                DT(date).dOpt(dateOptions)).t(tense(date,today)))

if __name__ == "__main__":
    today = datetime.today()
    loadEn(); print(DT(today).dOpt(dateOptions).realize(),end="")
    loadFr();print("-",DT(today,"fr").dOpt(dateOptions).realize(),"\n")
    for (i,day) in zip(range(1,len(participants)+1),
                       [today-timedelta(days=1),today,today+timedelta(days=1)]):
        print(report("assembly",participants[:i], day,"en").realize())
        print(report("réunion",participants[:i], day,"fr").realize())
        print("--")
        # # use Realizer subclasses on the reversed lists
        # English().report(participants[::-1][:i],day)
        # Francais().report(participants[::-1][:i], day)
        # print("====")


'''  output:
on Tuesday, September 26, 2023 at 5 p.m.- le mardi 26 septembre 2023 à 17 h 

Alice (one person) was present at an assembly on Monday, September 25, 2023 at 5 p.m.
Alice (une personne) fut présente à une réunion le lundi 25 septembre 2023 à 17 h. 
--
Alice and Eve (two persons) are present at an assembly on Tuesday, September 26, 2023 at 5 p.m.
Alice et Eve (deux personnes) sont présentes à une réunion le mardi 26 septembre 2023 à 17 h. 
--
Alice, Eve and Bob (three persons) will be present at an assembly on Wednesday, September 27, 2023 at 5 p.m.
Alice, Eve et Bob (trois personnes) seront présents à une réunion le mercredi 27 septembre 2023 à 17 h. 
--
'''