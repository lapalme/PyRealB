from pyrealb import *
from test import test

# exemples tirées du livre "Application de la réécriture de graphes au traitement automatique des langues"
#                           Guillaume Bonfante, Bruno Guillaume, Guy Perrier, ISTE éditions 2018
#     Chapitre 2: Syntaxes en dépendances: syntaxe de surface et syntaxe profonde
# nous avons choisi celles qui nous semblaient être des "défis" et certaines le furent...
# Les exemples en anglais et en français ont été séparés en deux fonctions ici.
# voici un modèle d'expression pour en ajouter de nouveaux
"""
        # N
        {"expression":
            root(),
         "expected":"",
         "message":" Figure ii p jj / REM:"},
"""
def bonfante_fr_ex():
    loadFr()
    return [
        {},  # dummy 0
        # 1
        {"expression":
             S(NP(D("le"),
                  N("conférence"),
                  A("intergouvernemental")),
               VP(V("tenter"),
                  PP(P("de"),
                     VP(V("répondre").t("b"),
                        Adv("précisément"),
                        PP(P("à"),
                           NP(D("ce"),
                              N("question")))))))            ,
         "expected":"La conférence intergouvernementale tente de répondre précisément à cette question. ",
         "message":" Figure 2.1 p 45 / REM: NP,AP et VP sont 'condensés'"},
        # 2
        {"expression":
             root(V("tenter"),
                  subj(N("conférence"),
                       det(D("le")),
                       mod(A("intergouvernemental"))),
                  comp(P("de"),
                       comp(V("répondre").t('b'),
                            mod(Adv("précisément")),
                            comp(P("à"),
                                 mod(N("question"),
                                     det(D("ce"))))))),
         "expected":"La conférence intergouvernementale tente de répondre précisément à cette question. ",
         "message":"Figure 2.2 p 46"},
        # 3
        {"expression":
            coord(C("et"),
                  root(V("convoquer"),
                       subj(N("directeur"),
                            det(D("le"))),
                       comp(N("conseil"),
                            det(D("le")))),
                  root(V("proposer"),
                       comp(N("plan"),
                            det(D("un"))),
                       comp(P("à"),
                            comp(N("conseil"),
                                 det(D("un")))).pro())).t("f"),
         "expected":"Le directeur convoquera le conseil et lui proposera un plan. ",
         "message":" Exercice 2.4 p 48"},
        # 4
        {"expression":
            root(V("être").t("f"),
                 coord(C("et"),
                       subj(N("curé"),
                            det(D("le"))),
                       subj(N("maire"),
                            det(D("le")),
                            comp(P("de"),
                                mod(N("village"),
                                det(D("le")))))).a(","),
                 mod(Adv("demain")).a(",").pos("pre"),
                 mod(A("présent"),
                     comp(P("à"),
                          comp(N("cérémonie"),
                               det(D("le")))))),
         "expected":"Le curé et le maire du village, demain, seront présents à la cérémonie. ",
         "message":" Exercice 2.6 p 48"},
        # 5
        {"expression":
             root(V("demander").t("pc").aux("êt"),
                  subj(Pro("lui").c("nom")),
                  mod(Pro("vous").c("dat")),
                  comp(P("de"),
                       comp(V("régler").t("b"),
                            comp(N("problème"),
                                 det(D("le")))))),
         "expected":"Il vous est demandé de régler le problème. ",
         "message":" Figure 2.11 p 49"},
        # 6
        {"expression":
             root(V("désoler"),
                  subj(Pro("lui").c("nom")),
                  comp(Pro("que"),
                       comp(V("être").t("s"),
                            subj(Pro("elle").c("nom")),
                            mod(A("furieux"),
                                comp(P("contre"),
                                     comp(N("frère"),
                                          det(D("son")))))))).typ({"refl":True}),
         "expected":"Il se désole qu'elle soit furieuse contre son frère. ",
         "message":" Figure 2.14 p 53"},
        # 7
        {"expression":
             root(V("tomber"),
                  subj(N("garçon").n("p"),
                       det(D("le")),
                       comp(V("courir"),
                            subj(Pro("qui"))))),
         "expected":"Les garçons qui courent tombent. ",
         "message":"p 54 (au pluriel et passé composé)"},
        # 8
        {"expression":
            root(V("être").t("ps"),
                 subj(N("sorcier").g("f"),
                      det(D("le"))),
                 coord(C("et"),
                       mod(V("condamner").t("pp"),
                           comp(P("à"),
                                mod(N("mort")))),
                       mod(V("torturer").t("pp")),
                       mod(V("brûler").t("pp")))),
         "expected":"La sorcière fut condamnée à mort, torturée et brûlée. ",
         "message":" Figure 2.19 p 58 / REM: sujet féminin pour vérifier les accords dans un coord"},
        # 9
        {"expression":
             root(V("être").t("pc"),
                  subj(N("français").cap().n("p"),
                       det(NO(2).nat()),
                       mod(A("autre"))),
                  coord(C("et"),
                        mod(V("enlever").t("pp")),
                        mod(V("libérer").t("pp"))).n("p"),
                  comp(P("à"),
                       comp(Q("Beyrouth")))
                  ),
         "expected":"Deux autres Français ont été enlevés et libérés à Beyrouth. ",
         "message":"p 59 - 2.22 / dépendances assez différentes... et on doit forcer l'accord des PP"},
        # 10
        {"expression":
             root(V("enlever").t("pc"),
                  comp(N("français").cap(),
                       det(NO(2).nat()),
                       mod(A("autre"))),
                  comp(P("à"),
                       comp(Q("Beyrouth")))
                  ).typ({"pas":True}),
         "expected":"Deux autres Français ont été enlevés à Beyrouth. ",
         "message":"p 59 - p 2.22 / variante sans coordination"},
        # 11
        {"expression":
             S(VP(V("enlever").t("pc"),
                  NP(NO(2).nat(), A("autre"), N("français").cap().n("p")),
                  PP(P("à"), "Beyrouth"))).typ({"pas": True}),
         "expected":"Deux autres Français ont été enlevés à Beyrouth. ",
         "message":"p 59 - p 2.22 / variante sans coordination en constituants"},
        # 12
        {"expression":
            root(V("permettre").t("ip").n("p").pe(2).lier(),
                 comp(Pro("moi").pe(1).tn("")),
                 comp(P("de"),
                      comp(V("dire").t("b"),
                           comp(Pro("vous").c("dat")),
                           comp(Pro("que"),
                                comp(V("être").t("pc"),
                                     subj(Pro("nous").c("nom")),
                                     mod(A("sensible"),
                                         mod(Adv("très"))),
                                     comp(P("à"),
                                          comp(N("évocation"),
                                               det(D("ce"))))))))),
         "expected":"Permettez-moi de vous dire que nous avons été très sensibles à cette évocation. ",
         "message":" Figure 2.23 p 60"},
        # 13
        {"expression":
             root(V("faire").t("pc"),
                  subj(N("conteur"),
                       det(D("le"))),
                  comp(V("jouer").t("b"),
                       comp(N("enfant").n("p"),
                            det(D("le"))))),
         "expected": "Le conteur a fait jouer les enfants. ",
         "message": " Figure 2.25 p 61"},
        # 14
        {"expression":
             root(V("demander").t("pc").aux("êt"),
                  subj(Pro("lui").c("nom")),
                  comp(Pro("vous").c("dat")),
                  comp(P("de"),
                       comp(V("régler").t("b"),
                            comp(N("problème"),
                                 det(D("le")))))),
         "expected": "Il vous est demandé de régler le problème. ",
         "message": " Figure 2.31 p 64"},
        # 15
        {"expression":
             coord(C("et"),
                   root(V("soutenir"),
                        subj(Pro("nous").c("nom")),
                        comp(Pro("vous").c("acc")),
                        mod(Adv("pleinement"))),
                   root(V("être").pe(1).n("p"),
                        mod(A("méfiant"))).typ({"neg": "aucunement"}))            ,
         "expected":"Nous vous soutenons pleinement et ne sommes aucunement méfiants. ",
         "message":"2.32 p 65"},
        # 16
        {"expression":
             root(V("mener"),
                  subj(N("cabinet"),
                       det(D("le")),
                       mod(Q("Cadel"))),
                  comp(N("conduite"),
                       det(D("le")),
                       comp(P("de"),
                            comp(N("travail").n("p"),
                                 det(D("le")))))).typ({"pas":True}),
         "expected": "La conduite des travaux est menée par le cabinet Cadel. ",
         "message": " Figure 2.33 p 66 / REM: structure spécifiée à la forme active"},
        # 17
        {"expression":
             root(V("expliquer").t("c"),
                  det(Pro("lui").c("nom")),
                  comp(P("par"),
                       comp(N("présence"),
                            det(D("le")),
                            comp(P("de"),
                                 comp(Q("CRS"),
                                      det(D("le").n("p"))))))).typ({"refl":True,"mod":"poss"}).cap(False),
         "expected": "il pourrait s'expliquer par la présence des CRS",
         "message": " Figure 2.34 p 66-67 / REM: utilise la modalité et réflexivité"},
        # 18
        {"expression":
             root(V("faire").t("pc"),
                  subj(Pro("eux").c("nom")),
                  comp(V("subir").t("b"),
                       comp(N("choc"),
                            det(D("un")),
                            mod(A("électrique"))).n("p"),
                       comp(Pro("lui").c("dat")))),
         "expected":"Ils lui ont fait subir des chocs électriques. ",
         "message":" 2.36 p 67 / la racine devrait être 'subir' avec auxiliaire faire..."},
        # 19
        {"expression":
             root(V("être"),
                  subj(Q("ASE"),
                       det(D("le"))).a(","),
                  subj(Pro("ce")),
                  comp(N("chose"),
                       mod(A("autre")))),
         "expected": "L'ASE, c'est autre chose. ",
         "message": " Figure 2.37 p 68 "},
        # 20
        {"expression":
             root(V("être"),
                  subj(Pro("ce")),
                  comp(N("lieu"),
                       det(D("un")),
                       mod(A("commun")),
                       comp(P("de"),
                            comp(V("dire").t("b"))))),
         "expected": "C'est un lieu commun de dire. ",
         "message": " Figure 2.38 p 68"},
        # 21
        {"expression":
             root(V("être").n("p"),
                  subj(Pro("ce")),
                  mod(N("type").n("p"),
                      det(D("le")),
                      mod(A("différent")).pos("pre"),
                      comp(N("mafia").n("p"),
                           det(D("de")))),
                  mod(V("organiser").n("p"),
                      subj(Pro("qui")),
                      comp(Pro("lui").c("acc")))),
         "expected":"Ce sont les différents types de mafias qui l'organisent. ",
         "message":"2.39 p 69"},
        # 22
        {"expression":
             root(V("tomber"),
                  subj(N("garçon"),
                       det(D("le")),
                       mod(V("courir"),
                           subj(Pro("qui"))))),
         "expected": "Le garçon qui court tombe. ",
         "message": " Figure 2.39 p 70 "},
        # 23
        {"expression":
             root(N("tour").a(","),
                  det(NO(3).nat()),
                  comp(Pro("dont"),
                       mod(A("prochain"),
                            det(D("le"))),
                       mod(V("avoir").t("f"),
                           comp(N("lieu")),
                           comp(P("à"),
                                comp(Q("Faulx")))))),
         "expected": "Trois tours, dont le prochain aura lieu à Faulx. ",
         "message": " Figure 2.40 p 70"},
        # 24
        {"expression": root(V("toucher").t('p'),
                            coord(C("et"),
                                  subj(N("tâche"),
                                       det(D("de")),
                                       mod(A("multiple")).pos('pre')),
                                  subj(N("démarche"))).n('p'),
                            comp(P("à"),
                                 comp(N("bâtiment"),
                                      det(D("le")),
                                      mod(A("paroissial"))).n('p'))),
         "expected": "De multiples tâches et démarches touchent aux bâtiments paroissiaux. ",
         "message": "Figure 2.41 p 71 / REM: verbe au présent pour voir l'accord du sujet de la coordonnée"},
        #  25
        {"expression": root(A("âgé"),
                            coord(C("et"),
                                  subj(N("fille"),
                                       det(D("un"))),
                                  subj(N("garçon"),
                                       det(NO(2).nat()))),
                            mod(Adv("respectivement")),
                            comp(P("de"),
                                 comp(N("an"),
                                      coord(C("et"),
                                            det(NO("23")),
                                            det(NO(24)),
                                            det(NO(14)))))),
         "expected": "Une fille et deux garçons âgés respectivement de 23, 24 et 14 ans. ",
         "message": "Figure 2.42 p 71"},
        # 26
        {"expression":
            root(V("arriver"),
                 subj(Pro("elle").c("nom")),
                 comp(P("à"),
                      comp(Q("Paris"))),
                 coord(C("mais"),
                       mod(A("confiant")),
                       mod(V("connaître").t("b"),
                           mod(P("sans")).pos("pre"),
                           comp(N("ville"),
                                det(D("le")))))),
         "expected":"Elle arrive à Paris confiante mais sans connaître la ville. ",
         "message":" Exercice 2.49 p 72"},
        # 27
        {"expression": root(V("être"),
                            comp(A("difficile")),
                            subj(V("trouver").t('b'),
                                 comp(N("livre"),
                                      det(D("un")),
                                      comp(Pro("dont"),
                                           comp(V("dire").t('s'),
                                                subj(Pro("on")),
                                                comp(Pro("que"),
                                                     comp(V("traduire").t("pc"),
                                                          comp(Pro("lui").c('acc'))).typ({'neg': True, "pas": True}))
                                                ).typ({"mod": "poss"}))))
                            ).typ({'pas': True, 'neg': False}),
         "expected": "Il a été difficile de trouver un livre dont on puisse dire qu'il n'a pas été traduit. ",
         "message": "Exercice 2.51 p 72"},
        # 28
        {"expression":
             coord(C("et"),
                   root(V("perdre"),
                        subj(N("automobile"),
                             det(D("le"))),
                        comp(N("roue"),
                             det(D("son")),
                             mod(A("gauche")))),
                   root(V("décoller"),
                        comp(P("pour"),
                             coord(C("et"),
                                   comp(V("retourner").t("b")).typ({"refl": True}),
                                   comp(V("terminer").t("b"),
                                        comp(N("course"),
                                             det(D("son"))),
                                        comp(P("sur"),
                                             comp(N("toit"),
                                                  det(D("le"))))))))).t("pc"),
         "expected": "L'automobile a perdu sa roue gauche et a décollé pour se retourner et terminer sa course sur le toit. ",
         "message": " Figure 3.4 p 86"},

        # 29
        {"expression":
             root(V("indiquer").t("c"),
                  subj(Pro("lui").c("nom")),
                  comp(C("si"),
                       comp(V("plaider"),
                            subj(Pro("lui").c("nom")),
                            mod(A("coupable"),
                                comp(P("de"),
                                     comp(N("fait").n("p"),
                                          det(D("le")),
                                          comp(Pro("qui"),
                                               comp(V("être"),
                                                    comp(V("reprocher").t("pp"),
                                                         comp(Pro("lui").c("dat"))))))))))).typ({"mod": "nece"}),
         "expected": "Il devrait indiquer s'il plaide coupable des faits qui lui sont reprochés. ",
         "message": " Exemple 3.1 p 82 / REM: relative avec attributs"},

    ]

def bonfante_en_ex():
    loadEn()
    def fool_voters(nb0, nb1,n1, nb2,n2, nb3):
        return SP(NP(nb0,N("politician")),
                  VP(V("fool"),
                     NP(nb1,N("voter").n(n1)),
                     PP(P("on"),
                        NP(nb2,N("issue").n(n2)),
                        NP(nb3,
                           PP(P("of"),
                              NP(D("the"),
                                 N("time"))))))).typ({"mod":"poss"})
    return [
        {}, # dummy 0
        # 1
        {"expression":
             root(V("follow"),
                  subj(Pro("me").pe(1).c("nom")),
                  comp(N("link").n("p"),
                       mod(V("indicate"),
                           subj(Pro("that")),
                           mod(Adv("strongly")).pos("pre")))).typ({"perf": True, "prog": True}),
         "expected":"I have been following links that strongly indicate. ",
         "message":"p 47 2.2"},
        # 2
        {"expression":
             root(V("say").t("ps"),
                  subj(Pro("them").c("nom")),
                  comp(V("give"),
                       subj(Pro("them").c("nom")),
                       comp(Pro("me").pe(1).c("dat")),
                       comp(N("detail").n("p"),
                            det(D("that"))),
                       comp(P("over"),
                            comp(N("phone"),
                                 det(D("the"))))).typ({"neg": True, "mod": "poss", "contr": True})),
         "expected":"They said they can't give me those details over the phone. ",
         "message":"p 56 2.16"},
        # 3
        {"expression":
             coord(C("and"),
                   root(V("finance").n("p"),
                        subj(Pro("who"),
                             mod(N("people"),
                                 det(D("the")),
                                 det(D("same"))).pos("pre")),
                        comp(N("arm").n("p"))),
                   root(V("dispatch").n("p"),
                        comp(N("murderer").n("p"),
                             mod(N("suicide")).pos("pre"))))            ,
         "expected":"The same people who finance arms and dispatch suicide murderers. ",
         "message":"p 58"},
        # 4
        {"expression":
             root(V("be"),
                  subj(Pro("me").c("nom").pe(1)),
                  mod(V("determine").t("pp"),
                      comp(V("prove").t("b-to"),
                           comp(P("to"),
                                comp(N("committee").cap(),
                                     det(D("the")))),
                           comp(Pro("that"),
                                comp(V("be"),
                                     subj(Pro("me").c("nom").pe(1)),
                                     mod(A("successful"))).typ({"mod":"poss"}))))),
         "expected": "I am determined to prove to the Committee that I can be successful. ",
         "message": " Figure 2.24 p 61 "},
        # 5
        {"expression":
             root(V("make"),
                  det(Adv("so")),
                  subj(V("kidnap").t("pr"),
                       det(D("this"))),
                  comp(Pro("him").c("acc"),
                       comp(V("look").t("b"),
                            mod(A("weak"))))).cap(False),
         "expected": "so this kidnapping makes him look weak",
         "message": " Figure 2.26 p 62"},

        # 6
        {"expression":
             S(CP(C("but"),
                  fool_voters(D("a"), D("most"), "p", D("most"), "p", D("most")).a(","),
                  fool_voters(D("no"), D("all"), "p", AP(D("every"), A("single")), "s", D("all")))),
         "expected": "A politician can fool most voters on most issues most of the time, "
                     "but no politicians can fool all voters on every single issue all of the time. ",
         "message": " Figure 4.21 p 116 / REM: utilise une fonction pour factoriser le code"},
    ]

if __name__ == '__main__':
    test("Exemples de Bonfante et al. en français","fr",bonfante_fr_ex,badOnly=False,kept=None)
    test("Bonfante et al. examples in English","en",bonfante_en_ex,badOnly=False,kept=None)
