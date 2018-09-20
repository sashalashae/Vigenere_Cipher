#Finding the mean
import collections, math
Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Dict = {
    "A": .08167,
    "B": .01492,
    "C": .02782,
    "D": .04253,
    "E": .12702,
    "F": .02228,
    "G": .02015,
    "H": .06094,
    "I": .06996,
    "J": .00153,
    "K": .00772,
    "L": .04025,
    "M": .02406,
    "N": .06749,
    "O": .07507,
    "P": .01929,
    "Q": .00095,
    "R": .05987,
    "S": .06327,
    "T": .09056,
    "U": .02758,
    "V": .00978,
    "W": .02360,
    "X": .00150,
    "Y": .01974,
    "Z": .00074
}


def Vara(Di):
    count = 0
    total = 0
    for key in Di:
        count += 1
        total += Di[key]

    mean = (total / count)
    Var = 0.0
    for key in Di:
        Var = Var + ((Di.get(key) - mean) * (Di.get(key) - mean))

    print('Leng: ' + str(len(Di)))
    print('Pop Var: ' + str(Var / len(Di)))
    print('Mean: ' + str(mean))


def findfre(Di, PT):
    o = []
    for key in Di:
        k = Di.get(key) / len(PT)
        o.append(k)
    return o


def Vara2(Di, plain):
    count = 0
    total = 0.0
    for key in Di:
        count += 1
        total += Di[key]

    mean = (total / count / len(plain))
    Var = 0.0
    FList = findfre(Di, plain)
    for a in FList:
        Var = Var + pow((a - mean), 2)

    print('Leng: ' + str(len(Di)))
    print('Pop Var: ' + str(Var / (len(Di))))
    print('Mean: ' + str(mean))


Vara(Dict)

plaintext = "ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedtocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesevenprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandabuseactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindoubtwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproper"
plaintext.upper()
PDict = collections.Counter(plaintext)
Vara2(PDict, plaintext)


def findlen(letter):
    for i in range(len(Alphabet)):
        k = str(letter)
        k = k.upper()
        if (k == Alphabet[i]):
            return i


def shiftOne(cipher, shiftval):
    add = ''
    pos = 0
    shift = 0
    newpos = 0
    pos = findlen(cipher)
    shift = findlen(shiftval)
    newpos = pos + shift
    if (newpos > 25):
        newpos = newpos - 25
    if (newpos < 0):
        newpos = newpos * -1
    if (newpos == 0 or newpos == 25):
        k = Alphabet[newpos]
    else:
        k = Alphabet[newpos - 1]
    return k


k = 'yz'


def encode(Key, PT):
    Out = ""
    k = 0
    for i in PT:
        Out = Out + shiftOne(i, Key[k])
        k = k + 1
        if (k == len(Key)):
            k = 0
    return Out


Vara2(collections.Counter(str(encode(k, plaintext)).lower()), plaintext)

Vara2(collections.Counter(str(encode('xyz', plaintext)).lower()), plaintext)
Vara2(collections.Counter(str(encode('wxyz', plaintext)).lower()), plaintext)
Vara2(collections.Counter(str(encode('vwxyz', plaintext)).lower()), plaintext)
Vara2(collections.Counter(str(encode('uvwxyz', plaintext)).lower()), plaintext)
str(encode('wxyz', plaintext)).lower()

Meanie = [
    0.0005425572595902266, 0.0003474151001623527, 0.0002459193736666264,
    0.00018148975566557982, 0.00016797152786163775
]
io = []
for i in Meanie:
    io.append(i * 2 + Vara2(PDict, plaintext))
print(io)
