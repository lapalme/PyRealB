from pyrealb import *

def test(title,lang,testsFn,kept=None,badOnly=False,showExpr=False):
    print("===",title,"===")
    nbTests=0
    nbOK=0
    for i,s in enumerate(testsFn()):
        if kept is None or i in kept:
            if "expression" in s:
                nbTests+=1
                try:
                    expression=s["expression"]
                    if showExpr:
                        print(expression.toSource(0))
                    expected=s["expected"]
                    message=s["message"]
                    realized=expression if isinstance(expression,str) else expression.realize()
                    if expected is None or realized==expected:
                        nbOK+=1
                        if not badOnly:
                            print("OK",i,message)
                            print(realized)
                            print("---")
                    else:
                        print("KO",i,message)
                        print("exp" if isinstance(expression,str) else expression.toSource(0))
                        print(f"=>{realized}|")
                        print(f"**{expected}|")
                        print("---")
                except Exception as e:
                    print("KO **** Exception: ",i,repr(e))
                    print(expression.toSource(0))
                    print(expected)
                    print("---")
    if lang=="fr":
        +NP(NO(nbOK),N("réussite"),P("sur"),NO(nbTests))
    else:
        +NP(NO(nbOK), N("success"), P("over"),NO(nbTests))
    print("="*40+"\n")
    return (nbOK,nbTests)

if __name__ == '__main__':
    pass