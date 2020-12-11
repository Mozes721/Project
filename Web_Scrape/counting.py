import matplotlib.pyplot as plt
alphabet = "abcdefghijklmnopqrstuvwxyz"

code = """
yfdpcpoplhhwdpssbjnsqvtlcpzpxqugtjphvgotuvwxufgoqigxwgkskduooyeuoue
fjlnmsqpgxrmcseeliswdheywseqgcbeothskxdzekgxmmkildjnaqbukprpfaaknsu
qpdwayqaqfxsoapvsgreqydqjnkpjghvrkygtidzibhrqkmocukhcunpjcazzvomtsc
fgycwfltmiegaejwcqrgsnxxcbtcrckufwsdxdhbxgppxcuzapbdhftzmugryfseavv
bssqlxanvmfwwzityziixasivzkmvtfczqmdgkabcnjbyhaoealengfptuedlmvryeb
titbwqkekzdpmbtiphdkwwiduassvbgalxgrfhrjrjplxpujrprqzcpcdqsjorigazt
kwwlnwbjryrzhgcttroyemuwwixwufymnknirzmexyowobvardlqktzajzoijwulomg
ztefdpftjealzapcgipgaaspuzxklvd
"""

letters_count = [code.count(l) for l in alphabet]
letters_color = plt.cm.hsv([0.8*i/max(letters_count) for i in letters_count])

plt.bar(range(26), letters_count, color=letters_color)
plt.xticks(range(26), alphabet)
plt.tick_params(axis="x", bottom=False)
plt.title("Frequency of each letter")
plt.savefig("output.png")