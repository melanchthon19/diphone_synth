#!/usr/bin/env python3

from phonotactics import Phonotactics
from phonetics import phonetics


class Test:
    def __init__(self, Phonotactics, phonetics):
        self.ph = Phonotactics(phonetics, debug=True)
        self.results = []
        self.errors = 0
        self.sentences = {
            'petaca': 'pe-ta-ka',
            'sol': 'sol',
            'abuela': 'a-bue-la',
            'calabaza': 'ka-la-ba-sa',
            'calabaza con ají': 'ka-la-ba-sa-ko-na-xí',
            'amelia y petaca': 'a-me-liai-pe-ta-ka',
            'el chaleco del padre pérez': 'el-Xa-le-ko-del-pa-dre-pé-res',
            'mientras petaca atisba desde la puerta': 'mien-tras-pe-ta-ka-a-tis-ba-des-de-la-puer-ta',
            'cuando nos fuimos a ver nuevas variedades': 'kuan-do-nos-fui-mo-sa-ber-nue-bas-ba-rie-da-des',
            'cañuela encaramada sobre la mesa descuelga del muro el pesado y mohoso fusil': 'ka-ñue-la-en-ka-ra-ma-da-so-bre-la-me-sa-des-kuel-ga-del-mu-ro-el-pe-sa-doi-mo-o-so-fu-sil',
            'las rendijas del rancho eran superiores en cantidad y número': 'las-ren-di-xas-del-ran-Xo-e-ran-su-pe-rio-re-sen-kan-ti-da-di-nú-me-ro',
            'el choclo con manzana es de los más cachilupi don juan con lluvia y trenzas': 'el-Xo-klo-kon-man-sa-na-es-de-los-más-ka-Xi-lu-pi-don-xuan-kon-Lu-biai-tren-sas',
            'Apoyado en el codo, con el cuello doblado': 'a-po-ia-do-e-nel-ko-do-ko-nel-kue-Lo-do-bla-do',
            'golpeaba sin descanso, y a cada golpe el agua de la cortadura': 'gol-pe-a-ba-sin-des-kan-so-ia-ka-da-gol-pe-e-la-gua-de-la-kor-ta-du-ra',
            'le azotaba el rostro con gruesas gotas que herían sus pupilas como martillazos': 'le-a-so-ta-ba-el-ros-tro-kon-grue-sas-go-tas-ke-e-rí-an-sus-pu-pi-las-ko-mo-mar-ti-La-sos',
            'Deteníase entonces por un momento para desaguar el surco y empuñaba': 'de-te-ní-a-se-en-ton-ses-po-run-mo-men-to-pa-ra-de-sa-gua-rel-sur-ko-iem-pu-ña-ba',
            'de nuevo la piqueta sin cuidarse de la fatiga que engarrotaba': 'de-nue-bo-la-pi-ke-ta-sin-kui-dar-se-de-la-fa-ti-ga-ke-en-ga-Ro-ta-ba',
            'sus músculos, del ambiente irrespirable de aquel agujero, ni del lodo en que se hundía su cuerpo': 'sus-mús-ku-los-de-lam-bien-tei-Res-pi-ra-ble-de-a-ke-la-gu-xe-ro-ni-del-lo-do-en-ke-seun-dí-a-su-kuer-po',
            'acosado por una idea fija, obstinada': 'a-ko-sa-do-po-ru-nai-de-a-fi-xa-obs-ti-na-da',
            'de extraer ese día, el último de la quincena, el mayor número posible de carretillas;': 'de-eK-tra-e-re-se-dí-a-e-lúl-ti-mo-de-la-kin-se-na-el-ma-ior-nú-me-ro-po-si-ble-de-ka-Re-ti-Las',
            'y esa obsesión era tan poderosa, absorbía de tal modo sus facultades,': 'ie-sa-ob-se-sió-ne-ra-tan-po-de-ro-sa-ab-sor-bí-a-de-tal-mo-do-sus-fa-kul-ta-des',
            'que la tortura física le hacía el efecto de la espuela que desgarra': 'ke-la-tor-tu-ra-fí-si-ka-le-a-sí-a-e-le-fek-to-de-la-es-pue-la-ke-des-ga-Ra',
            'los ijares de un caballo desbocado': 'lo-si-xa-res-deun-ka-ba-Lo-des-bo-ka-do',
            'La llanura arenosa y estéril estaba desierta.': 'la-La-nu-ra-a-re-no-sa-ies-té-ri-les-ta-ba-de-sier-ta',
            'A la derecha, interrumpiendo su monótona uniformidad,': 'a-la-de-re-Xain-te-Rum-pien-do-su-mo-nó-to-nau-ni-for-mi-dad',
            'alzábanse los blancos muros de los galpones coronados': 'al-sá-ban-se-los-blan-kos-mu-ros-de-los-gal-po-nes-ko-ro-na-dos',
            'por las lisas techumbres de zinc relucientes por la lluvia.': 'por-las-li-sas-te-Xum-bres-de-sink-re-lu-sien-tes-por-la-Lu-bia', 
            'Y más allá, tocando casi las pesadas nubes, surgía de la enorme chimenea de la mina': 'i-má-sa-Lá-to-kan-do-ka-si-las-pe-sa-das-nu-bes-sur-xí-a-de-la-e-nor-me-Xi-me-ne-a-de-la-mi-na',
            'el negro penacho de humo, retorcido, desmenuzado por las rachas furibundas del septentrión.': 'el-ne-gro-pe-na-Xo-deu-mo-re-tor-si-do-des-me-nu-sa-do-por-las-ra-Xas-fu-ri-bun-das-del-sep-ten-trión',
            'La anciana, siempre medrosa e inquieta,': 'la-an-sia-na-siem-pre-me-dro-sa-ein-kie-ta',
            'después de un instante de observación pasó su delgado cuerpo': 'des-pués-deu-nins-tan-te-de-ob-ser-ba-sión-pa-só-su-del-ga-do-kuer-po',
            'por entre los alambres de la cerca que limitaba por ese': 'po-ren-tre-lo-sa-lam-bres-de-la-ser-ka-ke-li-mi-ta-ba-po-re-se',
            'lado los terrenos del establecimiento, y se encaminó en': 'la-do-los-te-Re-nos-de-les-ta-ble-si-mien-toi-se-en-ka-mi-nó-en',
            'línea recta hacia las habitaciones. De vez en cuando se inclinaba y recogía': 'lí-ne-a-rek-ta-a-sia-la-sa-bi-ta-sio-nes-de-be-sen-kuan-do-sein-kli-na-bai-Re-ko-xí-a',
            'la húmeda chamiza, astillas, ramas, raíces secas desparramadas en la arena,': 'la-ú-me-da-Xa-mi-sa-as-ti-Las-Ra-mas-Ra-íses-se-kas-des-pa-Ra-ma-da-sen-la-a-re-na',
            'con las que el registro': 'kon-las-ke-el-re-xis-tro',
        }
        

    def evaluate(self):
        self.results = [self.ph.word2silabas(sent) for sent in self.sentences.keys()]
        for res in self.results:
            for component in res:
                print(component)
            print()
        gold = list(self.sentences.values())
        for i,res in enumerate(self.results):
            if res[-1] != gold[i]:
                print(gold[i])
                print(res[-1])
                self.errors += 1
        print('Errors:', self.errors)
        
        



if __name__ == "__main__":
    test = Test(Phonotactics, phonetics)
    test.evaluate()