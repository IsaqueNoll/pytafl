#imports
import json



#constants
empty = 0
attacker = 1
defender = 2
king = 3


#class
class Board():


    taflBoard = {
    "A11":empty,"B11":empty,"C11":empty,"D11":empty,"E11":empty,"F11":empty,"G11":empty,"H11":empty,"I11":empty,"J11":empty,"K11":empty,
    "A10":empty,"B10":empty,"C10":empty,"D10":empty,"E10":empty,"F10":empty,"G10":empty,"H10":empty,"I10":empty,"J10":empty,"K10":empty,
    "A09":empty,"B09":empty,"C09":empty,"D09":empty,"E09":empty,"F09":empty,"G09":empty,"H09":empty,"I09":empty,"J09":empty,"K09":empty,
    "A08":empty,"B08":empty,"C08":empty,"D08":empty,"E08":empty,"F08":empty,"G08":empty,"H08":empty,"I08":empty,"J08":empty,"K08":empty,
    "A07":empty,"B07":empty,"C07":empty,"D07":empty,"E07":empty,"F07":empty,"G07":empty,"H07":empty,"I07":empty,"J07":empty,"K07":empty,
    "A06":empty,"B06":empty,"C06":empty,"D06":empty,"E06":empty,"F06":empty,"G06":empty,"H06":empty,"I06":empty,"J06":empty,"K06":empty,
    "A05":empty,"B05":empty,"C05":empty,"D05":empty,"E05":empty,"F05":empty,"G05":empty,"H05":empty,"I05":empty,"J05":empty,"K05":empty,
    "A04":empty,"B04":empty,"C04":empty,"D04":empty,"E04":empty,"F04":empty,"G04":empty,"H04":empty,"I04":empty,"J04":empty,"K04":empty,
    "A03":empty,"B03":empty,"C03":empty,"D03":empty,"E03":empty,"F03":empty,"G03":empty,"H03":empty,"I03":empty,"J03":empty,"K03":empty,
    "A02":empty,"B02":empty,"C02":empty,"D02":empty,"E02":empty,"F02":empty,"G02":empty,"H02":empty,"I02":empty,"J02":empty,"K02":empty,
    "A01":empty,"B01":empty,"C01":empty,"D01":empty,"E01":empty,"F01":empty,"G01":empty,"H01":empty,"I01":empty,"J01":empty,"K01":empty,
    }

    def updateTaflBoard(self):
        global taflBoard

        jsonBoard = open("board.json", "r")

        taflBoard = json.loads(jsonBoard)

