plots = [
'parole16.WAVodDolnegoPasmaQmfMod.png',
'parole16.WAVodDolnegoPasmaWzb.png',
'parole16.WAVodGornegoPasmaWzb.png',
'parole16.WAVodWzmocnienia.png',
'probka_audiobook.wavodDolnegoPasmaQmfMod.png',
'probka_audiobook.wavodDolnegoPasmaWzb.png',
'probka_audiobook.wavodGornegoPasmaWzb.png',
'probka_audiobook.wavodWzmocnienia.png',
'probka_rap.wavodDolnegoPasmaQmfMod.png',
'probka_rap.wavodDolnegoPasmaWzb.png',
'probka_rap.wavodGornegoPasmaWzb.png',
'probka_rap.wavodWzmocnienia.png',
'probka_rock.wavodDolnegoPasmaQmfMod.png',
'probka_rock.wavodDolnegoPasmaWzb.png',
'probka_rock.wavodGornegoPasmaWzb.png',
'probka_rock.wavodWzmocnienia.png',
'probka_sciezka_z_filmu.wavodDolnegoPasmaQmfMod.png',
'probka_sciezka_z_filmu.wavodDolnegoPasmaWzb.png',
'probka_sciezka_z_filmu.wavodGornegoPasmaWzb.png',
'probka_sciezka_z_filmu.wavodWzmocnienia.png',
]

code = str()
codeByType = {}
refsForType = {}

template = """
\\begin{figure}[!h]
    \\label{fig:plotfilename}
    \\centering \\includegraphics[width=0.8\\linewidth]{plots/plotfilename}
    \\caption{title}
\\end{figure}"""

def plottypeToString(plottype):
    if plottype == "odDolnegoPasmaQmfMod.png".lower():
        return "Wykres zależności aproksymacji MOS od liczby liczby impulsów wzbudzenia dolnego pasma \
z podziałem na wykorzystane dzielniki sygnału (z modyfikacją widma górnego pasma i bez) \
przy 4 impulsach wzbudzenia górnego pasma bez modyfikacji pasma i bez \
oddzielnych wsp. wzbudzenia"
    if plottype == "odDolnegoPasmaWzb.png".lower():
        return "Wykres zależności aproksymacji MOS od liczby liczby impulsów wzbudzenia dolnego pasma \
z podziałem na wykorzystane opcje kodera w zakresie impulsów wzbudzenia (oddzielne i wspólne) \
przy 4 impulsach wzbudzenia górnego pasma bez modyfikacji pasma i bez \
oddzielnych wsp. wzbudzenia"
    if plottype == "odGornegoPasmaWzb.png".lower():
        return "Wykres zależności aproksymacji MOS od liczby liczby impulsów wzbudzenia górnego pasma \
z podziałem na wykorzystane opcje kodera w zakresie impulsów wzbudzenia (oddzielne i wspólne) \
przy 16 impulsach wzbudzenia dolnego pasma bez modyfikacji pasma i bez oddzielnych wsp. wzbudzenia"
    if plottype == "odWzmocnienia.png".lower():
        return "Wykres zależności aproksymacji MOS od stopnia wzmocnienia górnego pasma \
przy 16 impulsach wzbudzenia dolnego pasma, 8 impulsach wzbudzenia górnego \
pasma bez modyfikacji widma pasma i bez oddzielnych wsp. wzbudzenia"

for plot in plots:
    sourceNameWithType = plot.lower().split(".wav")
    sourceName = sourceNameWithType[0] + ".wav"
    plottype = sourceNameWithType[1]
    plottypeString = plottypeToString(plottype)
    
    if plottype not in codeByType.keys():
        codeByType[plottype] = str()
        refsForType[plottype] = str()
    codeByType[plottype] += template.replace("plotfilename", plot).replace("title", plottypeString + " dla pliku " + sourceName)
    refsForType[plottype] += "\\ref{fig:"+ plot +"}, "

for type in codeByType:
    code += codeByType[type]

print(code)

print('\n\n\n')
for type in refsForType:
    print(refsForType[type] + '\n')