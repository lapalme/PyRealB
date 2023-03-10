from pyrealb import *
from test import test


def elision_en():
    loadEn()
    
    elisionTestsEn=[
        [NP(D("a"),N("apple")),"an apple"],
        [CP(C("or"),NP(D("a"),N("elevator")),NP(D("a"),N("eucalyptus"))),
           "an elevator or a eucalyptus"],
        [CP(C("and"),NP(D("a"),N("one"),N("way")),
                     NP(D("a"),N("overpass"))),"a one way and an overpass"],
        [S(VP(V("eat"),NP(D("a"),N("apple").tag("a",{"href":'https:en.wikipedia.org/wiki/Apple'})))),
         "Eats an <a href=\"https:en.wikipedia.org/wiki/Apple\">apple</a>. "],
        [NP(NO(123),N("man")).tag("i").tag("p"),"<p><i>123 men</i></p>"],
        [NP(D("a").b("@@").cap(),N("elevator").tag("p")),"@@An <p>elevator</p>"],
        [CP(C("and"),NP(D("a"),N("unicorn")),
                     NP(D("a"),A("unusual"),N("exercise")),
                     NP(D("a"),A("honourable"),N("mention")),
                     NP(D("a"),A("humorous"),N("guy"))),
         "a unicorn, an unusual exercise, an honourable mention and a humorous guy"],
        [S(Pro("this"),VP(V("be"),
                          NP(D("a"),"XML",N("exercise"),
                             SP(Pro("that"),
                                NP(D("a").tag("b"),N("educator")).tag("i"),
                                VP(V("give")).typ({"mod":"poss"}))))),
         "This is an XML exercise that <i><b>an</b> educator</i> can give. "],
        [S(VP(V("play").t("ip"),
              NP(D("a"),A("musical"),N("note"),V("name").t("pp"),Q("A")).tag("a",{"href":'https:en.wikipedia.org/wiki/A_(musical_note)'}),
              PP(P("on"),NP(D("a"),N("oboe"))),
              PP(P("for"),VP(V("tune").t("pr"),NP(D("a"),N("orchestra")))))),
         "Play <a href=\"https:en.wikipedia.org/wiki/A_(musical_note)\">a musical note named A</a> on an oboe for tuning an orchestra. "],
        [Q("&"),"&"]
    ]
    
    tests=[{}]
    for exp,expected in elisionTestsEn:
        tests.append({
            "expression":exp,
            "expected":expected,
            "message":f"elision in {expected}"
        })
    return tests
    
if __name__ == '__main__':
    test("English dates","en",elision_en)
