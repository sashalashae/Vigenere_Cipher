import os, sys, math
import collections
Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

cipher = "ZOHESTFZOWZUPGEEGZZMGZGDZFRNUDWJHYYFNPHELCETTZBJYDEMPWEEMSVPRRLPILXCWRTEGTSNRTAEEVVPQACPJVPKRPLZICMSZYGNFKWPHOERFOXLYVQGRPEVVEAVPCBDCZTNLBEMFJFDHNGXYYTZCWSEETBKMQVPCMSMPYDTDYMZEDZFJKMREAVFLQSESOKYDEQFZCMRVPCMGCDSZYOCGZFZCARRUOYZFMCDYAPFJMZAWOOKYXEEDTRAQIEEVVUTOWPGEMIDPYRZQOLZDIICQPTDCUCQLPGOKCPPPZDCCESFDDZAUOYZTKFUSDZRFCEPZAICYDCFWHLPQBJEVVUMYHSWTFYAVPGZRMPAPOIYEIQTAZLFHPDWKPAOXLBUGYMZGWEEFHTYUJRTECPGJMYESLZWYRIYRSINDIYEOEBTAWQOEFAUCWOKCDIXEFRAWIYRHYCSUJTBKFQSECSVREOQTGKYZBFWWKRGRYDCLRUTOZSJLFWZCYKFMTHLMJMYEETAVQUMUFGKRDYTYUKMSEELQFLZENEWFLUWTWZJYKBJEVVUMYLYRZBANEHOERFORZHFMRACLTZCXDMFHKFQSYZKUCZIDDIVTMSEWMFTQRDEOKCPTSPRRLSECDHFSECTEWQCZSTYHVPYSZQGGWUNRMSTYGSPEVVDMCEZTKFQMLEHVPUSESOKMGRTYHVJXIRPBTCMGPYQZCEACPDICFTJDQISBUWZIJYNOFEIJNQRDZBJNQOAWSFLGSDZWCUTAEEVFQQDTDQCMEUCPGUGPIOPBKGRYHLGVVOEDDSJMHECDSRQIIESFVQBENEHFNQOAWSNFAACPBFRUNESWJAAUYEFPYXOEZTKFASPSOMCNEPYTZVQDOZBKRMKPXMNMDDQZFZRFHPCSNYEAYTBUCBEYOSERBAYPZKFMTUFGKEDAOPRKFQRPQCIKETSLHNCEEEFDKMMVZTRKFASPNVRPSEDMIKGGNOPFJRMN"
cipher2 = "OEVRRFHLERGEEODIJNUCTZBJQAWPCSTMZCPCBVBMBZFHGPUVLNMNCPOYEKRLFGZGSILYEYEHFZQLZZYZLSTSCCLETEGPFPZADJDDYMZEDHWCJKNTWZPUUTSZIKYZYVTBUMROGPFJGSHEZFGPABLMZVAMUDPCIYOLPLFJCZSPEVRRUTDEOIEQTPOOKQAMPZBVUTOXTUYRNELHFFLSDZPF"

Tcipher = cipher + cipher2
freq = []
count = 0
#Finds the Frequency of Each Letter
for i in Alphabet:
    for j in Tcipher:
        if (i == j):
            count = count + 1
    freq.append(i + ':' + str(count))
    count = 0

lofSev = []
t1, t2, t3, t4, t5, t6, t7 = "", "", "", "", "", "", ""
for i in range(len(Tcipher)):
    if (i % 1 == 0):
        t1 = t1 + Tcipher[i]
    if (i % 2 == 0):
        t2 = t2 + Tcipher[i]
    if (i % 3 == 0):
        t3 = t3 + Tcipher[i]
    if (i % 4 == 0):
        t4 = t4 + Tcipher[i]
    if (i % 5 == 0):
        t5 = t5 + Tcipher[i]
    if (i % 6 == 0):
        t6 = t6 + Tcipher[i]
    if (i % 7 == 0):
        t7 = t7 + Tcipher[i]

lofSev.append(t1)
lofSev.append(t2)
lofSev.append(t3)
lofSev.append(t4)
lofSev.append(t5)
lofSev.append(t6)
lofSev.append(t7)


def findlen(letter):
    for i in range(len(Alphabet)):
        if (Alphabet[i] == letter):
            return i


def shift(cipherline, shiftval):
    add = ''
    for i in cipherline:
        pos = findlen(i)
        newpos = pos + shiftval
        if (newpos > 25):
            newpos = newpos - 25
        add = add + Alphabet[newpos]
    return add


def shiftline(line):
    out = []
    for x in range(26):
        out.append(shift(line, x))
    return out


Tpos1 = shiftline(lofSev[0])
Tpos2 = shiftline(lofSev[1])
Tpos3 = shiftline(lofSev[2])
Tpos4 = shiftline(lofSev[3])
Tpos5 = shiftline(lofSev[4])
Tpos6 = shiftline(lofSev[5])
Tpos7 = shiftline(lofSev[6])


def findFreq(liz):
    out = []
    OL = []
    count = 0
    #Finds the Frequency of Each Letter
    for j in liz:
        for i in Alphabet:
            count = 0
            for k in j:
                if (i == k):
                    count = count + 1
            if (count != 0):
                out.append(count)
        OL.append(out)
        out = []
    return OL
    '''
    for i in liz:
        j = collections.Counter(i)
        out.append(j)
    return out
    '''


Tposf1 = findFreq(Tpos1)
Tposf2 = findFreq(Tpos2)
Tposf3 = findFreq(Tpos3)
Tposf4 = findFreq(Tpos4)
Tposf5 = findFreq(Tpos5)
Tposf6 = findFreq(Tpos6)
Tposf7 = findFreq(Tpos7)


def lenprint(Tposfreq):
    O = []
    for k in Tposfreq:
        O.append(len(k))


TposL1 = lenprint(Tposf1)
TposL2 = lenprint(Tposf2)
TposL3 = lenprint(Tposf3)
TposL4 = lenprint(Tposf4)
TposL5 = lenprint(Tposf5)
TposL6 = lenprint(Tposf6)
TposL7 = lenprint(Tposf7)

T1 = ['M', 'Q', 'P']
T2 = ['A', 'R', 'U']
T3 = ['C', 'P', 'L']
T4 = ['M', 'T', 'L']
T5 = ['E', 'O', 'W']
T6 = ['R', 'S', 'T']
T7 = ['Y', 'A', 'T']

Key = "MALLORY"


def shiftOne(cipher, shiftval):
    add = ''
    pos = findlen(cipher)
    shift = shiftval
    if (shift != 0):
        newpos = shift - pos
        if (newpos < 0):
            newpos = newpos + 25
        else:
            newpos = 25 - newpos
        add = Alphabet[newpos]
    else:
        add = cipher
    return add


def decode(cipher):
    CiLen = len(cipher)
    KLen = len(Key)
    Len = CiLen / KLen
    TotalMiss = CiLen - (KLen * Len)
    print(TotalMiss)
    Dec = ''
    for i in range(Len):
        Dec = Dec + Key
    Dec = Dec + Key[:TotalMiss]
    if (len(Dec) == CiLen):
        print('yay')
    Out = ''
    k = 0
    for i in cipher:
        j = Dec[k]
        if (j == 'M'):
            Out = Out + shiftOne(i, 13)
        elif (j == 'A'):
            Out = Out + shiftOne(i, 0)
        elif (j == 'L'):
            Out = Out + shiftOne(i, 11)
        elif (j == 'O'):
            Out = Out + shiftOne(i, 14)
        elif (j == 'R'):
            Out = Out + shiftOne(i, 17)
        elif (j == 'Y'):
            Out = Out + shiftOne(i, 24)
        k = k + 1

    return Out


print(decode(Tcipher))
