# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:41:49 2020

@author: ashte
"""

import pandas as pd
import random

COLUMN=['APPOINTMENT_ID','NAME','AGE','GENDER','TREATMENT','PHYSICIAN','APPOINTMENT_DATE','ROOM','ISDISCHARGED' ]
COLUMN1= ['SYMPTOM','DISEASE_DIAGNOSED','TYPE','SCHEMES']
data1 = pd.DataFrame(columns = COLUMN)

NAME = ['Maxwell','Steve','Gary','Gale','Loren','Omar','Antony','Riley','Norberto','Brendan','Harley','Kirby','Allen','Robt','Pete','Kraig','Jamal','Teodoro','Charley','Miguel','Abram','Gavin','Gordon','Elton','Michael','Greg','Orlando','Ian','Virgilio']
type2= [['Bladder Cancer','Blood or blood clots in the urine,Pain or burning sensation during urination.','Cancer','Cancer Scheme Bladder'],
['Breast Cancer','New lump in the breast or underarm (armpit),Thickening or swelling of part of the breast.','Cancer','Cancer Scheme Breast'],
['Colon and Rectal Cancer','A change in bowel habits, such as diarrhea, constipation or more-frequent bowel movements','Cancer','Cancer Scheme Rectal'],
['Endometrial Cancer','Unusual vaginal bleeding, spotting, or other discharge','Cancer','Cancer Scheme Endometrical'],
['Kidney Cancer','Blood in the urine (hematuria),Low back pain on one side ','Cancer','Cancer Scheme Kidney'],
['Leukemia','Fever or chills, Persistent fatigue, weakness.','Cancer','Cancer Scheme Lukemia'],
['Liver Cancer','Weight loss (without trying),Loss of appetite.','Cancer','Cancer Scheme Liver'],
['Lung Cancer','Coughing up blood or rust-colored sputum','Cancer','Cancer Scheme Lung'],
['Melanoma','Spread of pigment from the border of a spot into surrounding skin','Cancer','Cancer Scheme Melanoma'],
['Non-Hodgkin Lymphoma','Enlarged lymph nodes,Chills.','Cancer','Cancer Scheme Lymphoma'],
['Pancreatic Cancer','Jaundice and related symptoms. Jaundice is yellowing of the eyes and skin.','Cancer','Cancer Scheme Pancrea'],
['Thyroid Cancer','A lump in the neck, sometimes growing quickly,Swelling in the neck.','Cancer','Cancer Scheme Thyroid'],
['Chronic Kidney disorder','Fatigue, difficulty concentrating','Kidney','kidney Scheme Chronic'],
['Kidney stone','Pain in lower abdomen,Poor apetite ','Kidney','Kidney Scheme'],
['Urinary Tract infection','Frequent urination, burning','Kidney','Kidney Scheme Stone'],
['Alzheimer’s disease','memory loss, basic thinking skills ','Brain','Brain Scheme Alzheimer'],
['Dementia','memory changes that disrupt daily life,problems with planning or problem solving','Brain','Brain Scheme Dementiaa'],
['Acne','Breakouts on the skin composed of blackheads, whiteheads, pimples, or deep, painful cysts and nodules','Skin','Skin Scheme Acne'],
['Cold Sore','Red, painful, fluid-filled blister that appears near the mouth and lips','Skin','Skin Scheme Cold score'],
['valvular heart disease','Irregular heartbeat,Swollen feet or ankles.Chest pain','Heart','Heart Scheme Valvular'],
['heart infections','Changes in your heart rhythm,Dry or persistent cough','Heart','Heart Scheme Infection'],
['weak heart muscle ','Breathlessness with exertion or at rest,Swelling of the legs, ankles and feet','Heart','Heart Scheme'],
['Heart Attack','pain in left side of chest,blockages','Heart','Heart Scheme'],
['Brain Tumor','ball of mass present in brain','Brain','Brain Scheme Tumor'],
['sugar','Frequent urination','sugar','Sugar Schema'],
['Common cold','Fever, cough,flu','common','Common Schemes'],
['HeadAche','pain in head','common','Common Schemes'],
['Endometriosis','Heavy periods, miscarriage','women','Women Disease Scheme Endometriosis'],
['Uterine fibroids','Heavy or painful periods or bleeding between periods,Lower back pain','women','Women Disease Scheme Fibroids'],
['Gynecologic cancer','Cervical cancer, ovarian cancer','women','Women Disease Scheme Cancer'],
['Interstitial cystitis','Abdominal or pelvic mild discomfort,Frequent urination.','women','Women Disease Scheme Cystitis'],
['Polycystic ovary syndrome','Pelvic pain,Excess hair growth on the face, chest, stomach, thumbs, or toes.','women','Women Disease PCOS'],
]
data2= pd.DataFrame(columns = COLUMN1)

GENDER = ['F','M']

TREATMENT=['MRI', 'CITI SCAN', 'BLOOD PRESSURE', 'SUGAR LEVEL','Lipid Panel','Liver Panel','sonography','scan']
IS_DISCHARGED = ['Y','N']



for i in range(0,2000):
    data1.loc[i]= [i,random.choice(NAME),random.randint(30,70),random.choice(GENDER),random.choice(TREATMENT),'On duty physician', 'null', random.randint(1,20),random.choice(IS_DISCHARGED)]


for j in range(0,2000):
    data2.loc[j]= random.choice(type2)
    
dataset = pd.concat([data1, data2], axis=1, sort=False)
dataset.to_csv("dataset.csv")





