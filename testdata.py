from datetime import datetime
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


TEST_DATA = {
    "0": {
        "dataid": "0",
        "DATA": [
            {
                'intent': {
                    'name': 'g-info-1',
                    'confidence': 0.8357323894595907
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 8,
                        "value": "shrimp &",
                        "entity": "prep-op-2",
                        "confidence": 0.2946872999748379,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 9,
                        "end": 19,
                        "value": "black bean",
                        "entity": "ing-name-2",
                        "confidence": 0.30886753140122913,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'g-info-1',
                        'confidence': 0.8357323894595907
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.12212217519811293
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.032442109027989316
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.009703326314306815
                    }
                ],
                'text': 'Shrimp & black bean quesadillas.'
            },
            {
                'intent': {
                    'name': 'g-info-1',
                    'confidence': 0.7678938634466098
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 5,
                        "value": "makes",
                        "entity": "g-i-size-2",
                        "confidence": 0.3563294985707146,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 6,
                        "end": 15,
                        "value": "12 pieces",
                        "entity": "ing-quant-2",
                        "confidence": 0.4106697878101274,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'g-info-1',
                        'confidence': 0.7678938634466098
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.14841808974387313
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.06870293019422404
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.014985116615293238
                    }
                ],
                'text': 'Makes 12 pieces.'
            },
            {
                'intent': {
                    'name': 'g-info-1',
                    'confidence': 0.43338222226317913
                },
                'entities': [],
                'intent_ranking': [
                    {
                        'name': 'g-info-1',
                        'confidence': 0.43338222226317913
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.2956837356721099
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.210734716329169
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.0601993257355421
                    }
                ],
                'text': 'Difficulty.'
            },
            {
                'intent': {
                    'name': 'g-info-1',
                    'confidence': 0.7790934445941843
                },
                'entities': [],
                'intent_ranking': [
                    {
                        'name': 'g-info-1',
                        'confidence': 0.7790934445941843
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.20122974362722573
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.014862679420098467
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.004814132358491749
                    }
                ],
                'text': 'Not too tricky.'
            },
            {
                'intent': {
                    'name': 'nut-1',
                    'confidence': 0.9100677434359897
                },
                'entities': [],
                'intent_ranking': [
                    {
                        'name': 'nut-1',
                        'confidence': 0.9100677434359897
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.04668722880178984
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.02541555241495377
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.01782947534726656
                    }
                ],
                'text': 'Nutrition per serving.'
            },
            {
                'intent': {
                    'name': 'nut-1',
                    'confidence': 0.9527027974337191
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 8,
                        "value": "calories",
                        "entity": "nut-type-2",
                        "confidence": 0.8588587327774114,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'nut-1',
                        'confidence': 0.9527027974337191
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.026428279858442455
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.01482797021155938
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.006040952496278726
                    }
                ],
                'text': 'Calories 201 10%.'
            },
            {
                'intent': {
                    'name': 'nut-1',
                    'confidence': 0.9198460735479972
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 3,
                        "value": "fat",
                        "entity": "nut-type-2",
                        "confidence": 0.9247468794727762,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 4,
                        "end": 7,
                        "value": "10 g",
                        "entity": "nut-quant-2",
                        "confidence": 0.903556986269021,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 8,
                        "end": 11,
                        "value": "14 %",
                        "entity": "nut-perc-2",
                        "confidence": 0.9301318553607852,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'nut-1',
                        'confidence': 0.9198460735479972
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.03411869682754795
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.0314923706056668
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.014542859018788342
                    }
                ],
                'text': 'Fat 10g 14%.'
            },
            {
                'intent': {
                    'name': 'nut-1',
                    'confidence': 0.9011110718940383
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 9,
                        "value": "saturates",
                        "entity": "nut-type-2",
                        "confidence": 0.8609051275325594,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 10,
                        "end": 14,
                        "value": "5,3 g",
                        "entity": "nut-quant-2",
                        "confidence": 0.8827472502004647,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 15,
                        "end": 18,
                        "value": "27 %",
                        "entity": "nut-perc-2",
                        "confidence": 0.9254196626562288,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'nut-1',
                        'confidence': 0.9011110718940383
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.047649943526731235
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.043935372684262605
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.007303611894967789
                    }
                ],
                'text': 'Saturates 5,3g 27%.'
            },
            {
                'intent': {
                    'name': 'nut-1',
                    'confidence': 0.9565790210805897
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 7,
                        "value": "protein",
                        "entity": "nut-type-2",
                        "confidence": 0.9060679849547116,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 8,
                        "end": 13,
                        "value": "12,4 g",
                        "entity": "nut-quant-2",
                        "confidence": 0.897254798975432,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 14,
                        "end": 17,
                        "value": "25 %",
                        "entity": "nut-perc-2",
                        "confidence": 0.9198714053954636,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'nut-1',
                        'confidence': 0.9565790210805897
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.02228488862314458
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.016716099329963558
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.004419990966302066
                    }
                ],
                'text': 'Protein 12,4g 25%.'
            },
            {
                'intent': {
                    'name': 'nut-1',
                    'confidence': 0.9310820986526122
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 5,
                        "value": "carbs",
                        "entity": "nut-type-2",
                        "confidence": 0.8494622792340647,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 6,
                        "end": 11,
                        "value": "14,3 g",
                        "entity": "nut-quant-2",
                        "confidence": 0.8721522243709535,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 12,
                        "end": 14,
                        "value": "6 %",
                        "entity": "nut-perc-2",
                        "confidence": 0.8961816004168511,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'nut-1',
                        'confidence': 0.9310820986526122
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.042878432826517654
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.017294508544674122
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.008744959976196034
                    }
                ],
                'text': 'Carbs 14,3g 6%.'
            },
            {
                'intent': {
                    'name': 'nut-1',
                    'confidence': 0.9291864013837634
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 6,
                        "value": "sugars",
                        "entity": "nut-type-2",
                        "confidence": 0.7854219731905052,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 7,
                        "end": 11,
                        "value": "0,6 g",
                        "entity": "nut-quant-2",
                        "confidence": 0.8326297601132875,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 12,
                        "end": 14,
                        "value": "1 %",
                        "entity": "nut-perc-2",
                        "confidence": 0.8617350879277379,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'nut-1',
                        'confidence': 0.9291864013837634
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.054200714184292176
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.009244469271121995
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.007368415160822355
                    }
                ],
                'text': 'Sugars 0,6g 1%.'
            },
            {
                'intent': {
                    'name': 'nut-1',
                    'confidence': 0.7720195120531921
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 5,
                        "value": "fibre",
                        "entity": "nut-type-2",
                        "confidence": 0.19444598977825156,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 6,
                        "end": 10,
                        "value": "4,3 g",
                        "entity": "nut-quant-2",
                        "confidence": 0.25049920231691075,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'nut-1',
                        'confidence': 0.7720195120531921
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.1333173735771113
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.05494862308060307
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.0397144912890935
                    }
                ],
                'text': "Fibre 4,3g - Of an adult's reference intake."
            },
            {
                'intent': {
                    'name': 'ing-1',
                    'confidence': 0.8662867189310811
                },
                'entities': [],
                'intent_ranking': [
                    {
                        'name': 'ing-1',
                        'confidence': 0.8662867189310811
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.0681122459031471
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.034114678070501975
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.03148635709526944
                    }
                ],
                'text': 'Ingredients.'
            },
            {
                'intent': {
                    'name': 'ing-1',
                    'confidence': 0.5313848008141414
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 5,
                        "value": "200 g",
                        "entity": "ing-quant-2",
                        "confidence": 0.7709895763180951,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 6,
                        "end": 11,
                        "value": "large",
                        "entity": "ing-quant-2",
                        "confidence": 0.4354783064919301,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 12,
                        "end": 22,
                        "value": "raw prawns",
                        "entity": "ing-name-2",
                        "confidence": 0.5360367195192486,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'ing-1',
                        'confidence': 0.5313848008141414
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.28298732476791577
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.10108497945807257
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.08454289495987023
                    }
                ],
                'text': '200 g large raw prawns , from sustainable sources.'
            },
            {
                'intent': {
                    'name': 'ing-1',
                    'confidence': 0.9927523470762296
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 12,
                        "value": "1 tablespoon",
                        "entity": "ing-quant-2",
                        "confidence": 0.9583663843476958,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 13,
                        "end": 27,
                        "value": "smoked paprika",
                        "entity": "ing-name-2",
                        "confidence": 0.48969205997476595,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'ing-1',
                        'confidence': 0.9927523470762296
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.005648503707341595
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.00088730949647299
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.0007118397199557779
                    }
                ],
                'text': '1 tablespoon smoked paprika.'
            },
            {
                'intent': {
                    'name': 'ing-1',
                    'confidence': 0.9329552962600853
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 12,
                        "value": "1 tablespoon",
                        "entity": "ing-quant-2",
                        "confidence": 0.9695159636152612,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 13,
                        "end": 26,
                        "value": "vegetable oil",
                        "entity": "ing-name-2",
                        "confidence": 0.7768118289176958,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'ing-1',
                        'confidence': 0.9329552962600853
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.05626276423706232
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.00933961238819734
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.0014423271146546857
                    }
                ],
                'text': '1 tablespoon vegetable oil.'
            },
            {
                'intent': {
                    'name': 'ing-1',
                    'confidence': 0.7799507953527091
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 5,
                        "value": "250 g",
                        "entity": "ing-quant-2",
                        "confidence": 0.7691029184618731,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 6,
                        "end": 12,
                        "value": "mature",
                        "entity": "ing-name-2",
                        "confidence": 0.3289166454498302,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 13,
                        "end": 27,
                        "value": "cheddar cheese",
                        "entity": "ing-name-2",
                        "confidence": 0.45852843429722007,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'ing-1',
                        'confidence': 0.7799507953527091
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.16732393726282407
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.042431624991776454
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.010293642392690558
                    }
                ],
                'text': '250 g mature cheddar cheese.'
            },
            {
                'intent': {
                    'name': 'ing-1',
                    'confidence': 0.983125717499028
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 1,
                        "value": "4",
                        "entity": "ing-quant-2",
                        "confidence": 0.8838675713010887,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 2,
                        "end": 7,
                        "value": "large",
                        "entity": "ing-quant-2",
                        "confidence": 0.7335923882908728,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 8,
                        "end": 23,
                        "value": "flour tortillas",
                        "entity": "ing-name-2",
                        "confidence": 0.475311143774274,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'ing-1',
                        'confidence': 0.983125717499028
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.009463292389361574
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.0060338524722048925
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.0013771376394056127
                    }
                ],
                'text': '4 large flour tortillas.'
            },
            {
                'intent': {
                    'name': 'ing-1',
                    'confidence': 0.8377510293080016
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 5,
                        "value": "400 g",
                        "entity": "ing-quant-2",
                        "confidence": 0.9684532906687199,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 6,
                        "end": 17,
                        "value": "black beans",
                        "entity": "ing-name-2",
                        "confidence": 0.9645898294162998,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'ing-1',
                        'confidence': 0.8377510293080016
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.07062347394379277
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.06102148872002337
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.03060400802818226
                    }
                ],
                'text': '400 g black beans.'
            },
            {
                'intent': {
                    'name': 'ing-1',
                    'confidence': 0.6406245101091429
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 13,
                        "value": "4 tablespoons",
                        "entity": "ing-quant-2",
                        "confidence": 0.9742880472571819,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 14,
                        "end": 21,
                        "value": "pickled",
                        "entity": "ing-form-2",
                        "confidence": 0.5267064051901812,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'ing-1',
                        'confidence': 0.6406245101091429
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.3237243651146282
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.030728890615707594
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.004922234160521478
                    }
                ],
                'text': '4 tablespoons pickled jalapeños , plus extra to serve.'
            },
            {
                'intent': {
                    'name': 'ing-1',
                    'confidence': 0.5656458904142322
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 13,
                        "value": "2 tablespoons",
                        "entity": "ing-quant-2",
                        "confidence": 0.9792320560659179,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 14,
                        "end": 23,
                        "value": "coriander",
                        "entity": "ing-name-2",
                        "confidence": 0.9065786229085425,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'ing-1',
                        'confidence': 0.5656458904142322
                    },
                    {
                        'name': 'prep-1',
                        'confidence': 0.41933818975086795
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.009083046246577792
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.00593287358832199
                    }
                ],
                'text': '2 tablespoons coriander , plus extra to serve.'
            },
            {
                'intent': {
                    'name': 'prep-1',
                    'confidence': 0.5157529605906025
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 10,
                        "value": "sour cream",
                        "entity": "ing-name-2",
                        "confidence": 0.7131825910989444,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 15,
                        "end": 20,
                        "value": "salsa",
                        "entity": "ing-name-2",
                        "confidence": 0.5051778833592836,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 23,
                        "end": 31,
                        "value": "to serve",
                        "entity": "ing-purp-2",
                        "confidence": 0.6904955257414587,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'prep-1',
                        'confidence': 0.5157529605906025
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.40006117145460285
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.07845500330142872
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.005730864653366071
                    }
                ],
                'text': 'sour cream and salsa , to serve.'
            },
            {
                'intent': {
                    'name': 'prep-1',
                    'confidence': 0.9649494339030334
                },
                'entities': [],
                'intent_ranking': [
                    {
                        'name': 'prep-1',
                        'confidence': 0.9649494339030334
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.014765836454383296
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.012893869582260157
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.007390860060322845
                    }
                ],
                'text': 'Method.'
            },
            {
                'intent': {
                    'name': 'prep-1',
                    'confidence': 0.9039880705378603
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 15,
                        "value": "in a small bowl",
                        "entity": "prep-met-2",
                        "confidence": 0.9804865488080221,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 17,
                        "end": 21,
                        "value": "toss",
                        "entity": "prep-op-2",
                        "confidence": 0.9740588396075012,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 26,
                        "end": 32,
                        "value": "prawns",
                        "entity": "ing-name-2",
                        "confidence": 0.6917582537591719,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 33,
                        "end": 56,
                        "value": "with the smoked paprika",
                        "entity": "prep-met-2",
                        "confidence": 0.900170412629879,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 66,
                        "end": 70,
                        "value": "salt",
                        "entity": "ing-name-2",
                        "confidence": 0.8777502506339309,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 75,
                        "end": 81,
                        "value": "pepper",
                        "entity": "ing-name-2",
                        "confidence": 0.9593998727064194,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'prep-1',
                        'confidence': 0.9039880705378603
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.05092093766093944
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.042800729965687914
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.00229026183551226
                    }
                ],
                'text': 'In a small bowl, toss the prawns with the smoked paprika and some salt and pepper.'
            },
            {
                'intent': {
                    'name': 'prep-1',
                    'confidence': 0.9537057626906291
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 23,
                        "value": "heat a small frying pan",
                        "entity": "prep-op-2",
                        "confidence": 0.6688252842980399,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 29,
                        "end": 39,
                        "value": "1 teaspoon",
                        "entity": "ing-quant-2",
                        "confidence": 0.9603900481768416,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 47,
                        "end": 50,
                        "value": "oil",
                        "entity": "ing-name-2",
                        "confidence": 0.9479835751496193,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'prep-1',
                        'confidence': 0.9537057626906291
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.04300704761110354
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.002281106221095518
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.0010060834771717419
                    }
                ],
                'text': 'Heat a small frying pan with 1 teaspoon of the oil.'
            },
            {
                'intent': {
                    'name': 'prep-1',
                    'confidence': 0.9390229213616851
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 4,
                        "value": "sear",
                        "entity": "prep-op-2",
                        "confidence": 0.5675038891609016,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 20,
                        "end": 28,
                        "value": "1 minute",
                        "entity": "prep-dur-2",
                        "confidence": 0.5731070676108507,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'prep-1',
                        'confidence': 0.9390229213616851
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.03611079319984131
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.020620233427928417
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.004246052010545246
                    }
                ],
                'text': 'Sear the prawns for 1 minute each side.'
            },
            {
                'intent': {
                    'name': 'prep-1',
                    'confidence': 0.9954475006755854
                },
                'entities': [
                    {
                        "start": 8,
                        "end": 16,
                        "value": "let cool",
                        "entity": "prep-op-2",
                        "confidence": 0.8231565933210696,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'prep-1',
                        'confidence': 0.9954475006755854
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.0027730733840643754
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.000939863263928327
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.0008395626764219891
                    }
                ],
                'text': 'Remove, let cool and halve lengthways.'
            },
            {
                'intent': {
                    'name': 'prep-1',
                    'confidence': 0.9207712714894193
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 9,
                        "value": "set aside",
                        "entity": "prep-op-2",
                        "confidence": 0.7162752176579408,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'prep-1',
                        'confidence': 0.9207712714894193
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.06931239007886991
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.008207437292729193
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.0017089011389814772
                    }
                ],
                'text': 'Set aside.'
            },
            {
                'intent': {
                    'name': 'prep-1',
                    'confidence': 0.8349760329650123
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 6,
                        "value": "spread",
                        "entity": "prep-op-2",
                        "confidence": 0.5781659458073979,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 7,
                        "end": 11,
                        "value": "half",
                        "entity": "ing-quant-2",
                        "confidence": 0.5404328666448275,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 19,
                        "end": 25,
                        "value": "cheese",
                        "entity": "ing-name-2",
                        "confidence": 0.6669200666013286,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 26,
                        "end": 44,
                        "value": "over two tortillas",
                        "entity": "prep-met-2",
                        "confidence": 0.8907866846437634,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'prep-1',
                        'confidence': 0.8349760329650123
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.08883243996415842
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.07273382722470498
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.003457699846124042
                    }
                ],
                'text': 'Spread half of the cheese over two tortillas.'
            },
            {
                'intent': {
                    'name': 'prep-1',
                    'confidence': 0.9763622660689267
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 5,
                        "value": "drain",
                        "entity": "prep-op-2",
                        "confidence": 0.6925606634336845,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 10,
                        "end": 15,
                        "value": "beans",
                        "entity": "ing-name-2",
                        "confidence": 0.7408336183933444,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 28,
                        "end": 32,
                        "value": "chop",
                        "entity": "prep-op-2",
                        "confidence": 0.7321198369641837,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 37,
                        "end": 46,
                        "value": "jalapeños",
                        "entity": "ing-name-2",
                        "confidence": 0.7686221900357325,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 53,
                        "end": 61,
                        "value": "sprinkle",
                        "entity": "prep-op-2",
                        "confidence": 0.828516725400611,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'prep-1',
                        'confidence': 0.9763622660689267
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.01416329322116024
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.007966579945824682
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.0015078607640883746
                    }
                ],
                'text': 'Drain the beans and roughly chop the jalapeños, then sprinkle over, along with the prawns.'
            },
            {
                'intent': {
                    'name': 'prep-1',
                    'confidence': 0.9743984253173005
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 6,
                        "value": "finely",
                        "entity": "prep-met-2",
                        "confidence": 0.6027702636428418,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 7,
                        "end": 11,
                        "value": "chop",
                        "entity": "prep-op-2",
                        "confidence": 0.9108996386829664,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 16,
                        "end": 25,
                        "value": "coriander",
                        "entity": "ing-name-2",
                        "confidence": 0.9746523587610182,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 32,
                        "end": 38,
                        "value": "divide",
                        "entity": "prep-op-2",
                        "confidence": 0.3039125631565771,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 51,
                        "end": 60,
                        "value": "tortillas",
                        "entity": "ing-name-2",
                        "confidence": 0.5806453377304741,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 62,
                        "end": 67,
                        "value": "cover",
                        "entity": "prep-op-2",
                        "confidence": 0.8373077521190713,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 68,
                        "end": 93,
                        "value": "with the remaining cheese",
                        "entity": "prep-met-2",
                        "confidence": 0.456828009323442,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 98,
                        "end": 101,
                        "value": "top",
                        "entity": "prep-op-2",
                        "confidence": 0.8676014778602691,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 102,
                        "end": 126,
                        "value": "with the other tortillas",
                        "entity": "prep-met-2",
                        "confidence": 0.6181736775164633,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'prep-1',
                        'confidence': 0.9743984253173005
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.01678032074888925
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.00702379956211622
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.0017974543716941026
                    }
                ],
                'text': 'Finely chop the coriander, then divide between the tortillas, cover with the remaining cheese and top with the other tortillas.'
            },
            {
                'intent': {
                    'name': 'prep-1',
                    'confidence': 0.9857794820842136
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 6,
                        "value": "divide",
                        "entity": "prep-op-2",
                        "confidence": 0.9367710596321613,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 23,
                        "end": 26,
                        "value": "oil",
                        "entity": "ing-name-2",
                        "confidence": 0.9476551784339632,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 27,
                        "end": 50,
                        "value": "between two frying pans",
                        "entity": "prep-met-2",
                        "confidence": 0.7330286693801323,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 55,
                        "end": 65,
                        "value": "place them",
                        "entity": "prep-op-2",
                        "confidence": 0.9132819904551509,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 66,
                        "end": 88,
                        "value": "over a low – medium heat",
                        "entity": "prep-met-2",
                        "confidence": 0.5729031493366381,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'prep-1',
                        'confidence': 0.9857794820842136
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.006797998685813642
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.004184898195400257
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.0032376210345725375
                    }
                ],
                'text': 'Divide the rest of the oil between two frying pans and place them over a low–medium heat.'
            },
            {
                'intent': {
                    'name': 'prep-1',
                    'confidence': 0.9521517651835734
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 5,
                        "value": "brown",
                        "entity": "prep-op-2",
                        "confidence": 0.624335833906961,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 10,
                        "end": 19,
                        "value": "tortillas",
                        "entity": "ing-name-2",
                        "confidence": 0.4059079396194886,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 20,
                        "end": 31,
                        "value": "on one side",
                        "entity": "prep-met-2",
                        "confidence": 0.5779498301970977,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 36,
                        "end": 50,
                        "value": "3 to 4 minutes",
                        "entity": "prep-dur-2",
                        "confidence": 0.8645891342369044,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 52,
                        "end": 89,
                        "value": "until the cheese is melted and golden",
                        "entity": "prep-cond-2",
                        "confidence": 0.7112230706942562,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'prep-1',
                        'confidence': 0.9521517651835734
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.03378194121572006
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.011452994489847714
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.0026132991108588403
                    }
                ],
                'text': 'Brown the tortillas on one side for 3 to 4 minutes, until the cheese is melted and golden, taking care not to let them burn.'
            },
            {
                'intent': {
                    'name': 'prep-1',
                    'confidence': 0.9704606110035121
                },
                'entities': [
                    {
                        "start": 19,
                        "end": 23,
                        "value": "cook",
                        "entity": "prep-op-2",
                        "confidence": 0.9802294360073132,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 28,
                        "end": 37,
                        "value": "3 minutes",
                        "entity": "prep-dur-2",
                        "confidence": 0.9368158409924705,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'prep-1',
                        'confidence': 0.9704606110035121
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.026165196740026687
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.002213635392331085
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.0011605568641301586
                    }
                ],
                'text': 'Turn them over and cook for 3 minutes.'
            },
            {
                'intent': {
                    'name': 'prep-1',
                    'confidence': 0.9574907676393667
                },
                'entities': [
                    {
                        "start": 22,
                        "end": 30,
                        "value": "a little",
                        "entity": "ing-quant-2",
                        "confidence": 0.7640892366889283,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 31,
                        "end": 34,
                        "value": "dry",
                        "entity": "ing-name-2",
                        "confidence": 0.6944164683802132,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 36,
                        "end": 60,
                        "value": "add another tiny drizzle",
                        "entity": "prep-op-2",
                        "confidence": 0.30555478354087184,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 64,
                        "end": 77,
                        "value": "vegetable oil",
                        "entity": "ing-name-2",
                        "confidence": 0.35771675797126096,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'prep-1',
                        'confidence': 0.9574907676393667
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.020282617743715894
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.017731763983699078
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.0044948506332181904
                    }
                ],
                'text': 'If the pan is looking a little dry, add another tiny drizzle of vegetable oil.'
            },
            {
                'intent': {
                    'name': 'prep-1',
                    'confidence': 0.9673933415821766
                },
                'entities': [
                    {
                        "start": 0,
                        "end": 4,
                        "value": "once",
                        "entity": "prep-op-2",
                        "confidence": 0.7929398012510178,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 9,
                        "end": 15,
                        "value": "cheese",
                        "entity": "ing-name-2",
                        "confidence": 0.3235964577359888,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 28,
                        "end": 63,
                        "value": "remove the quesadillas from the pan",
                        "entity": "prep-op-2",
                        "confidence": 0.4864285184119809,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 68,
                        "end": 80,
                        "value": "cut each one",
                        "entity": "prep-op-2",
                        "confidence": 0.6736742650287608,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 81,
                        "end": 99,
                        "value": "into six triangles",
                        "entity": "prep-met-2",
                        "confidence": 0.7650805363527271,
                        "extractor": "ner_crf"
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'prep-1',
                        'confidence': 0.9673933415821766
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.022046148548507616
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.008838516403333817
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.0017219934659821257
                    }
                ],
                'text': 'Once the cheese has melted, remove the quesadillas from the pan and cut each one into six triangles.'
            },
            {
                'intent': {
                    'name': 'prep-1',
                    'confidence': 0.5615254752927695
                },
                'entities': [
                    {
                        "start": 21,
                        "end": 27,
                        "value": "topped",
                        "entity": "prep-op-2",
                        "confidence": 0.5057518113557856,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 28,
                        "end": 41,
                        "value": "with a dollop",
                        "entity": "prep-met-2",
                        "confidence": 0.5539044300113334,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 45,
                        "end": 55,
                        "value": "sour cream",
                        "entity": "ing-name-2",
                        "confidence": 0.6734687484924944,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 60,
                        "end": 65,
                        "value": "salsa",
                        "entity": "ing-name-2",
                        "confidence": 0.5045355267543106,
                        "extractor": "ner_crf"
                    },
                    {
                        "start": 71,
                        "end": 78,
                        "value": "pickled",
                        "entity": "ing-name-2",
                        "confidence": 0.24321186294259792,
                        "extractor": "ner_crf"
                    },
                    {
                        'start': 93,
                        'end': 109,
                        'value': 'coriander leaves',
                        'entity': 'ing-name-2',
                        'confidence': 0.8622208729599671,
                        'extractor': 'ner_crf'
                    }
                ],
                'intent_ranking': [
                    {
                        'name': 'prep-1',
                        'confidence': 0.5615254752927695
                    },
                    {
                        'name': 'g-info-1',
                        'confidence': 0.29988417747990187
                    },
                    {
                        'name': 'ing-1',
                        'confidence': 0.13275235253489343
                    },
                    {
                        'name': 'nut-1',
                        'confidence': 0.005837994692435149
                    }
                ],
                'text': 'Serve straight away, topped with a dollop of sour cream and salsa, the pickled jalapeños and coriander leaves.'
            }
        ],
        "timestamp": get_timestamp(),
    },
}


def read_all():
    return [TEST_DATA[key] for key in sorted(TEST_DATA.keys())]


def read_one(dataid):
    if dataid in TEST_DATA:
        t_data = TEST_DATA.get(dataid)
    else:
        abort(
            404, "dataid {dataid} not found".format(dataid=dataid)
        )
    return t_data


def read_latest():
    dataid = -1
    for key in TEST_DATA:
        dataid += 1
    dataid = str(dataid)
    if dataid in TEST_DATA:
        t_data = TEST_DATA.get(dataid)
    else:
        abort(
            404, "dataid {dataid} not found".format(dataid=dataid)
        )
    return t_data


def delete(dataid):
    if dataid in TEST_DATA:
        del TEST_DATA[dataid]
        return make_response(
            "{dataid} successfully deleted".format(dataid=dataid), 200
        )
    else:
        abort(
            404, "dataid {dataid} not found".format(dataid=dataid)
        )
