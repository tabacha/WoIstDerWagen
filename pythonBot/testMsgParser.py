
import msgParse
import logging
import unittest
log = logging.getLogger(__name__)

def testParse(msg, zugArt, zugNr, bahnhof, waggonNr):
    (zugArtParse, zugNrParse, bahnhofParse, waggonNrParse) = msgParse.parseMsg(msg)
    if (not((zugArtParse == zugArt) and (zugNrParse == zugNr) and (bahnhofParse == bahnhof) and (waggonNrParse == waggonNr))):
        print("FAILED msg %s ( Art: %s => %s ) (Nr: %s => %s ) (Bhf: %s => %s ) (Waggon: %s => %s ) " % (msg, zugArt, zugArtParse, zugNr, zugNrParse, bahnhof, bahnhofParse, waggonNr, waggonNrParse))

p=msgParse.parseMsg

class TestStringMethods(unittest.TestCase):
    def testParse1(self):
        self.assertEqual(p("?"),(None,None,'?',None))
    def testParse2(self):
        self.assertEqual(p("Bonn ec6 260"),('EC','6','Bonn', '260'))
    def testParse3(self):
        self.assertEqual(p("#ec6 Bonn wagen 260"),('EC','6','Bonn', '260'))
    def testParse4(self):
        self.assertEqual(p("en446 Wagen 268 Frankfurt(oder)"),('EN','446','Frankfurt(oder)', '268'))
    def testParse5(self):
        self.assertEqual(p("#IC144 Hannover Wagen 11"),('IC','144','Hannover','11'))
    def testParse6(self):
        self.assertEqual(p("IC145 Osnabrück Hbf Wagen 8"),('IC','145','Osnabrück Hbf','8'))
    def testParse7(self):
        self.assertEqual(p("#IC1955 Fulda Wagen12"),('IC','1955','Fulda','12'))
    def testParse8(self):
        self.assertEqual(p("#IC2061 Augsburg 10"),('IC','2061','Augsburg','10'))
    def testParse9(self):
        self.assertEqual(p("#IC2061 Augsburg 10 Wagen 10"),('IC','2061','Augsburg 10','10'))
    def testParse10(self):
        self.assertEqual(p("#IC2061 Augsburg Hbf Wagen 10"),('IC','2061','Augsburg Hbf','10'))
    def testParse10(self):
        self.assertEqual(p("#ic2267 272 karlsruhe"),('IC','2267','karlsruhe','272'))
    def testParse11(self):
        self.assertEqual(p("#ic2267 Karlsruhe 272"),('IC','2267','Karlsruhe','272'))
    def testParse12(self):
        self.assertEqual(p("IC2426 Wagen 5 berlin"),('IC','2426','berlin','5'))
    def testParse13(self):
        self.assertEqual(p("IC60456 Wagen 267 berlin"),('IC','60456','berlin','267'))
    def testParse14(self):
        self.assertEqual(p("#ICE1557 Fulda Wagen 27"),('ICE','1557','Fulda','27'))
    def testParse15(self):
        self.assertEqual(p("#ICE613 Köln Wagen 22"),('ICE','613','Köln','22'))
    def testParse16(self):
        self.assertEqual(p("#ICE614 Augsburg Wagen 25"),('ICE','614','Augsburg','25'))
    def testParse17(self):
        self.assertEqual(p("#ICE614 Augsburg Wagen 32"),('ICE','614','Augsburg','32'))
    def testParse18(self):
        self.assertEqual(p("ice674 hamburg 11"),('ICE','674','hamburg','11'))
    def testParse19(self):
        self.assertEqual(p("#ICE674 Hamburg Wagen 11"),('ICE','674','Hamburg','11'))
    def testParse20(self):
        self.assertEqual(p("#ice725 Aschaffenburg Wagen 23"),('ICE','725','Aschaffenburg','23'))
    def testParse21(self):
        self.assertEqual(p("#ICE725 Frankfurt Wagen 23"),('ICE','725','Frankfurt','23'))
    def testParse22(self):
        self.assertEqual(p("#ICE725 Köln Wagen 33"),('ICE','725','Köln','33'))
    def testParse23(self):
        self.assertEqual(p("ICE 732 Frankfurt Wagen 34"),('ICE','732','Frankfurt','34'))
    def testParse24(self):
        self.assertEqual(p("mag dich scheinbar nicht *g*"),(None, None, 'mag dich scheinbar nicht *g*', None))
    def testParse25(self):
        self.assertEqual(p("Wagen 34 EN 732 Frankfurt"),('EN','732','Frankfurt','34'))
    def testParse26(self):
        self.assertEqual(p("Wagen 34 #EN 732 Frankfurt"),('EN','732','Frankfurt','34'))

if __name__ == '__main__':
    unittest.main()
