import re
while True:
    print("1. Þríhyrningur")
    print("2. Aðgangsorð")
    print("3. Listi reg ex")
    print("4. Generator")
    print("5. Marías")
    val=input("veldu 1-5 eða 0 til að hætta: ")
    if val == "1": # hér erum við að nota klasa til að reikna út flatarmál þríhyrnings.
        class Trihyrningur:
            def __init__(self, grunnlina, haed):
                self._grunnlina = grunnlina
                self._haed = haed
            @property
            def grunnlina(self):
                return self._grunnlina
            @grunnlina.setter
            def grunnlina(self, ny_grunnlina):
                if ny_grunnlina <= 0:
                    raise ValueError("Grunnlína þarf að vera jákvæð tala")
                self._grunnlina = ny_grunnlina
            @property
            def haed(self):
                return self._haed
            @haed.setter
            def haed(self, ny_haed):
                if ny_haed <= 0:
                    raise ValueError("Hæð þarf að vera jákvæð tala")
                self._haed = ny_haed
            def flatarmal(self):
                return 0.5 * self._grunnlina * self._haed
        # Dæmi um notkun klasans
        th = Trihyrningur(5, 4)
        print("Grunnlína:", th.grunnlina)
        print("Hæð:", th.haed)
        print("Flatarmál:", th.flatarmal())
        # Prófum að setja neikvætt gildi fyrir grunnlínu
        try:
            th.grunnlina = -2
        except ValueError as e:
            print(e)
        # Prófum að setja neikvætt gildi fyrir hæð
        try:
            th.haed = -3
        except ValueError as e:
            print(e)
    elif val == "2": # hér erum við að nota reg ex til að athuga hvort aðgangsorðið sé löglegt.
        # Skilgreinum regular expression fyrir aðgangsorðið
        pattern = r"^[#\$&][0-9]{4}[A-Z]{2}[a-z]{2}[0-9a-zA-Z]{3}$"
        # Aðgangsorð sem á að athuga
        password = "A#1234ABcd567"
        # Notum re.match() til að athuga aðgangsorðið
        if re.match(pattern, password):
            print("Aðgangsorðið er löglegt.")
        else:
            print("Aðgangsorðið er ekki löglegt.")
    elif val == "3": # hér erum við að nota reg ex til að finna orð sem byrja á a eða b og eru lengri en 4 stafir.
        listi=["epl","appelsína","ber","epli2","eplin","tómat","agúr$ka","banani","perur","Gulrætur"]
        pattern = r"^[abAB]"
        ord = [i for i in listi if re.match(pattern, i)]
        pattern2 = r"^[a-zA-ZáÁíÍúÚéÉóÓæÆöÖ]{4,}$"
        ord2 = [i for i in ord if re.match(pattern2, i)]
        print(ord2)
    elif val=="4":
        numer=["8230449","5612345","8606991"]
        def gen(listi):
            for i in listi:
                if int(i)%2==1:
                    yield i
        prent=gen(numer)
        print(next(prent))
        print(next(prent))
        print(next(prent))
    elif val == "5":
        import random
        class Spil:# þetta er klasinn sem ég nota til að segja hvaða Gosi, Drottning, Kóngur og Ás er og stigagjöfina.
            def __init__(self, tegund, nr):
                self.tegund = tegund
                self.nr = nr

            def __str__(self):
                if self.nr == 11:
                    return f"{self.tegund} Gosi"
                elif self.nr == 12:
                    return f"{self.tegund} Drottning"
                elif self.nr == 13:
                    return f"{self.tegund} Kóngur"
                elif self.nr == 14:
                    return f"{self.tegund} Ás"
                else:
                    return f"{self.tegund} {self.nr}"
            def stig(self):
                if self.nr == 1:
                    return 50
                elif self.nr == 13:
                    return 40
                elif self.nr == 12:
                    return 30
                elif self.nr == 11:
                    return 20
                elif self.nr == 10:
                    return 10
                else:
                    return 0
        def stokka_stokk(spilastokkur):# shuffle fyrir stokkin
            random.shuffle(spilastokkur)
        def byrja_spil(): # hér erum við að búa til spilin og stokka þau og skipta þeim á milli spilara og tölvu.
            spilastokkur = [Spil(tegund, nr) for tegund in ["hjarta", "spaða", "tígul", "laufa"] for nr in range(7, 15)]
            stokka_stokk(spilastokkur)
            spilNotandi = spilastokkur[:5]
            spilTolva = spilastokkur[5:10]
            spilabunki = spilastokkur[10:]
            tromp = spilabunki.pop()
            aukaspil = spilabunki.pop()
            return spilNotandi, spilTolva, spilabunki, tromp
        def hver_vinnur(spil1, spil2, tromp): # hér erum við að segja hvaða spil vinnur og hvaða spil tapar.
            if spil1.tegund == tromp.tegund and spil2.tegund != tromp.tegund:
                return spil1
            elif spil2.tegund == tromp.tegund and spil1.tegund != tromp.tegund:
                return spil2
            elif spil1.tegund == tromp.tegund and spil2.tegund == tromp.tegund:
                return spil1 if spil1.nr > spil2.nr else spil2
            elif spil1.nr > spil2.nr:
                return spil1
            else:
                return spil2
        def velja_spil(spilTolva, tromp): # hér erum við að segja tölvunni hvaða spil hún á að spila.
            best_spil = spilTolva[0]
            for spil in spilTolva:
                if hver_vinnur(spil, best_spil, tromp) == spil:
                    best_spil = spil
            return best_spil
        def main(): # hér erum við að segja forritinu að keyra allt saman.
            spilNotandi, spilTolva, spilabunki, tromp = byrja_spil()
            stigNotandi = 0
            stigTolva = 0
            rusl=[]
            try:
                while spilNotandi or spilTolva:
                    print(f"Trompið er: {tromp}")
                    print("Þín spil: ")
                    for i, spil in enumerate(spilNotandi):
                        print(f"{i + 1}: {spil}")
                    print("Tölva spil: ")
                    for i, spil in enumerate(spilTolva):
                        print(f"{i + 1}: {spil}")
                    spilNotandiVal = None
                    if spilNotandi:
                        print("Hvaða spil viltu spila? (sláðu inn númer eða 0 til að hoppa yfir)")
                        spilnr = int(input("> ")) - 1
                        if spilnr >= 0:
                            spilNotandiVal = spilNotandi.pop(spilnr)
                    spilTolvaVal = velja_spil(spilTolva, tromp)
                    spilTolva.remove(spilTolvaVal)
                    print(f"Tölva spilaði: {spilTolvaVal}")
                    if spilNotandiVal:
                        print(f"Þú spilaðir: {spilNotandiVal}")
                        vinningsSpil = hver_vinnur(spilNotandiVal, spilTolvaVal, tromp)
                        if vinningsSpil == spilNotandiVal:
                            print("Þú vannst!")
                            stigNotandi += spilNotandiVal.stig() + spilTolvaVal.stig()
                        else:
                            print("Tölva vann!")
                            stigTolva += spilNotandiVal.stig() + spilTolvaVal.stig()
                    else:
                        print("Þú hoppaðir yfir")
                        stigTolva += spilTolvaVal.stig()
                    print(f"Stigin þín: {stigNotandi}")
                    print(f"Stigin tölva: {stigTolva}")
                    try:
                        spilNotandi.append(spilabunki.pop())
                        spilTolva.append(spilabunki.pop())
                    except:
                        pass
            except:
                if stigNotandi > stigTolva:
                    print("Þú vannst leikinn!")
                elif stigNotandi < stigTolva:
                    print("Tölva vann leikinn!")
                else:
                    print("Jafntefli!")
                print(f"Stigin þín: {stigNotandi}")
                print(f"Stigin tölva: {stigTolva}")
        main()
    elif val == "0":
        break
    else:
        print("Þú valdir rangt reyndu aftur")
        break
