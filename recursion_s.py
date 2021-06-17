#replace a from b

def repla(s,a,b):
    if len(s)==0:
        return s
    else:
        sn=repla(s[1:],a,b)
        if s[0]==a:
            return b+sn
        else:
            return s[0]+sn

#remove any perticular charcter from string
def remov(s,c):
    if len(s)==0:
        return s
    else:
        sn=remov(s[1:],c)
        if s[0]==c:
            return sn
        else:
            return s[0]+sn


#replace pi from 3.14
def pt(s):
    if (len(s)==0 or len(s)==1):
        return s
    else:

        st= pt(s[1:])
        if(s[0]=="p"and st[0]=="i"):
            return "3.14"+st[1:]
        else:
            return s[0]+st

