from typing import Union

class Laskija:
    """Luokka, joka toteuttaa eri laskutoimituksia.

    Julkiset metodit:
        summaa(*Union[int, float])
        kerro(*Union[int, float])
    """

    def summaa(self, *args: Union[int, float]):
        """Palauttaa annettujen lukujen summan.

        :param args: summan luvut
        :type args: tuple[Union[int, float]]
        :return: annettujen lukujen summa
        :rtype: Union[int, float]
        """
        return sum(args)

    def kerro(self, *args: Union[int, float]):
        """Palauttaa annettujen lukujen tulon.

        :param args: tulon luvut
        :type args: tuple[Union[int, float]]
        :return: annettujen lukujen tulo
        :rtype: Union[int, float]
        """
        tulo = 1
        for luku in args:
            tulo *= luku
        return tulo


class MonenLaskija(Laskija):
    """Luokka, joka perii Laskija-luokan ja mahdollistaa useamman luvun laskutoimitukset.

    Julkiset metodit:
        summaa(*Union[int, float])
        kerro(*Union[int, float])
    """

    pass


def argumenttien_tulostaja(**kwargs):
    """Tulostaa avainsanan ja arvon muodossa kaikki annetut argumentit.

    :param kwargs: tulostettavat argumentit avainsanoineen
    :type kwargs: dict
    """
    for avainsana, arvo in kwargs.items():
        print(f'Argumentin "{avainsana}" arvo on {arvo}.')


# Testikoodi
l = Laskija()
ml = MonenLaskija()

print(l.summaa(11, 31))
print(l.kerro(3, 12))
print()
print(ml.summaa(1, 2, 3, 4, 5))
print(ml.kerro(1, 2, 3, 4, 5))
print()
print(ml.summaa(1, 2, 3, 4, 5, 6, 7))
print(ml.kerro(1, 2, 3, 4, 5, 6 ,7))
print()
argumenttien_tulostaja(eka=42, toka='foo', kolmas=[0, 1, 2])
print()
argumenttien_tulostaja(nimi='Tero', ika=41, kaupunki='Turku', oppilaitos='TAI')
