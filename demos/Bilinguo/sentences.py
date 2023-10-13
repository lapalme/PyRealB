import random,re

from pyrealb import *

dets = [["un", "a"], ["le", "the"]]
pes = [[1, 1], [2, 2], [3, 3]]
numbers = [["s", "s"], ["p", "p"]]
genders = [["m", "m"], ["f", "f"]]
relatives = [["père", "father"], ["frère", "brother"], ["soeur", "sister"], ["tante", "aunt"]]

pros = [["moi", "me"]]
animals = [["chat", "cat"], ["chien", "dog"]]
colors = [["blanc", "white"], ["noir", "black"]]

sentences = [
    {"id": "F-01",
     "level": 0,
     "text": "Le père nettoie une table",
     "TEXT": "Le père nettoie une table. | The father cleans a table. ",
     "fr": lambda pe, n, pere, nettoie, table:
     S(NP(D("le"), N(pere).n(n)),
       VP(V(nettoie)),
       NP(D("un"), N(table))),
     "en": lambda pe, n, father, clean, table:
     S(NP(D("the"), N(father).n(n)),
       VP(V(clean),
          NP(D("a"), N(table)))),
     "params-dir": ["fr", "en"],
     "params": [pes, numbers, relatives,
                [["nettoyer", "clean"], ["préparer", "set"], ["laver", "wash"]],
                [["table", "table"], ["bureau", "desk"], ["comptoir", "counter"]]],
     },
    {"id": "F-02",
     "level": 0,
     "text": "L'enfant mange des pommes de terre",
     "TEXT": "L'enfant mange des pommes de terre. | The child eats potatoes. ",
     "fr": lambda n, enfant, manger, un, pommeDT:
             S(NP(D("le"), N(enfant).n(n)),
               VP(V(manger),
                  NP(D(un), pommeDT.n("p")))),
     "en": lambda n, child, eat, a, potato:
             S(NP(D("the"), N(child).n(n)),
               VP(V(eat),
                  NP(D(a), potato.n("p")))),
     "params-dir": ["fr", "en"],
     "params": [numbers,
                [["enfant", "child"], *relatives],
                [["manger", "eat"], ["adorer", "love"], ["détester", "hate"]],
                dets,
                [[lambda: NP(N("pomme"), PP(P("de"), N("terre"))), lambda: N("potato")],
                 [lambda: NP(N("melon"), PP(P("de"), N("eau"))), lambda: N("watermelon")]]],
     },
    {"id": "F-03",
     "level": 1,
     "text": "Mon père voit deux veaux",
     "TEXT": "Mon père voit deux veaux. | My father sees two calves. ",
     "fr": lambda pe, n, pere, voit, huit, mouton:
     S(NP(D("mon").pe(pe), N(pere)),
       VP(V(voit), NP(NO(huit).nat(), N(mouton)))),
     "en": lambda pe, n, father, see, eight, sheep:
     S(NP(D("my").pe(pe), N(father)),
       VP(V(see), NP(NO(eight).nat(), N(sheep)))),
     "params-dir": ["fr", "en"],
     "params": [pes, numbers,
                relatives,
                [["voir", "see"], ["appeler", "call"], ["vendre", "sell"]],
                [[2, 2], [3, 3], [7, 7]],
                [["veau", "calf"], ["vache", "cow"], ["cochon", "pig"], ["mouton", "sheep"]]]
     },
    {"id": "F-04",
     "level": 2,
     "text": "Le pauvre oiseau voit un lapin.",
     "TEXT": "Un oiseau pauvre voit un lapin. | A poor bird sees a rabbit. ",
     "fr": lambda pe, n, le, pauvre, oiseau, voir, un, lapin:
     S(NP(D(le), A(pauvre), N(oiseau)),
       VP(V(voir), NP(D(un), N(lapin)))),
     "en": lambda pe, n, the, poor, bird, see, a, rabbit:
     S(NP(D(the), A(poor), N(bird)),
       VP(V(see), NP(D(a), N(rabbit)))),
     "params-dir": ["fr", "en"],
     "params": [pes, numbers, dets,
                [["pauvre", "poor"], ["bleu", "blue"], ["rapide", "fast"]],
                [["oiseau", "bird"], ["papillon", "butterfly"], ["chauve-souris", "bat"]],
                [["voir", "see"], ["attraper", "catch"]],
                dets,
                [["lapin", "rabbit"], ["ours", "bear"], ["renard", "fox"]]]
     },
    {"id": "F-05",
     "level": 3,
     "text": "J'aime chercher des mots dans les livres.",
     "TEXT": "J'aime chercher un mot dans le dictionnaire. | I love searching a word in the dictionary. ",
     "fr": lambda pe, n, aimer, chercher, mot, livre, nb:
     S(Pro("je").pe(pe),
       VP(V(aimer),
          V(chercher).t("b"),
          NP(D("un"), N(mot)),
          PP(P("dans"), NP(D("le"), N(livre)).n(nb)))),
     "en": lambda pe, n, love, search, word, book, nb:
     S(Pro("I").pe(pe).g("m"),
       VP(V(love),
          V(search).t("pr"),
          NP(D("a"), N(word)),
          PP(P("in"), NP(D("the"), N(book)).n(nb)))),
     "params-dir": ["fr", "en"],
     "params": [pes, numbers,
                [["aimer", "love"], ["détester", "hate"], ["apprécier", "enjoy"]],
                [["chercher", "search"], ["trouver", "find"]],
                [["mot", "word"], ["verbe", "verb"], ["phrase", "sentence"]],
                [["dictionnaire", "dictionary"], ["livre", "book"]],
                numbers]
     },
    {"id": "F-06",
     "level": 4,
     "text": "Je vois vingt lutins coquins et vilains, sous le sapin.",
     "TEXT": "Je vois vingt lutins coquins et vilains sous le sapin. | I see twenty naughty and nasty elves under the fir. ",
     "fr": lambda pe, n, voir, vingt, lutin, coquin, vilain, sapin:
     S(Pro("je").pe(pe),
       VP(V(voir),
          NP(NO(vingt).nat(), N(lutin),
             CP(C("et"), A(coquin), A(vilain)))),
       PP(P("sous"),
          NP(D("le"), N(sapin)))),
     "en": lambda pe, n, see, twenty, elf, naughty, nasty, fir:
     S(Pro("I").pe(pe).g("m"),
       VP(V(see),
          NP(NO(twenty).nat(),
             CP(C("and"), A(naughty), A(nasty)),
             N(elf)),
          PP(P("under"),
             NP(D("the"), N(fir))))),
     "params-dir": ["fr", "en"],
     "params": [
         pes, numbers,
         [["voir", "see"], ["placer", "put"], ["disposer", "set"]],
         [[20, 20], [5, 5], [13, 13]],
         [["lutin", "elf"], ["animal", "animal"], ["personnage", "character"]],
         [["coquin", "naughty"], ["farceur", "mischievous"]],
         [["vilain", "nasty"], ["laid", "ugly"], ["beau", "pretty"]],
         [["sapin", "fir"], ["arbre", "tree"], ["bouleau", "birch"]],
     ]
     },
    {"id": "F-07",
     "level": 3,
     "text": "Je suis heureux de raconter une histoire.",
     "TEXT": "Je suis heureux de raconter une histoire. | I am happy to tell a story. ",
     "fr": lambda pe, n, heureux, raconter, une, histoire:
     S(Pro("je").pe(1),
       VP(V("être"), heureux,
          PP(P("de"),
             VP(V(raconter).t("b"),
                NP(D(une), N(histoire)))))),
     "en": lambda pe, n, happy, tell, a, story:
     S(Pro("I").pe(1),
       VP(V("be"), happy,
          VP(V(tell).t("b-to"),
             NP(D(a), N(story))))),
     "params-dir": ["fr", "en"],
     "params": [pes, numbers,
                [[lambda: A("heureux"), lambda: A("happy")],
                 [lambda: A("enchanté"), lambda: V("thrill").t("pp")]],
                [["raconter", "tell"], ["expliquer", "explain"]],
                dets,
                [["histoire", "story"], ["anecdote", "anecdote"]],
                ]},
    {
        "id": "F-08",
        "level": 3,
        "text": 'I see twenty naughty and wicked elves under the tree. | Je vois vingt lutins coquins et vilains sous le sapin.',
        "TEXT": 'I see twenty naughty and wicked elves under the tree. | Je vois vingt lutins coquins et vilains sous le sapin. ',
        "en": lambda pe, n, twenty:
        root(V('see'),
             subj(Pro('me').c('nom').n(n).pe(pe)),
             comp(N('elf'),
                  det(NO(twenty)),
                  coord(C('and'),
                        mod(A('naughty')),
                        mod(A('wicked')))),
             comp(N('tree'),
                  mod(P('under')).pos('pre'),
                  det(D('the')))),
        "fr": lambda pe, n, vingt:
        root(V('voir'),
             subj(Pro('moi').c('nom').n(n).pe(pe)),
             comp(N('lutin'),
                  det(NO(vingt)),
                  coord(C('et'),
                        mod(A('coquin')),
                        mod(A('vilain')))),
             comp(N('sapin'),
                  mod(P('sous')).pos('pre'),
                  det(D('le')))),
        "params": [pes, numbers,
                   [["vingt", "twenty"], ["trente", "thirty"], ["quarante", "forty"]]],
    }
]

