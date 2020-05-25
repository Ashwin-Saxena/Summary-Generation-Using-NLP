#DATED : 11 MARCH 2019
#importing libraries
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
import bs4 as BeautifulSoup
import urllib.request  

article_content = ''

#providing custom text
article_content="""

Introduction Proximal femoral osteotomy plays a significant role in the treatment of several hip disorders in children [1–3]. The indications are wide and varied, such as Legg–Calve–Perthes disease, developmental dysplasia of the hip (DDH), idio- pathic increased femoral anteversion, slipped capital femoral epiphysis, and hip subluxation or dislocation in neuromus- cular diseases, but the most common indication is cerebral palsy [4–9]. Conventionally, the blade plate (BP) has been used as this procedure is relatively quick and uncomplicated to perform. However, the pediatric locking compression plate (LCP) has recently been applied widely. It supports strong angular stability even if patients have severe osteo- porosis [10–12]. However, the LCP procedure involves a longer operation and greater blood loss than a conventional BP [12]. There are many hardware-related complications after a proximal femoral osteotomy, such as implant-related 
fractures, loss of fixation around the plate, plate or screw breakage, nonunion, or delayed union [13]. 
Although several studies have shown the strengths and weaknesses of these plates, relatively few have evaluated the complications during the follow-up period after sur- gery. A few retrospective studies included very few operations. Therefore, we compared the outcomes of proximal femoral osteotomies using the conventional BP or the pediatric LCP by focusing on hardware-related complications and also the factors influencing these complications in patients who have undergone proximal femoral osteotomy. 
Patients and methods This retrospective study was approved by the institutional review board at our hospital (IRB no: B-1503/292-101). 

Hardware-related complications after proximal femoral osteotomy Chung et al. 265 
The need for informed consent was waived because of the 
Picture Archiving and Communication System (Impax; Agfa, retrospective nature of the study. We included patients 
Mortsel, Belgium). who fulfilled the following criteria: (a) aged less than or equal to 20 years and visited our hospital from May 2003 
Consensus building to December 2014, (b) had undergone a surgery including 
A consensus-building session involving five orthopedic a proximal femoral osteotomy (femoral varization derota- 
surgeons with 31, 15, 13, 11, and 10 years of orthopedic tional osteotomy or femoral derotational osteotomy) with 
experience, respectively, took place to define hardware- BP or LCP, (c) had been followed up until 6 months after 
related complications. Previous studies were reviewed hardware removal, (d) had preoperative and immediate 
[12–23], and one of the authors (M.K.C.) pooled eight postoperative hip radiographs and follow-up radiographs 
events relevant to the category of hardware-related until hardware removal, and (e) diagnosed with cerebral 
complications: implant-related fracture, loss of fixation palsy, Legg–Calve–Perthes disease, DDH, or idiopathic 
around the plate, plate or screw breakage, nonunion, increased femoral anteversion. Exclusion criteria were as 
delayed union, heterotopic ossification, skin irritation follows (a) patients who had undergone an operation 
because of plate protuberance, and avascular necrosis of without BP or LCP or with additional other surgical fixa- 
the femoral head on hip radiographs. The consensus tion instruments, and (b) those who had inadequate 
panel considered the close causal relationship between radiographs for review (Fig. 1). 
Demographic and clinical data, including patient age, sex, 
the type of plate and problem as the most important criterion when choosing which to include in this study. Therefore, we focused on the mechanical problems of disease, side (right or left) of hip, Gross Motor Functional 
plates. In case of vague standards for judgment or too Classification System (GMFCS) level in cerebral palsy, 
many causes, we excluded the problem. The scoring operation details, and complications, were obtained from the 
method was used to reach an agreement. The panels hospital’s Electronic Medical Record and Information 
casted a vote on ‘certain relationship’ or ‘vague or no System. We reviewed hip radiographs to detect hardware- 
relationship’. Only unanimous votes for certain relation- related mechanical complications throughout the follow-up 
ship could be passed. Finally, four events were included period. Hip radiographs were obtained from the hospital’s 
by consensus of the panel: (a) an implant-related fracture 
Fig. 1 
Inclusion and exclusion criteria. BP, blade plate; DDH, developmental dysplasia of the hip; FDO, femoral derotational osteotomy; FVDO, femoral varization derotational osteotomy; GMFCS, Gross Motor Function Classification System; LCP, locking compression plate. 
Copyright r 2018 Wolters Kluwer Health, Inc. All rights reserved. 

266 Journal of Pediatric Orthopaedics B 2018, Vol 27 No 3 
involving peri-implant fractures and proximal femoral 
the distal part of the femur was fixed with at least two fractures in the acute phase within 6 months after hard- 
locking screws and one cortical compression screw. ware removal. [13,18,22,24]; (b) loss of fixation around the plate (caused by events such as loss of angular cor- rection or plate pulling); (c) plate or screw breakage; and (d) nonunion, defined as a failure to achieve bony union at 6 months following fixation [25,26]. Delayed union, heterotopic ossification, avascular necrosis of the femoral head, and skin irritation were considered inadequate and insufficient to reflect a hardware-related problem and were excluded by consensus on that basis [27]. 
Copyright r 2018 Wolters Kluwer Health, Inc. All rights reserved. 
In the BP group, immobilization with a short leg cast with a bar was applied to all patients, except those with a hip spica cast, for about 4–6 weeks after surgery. In the LCP group, if only a proximal femoral osteotomy was per- formed, patients did not use a cast or a brace routinely. If the osteotomy was performed in combination with other surgical procedures, such as periacetabular osteotomy or adductor tenotomy, a brace or a cast was used according to the postoperative protocol of the other procedure. In To reflect bone health, diseases were classified into two 
case of DDH with open reduction and femoral varization categories: poor bone health and normal bone health. 
osteotomy, a hip spica cast was applied to both groups. Cerebral palsy patients tend to have bone deficits, even if they are GMFCS level I or II. Therefore, we classified cerebral palsy patients into the poor bone health category [28–30]. Specifically, patients without problem in bone quality other than pathologic femur lesions were inclu- ded in the category of normal bone health. This category contained Legg–Calve–Perthes disease, DDH, and idiopathic increased femoral anteversion. 
Statistical analysis Descriptive statistics such as mean and SD were used to summarize the patient demographics. The χ2 test or Fisher’s exact test was used to compare categorical vari- ables such as the number of complications. This study included bilateral cases. Therefore, the incidence of complications was analyzed depending on the number of patients in bilateral cases, and also among cases, a gen- Operative protocol 
eralized estimating equation (GEE) was adopted to Proximal femoral osteotomy was performed by two 
ensure statistical independence [31]. pediatric surgeons (C.Y.C. and M.S.P.) with 27 and 11 years of experience in pediatric orthopedics, respec- tively. Both surgeons followed the same treatment approach. Osteotomy sites were internally fixed with a BP (Stryker, Selzach, Switzerland) or a pediatric LCP (Synthes, Zuchwil, Switzerland) in accordance with the surgeon’s preference. 
Associations between the risk factors and hardware- related mechanical complications were assessed using the GEE to calculate the adjusted odds ratios and con- fidence intervals. The dependent variables were adjus- ted according to multiple factors using a GEE with patient age, sex, type of plate, and GMFCS level in cerebral palsy patients as the fixed effects and individual 
Blade plate Using a standard lateral approach to the proximal femur, a 2.0 mm guide wire was placed into the proximal femur, beginning laterally ∼1.5cm distal to the trochanteric apophysis. The position of the chisel was checked with 
patients and side of the body as the random effects. Patients with cerebral palsy were stratified into two groups according to the GMFCS level: ambulatory (GMFCS levels I–III) and nonambulatory (GMFCS levels IV and V). 
intraoperative fluoroscopy to confirm appropriate position 
Statistical analyses were carried out with R, version 3.1.2 in all planes. The appropriate size chisel was inserted into 
software using the Nonlinear Mixed-Effect package 20 the proximal femur immediately cephalad to the guide 
(R Foundation for Statistical Computing, Vienna, wire. Femoral osteotomy was performed around the les- 
Austria). All statistics were two tailed and P values of less ser trochanter. After angular or rotational correction, the 
than 0.05 were considered significant. distal fragment was fixed with at least two compression cortical screws. 
Results A total of 263 patients fulfilled the inclusion criteria. After Locking compression plate 
implementation of the exclusion criteria, a total of 417 Using the same approach as the BP, a 2.0 mm guide wire 
hips from 251 patients were finally included in this study. was introduced into the proximal femur. With an aiming 
A total of 384 hips were in the poor bone health group block for 3.5 or 5.0 mm screws, two 2.8 mm wires were 
and 33 hips were in the normal bone health group. A total inserted. Proximal femoral osteotomy was performed 
of 273 hips had a BP and 144 hips had a LCP (Fig. 1). 1 cm distal to the insertion of the K-wire. After angular or 
The mean age of the patients at the time of surgery was rotational correction, an LCP with a drill sleeve was 
9.1± 3.1 (range: 4.4–19.3) years in the BP group and placed through 2.8mm wires inserted at the proximal 
9.8± 3.7 (range: 3.3–19.7) years in the LCP group. The part of the femur. After fixing the femur and plate using a 
mean time until plate removal was 1.2± 0.6 (range: reduction forcep and a bone holding clamp, the proximal 
0.6–7.2) years in the BP group and 1.1± 0.6 (range: part of the femur was fixed with three locking screws, and 
0.6–6.3) years in the LCP group. The mean follow-up 

Hardware-related complications after proximal femoral osteotomy Chung et al. 267 
Table 1 Summary of patient data 
were not significantly different with respect to age or sex. 
Patients’ information BP Age at surgery [mean ± SD (range)] 
(years) 
LCP P 
0.16 
Second, the results of the proximal femoral osteotomy could have been affected by the operative protocol. The detailed operative protocol may differ between institutes. Male/female Duration till plate removal 
[mean ±SD (range)] (years) 
118/49 51/33 0.12 
For example, an additional fixation screw or pin between the osteotomy site or compression screw insertion at the distal screw hole of the LCP can affect the results of the operation. However, an ideal protocol has not yet been established. At our institute, we applied two sizes of plates in both the LCP and the BP groups. Therefore, there were some cases in which the size of the plate was relatively ambiguous for some patients. Although this is a problem with both plates in our study, the proper size of the plate can also be an important factor for stability. Moreover, screw fixation of the proximal femur with the BP was not applied in our previous operative technique. In the past, proximal screws were not used routinely in all medical centers. We believe that additional screw fixa- tion in the proximal femur is necessary to maintain sta- bility. In addition, the indication of immobilization with a cast can be different among medical centers. Our initial indication for immobilization in a hip spica cast was for the cases where the surgeon judged it necessary among DDH patients who underwent open reduction and femoral varization osteotomy in both groups, and an abduction short leg cast with a bar was applied to all other children only in the BP group. Therefore, further studies may be needed to evaluate the optimal protocol for proximal femoral osteotomy. Third, in all cases, after union was confirmed throughout the follow-up period, we performed hardware removal for all the patients to prevent local pressure symptoms, iliotibial band irritation, or difficulty in removing the hardware later because of exuberant callus, and to facilitate any subsequent femoral surgery [24]. The follow-up duration of our study was limited to at least 6 months after hardware removal to reflect all mechanical complications from the time of hardware removal to the healing of the screw hole. In a previous study, bone mass in young adult men returned to close to normal 18 weeks after hardware removal [18,24]. Hardware removal is recommended for pediatric patients at many institutions [17,24,32]; however, there is some controversy on the efficacy of hardware removal. Further studies may be necessary to compare the prog- nosis associated with maintaining the plate in the body. 
We speculated that the different features between the two groups were caused by the stability of grip in the plates. Locking plates offer improved torsional and bending stability and less pull out of the screw-plate construct in comparison with the conventional BP [33]. Locking plates have a fixed stable angular plate-bone fixation, and this design converts shear stress into com- pressive stress at the screw–bone interface [34]. On the one hand, this strong grip provides angular stability and advantages in severely osteoporotic patients such as elderly or nonambulatory patients. Postoperative braces 
Copyright r 2018 Wolters Kluwer Health, Inc. All rights reserved. 
9.1± 3.1 
9.8 ±3.7 (4.4–19.3) 
(3.3–19.7) 
< 0.001 
Type of disease (patients/hips) 
Cerebral palsy 155/260 67/124 Ambulatory status in CP patients 
(GMFCS level) 
1.2± 0.6 
1.1 ±0.6 (0.6–7.2) 
(0.6–6.3) 
0.002 
I, II, III [n (%)] 100 (65) 28 (42) IV, V [n (%)] 55 (35) 39 (58) Legg–Calve–Perthes 9/9 11/11 Developmental dysplasia of hip 2/2 2/2 Idiopathic increased femoral 
anteversion 
1/2 4/7 
BP, blade plate; CP, cerebral palsy; GMFCS, Gross Motor Function Classification System; LCP, locking compression plate. 
duration was 8.8±2.2 (range: 2.4–12.1) years in the BP group and 3.5± 1.9 (range: 1.2–8.2) years in the LCP group. Overall, a BP was used in 167 patients and an LCP was used in 84 patients (Table 1). 
The overall complication rate in the BP group was 3.0% (five in 167) and 3.6% (three in 84) in the LCP group, and there was no significant difference (P=0.74). Seven cases of loss of fixation (five patients) in the BP group were confirmed (Fig. 2). No other hardware-related mechan- ical complications were found in the BP group. A total of three complications in three patients occurred in the LCP group. Before plate removal, there was an implant-related fracture in one patient (Fig. 3). In addition, two implant- related fractures occurred within 6 months after hardware removal in GMFCS level V patients (Table 2). 
All complications in both groups occurred only in cerebral palsy patients. The risk of complications increased with the age (P=0.002), but sex, body side, plate type, and ambulatory status were not significantly associated with complications (Table 3). 
Discussion This study was carried out to investigate the hardware- related mechanical complications and the associated risk factors after proximal femoral osteotomy with conven- tional BP or pediatric LCP. According to our results, the overall incidence of complications was not significantly different between the two groups (3.0, 3.6%, P=0.74), but the characteristics were different. All complications of the BP group were the loss of fixation and only implant- related fractures occurred in the pediatric LCP group. The risk of complications increased significantly with age (odds ratio=1.3, 95% confidence interval =1.1–1.5). 
Some limitations of this study need to be addressed before discussing the results in detail. First, our study was retrospective in design; therefore, there may have been discrepancies between the characteristics of the patients in each group. However, patient demographics 
268 Journal of Pediatric Orthopaedics B 2018, Vol 27 No 3 
Fig. 2 
Blade plate ‘loss of fixation’ in a 10-year-old boy (Gross Motor Function Classification System level II). (a) Immediate postoperative radiograph shows a femoral derotational osteotomy that was performed. (b) One week postoperatively, the blade plate was loosening, and femoral angular deformity occurred. 
or casts are usually not applied, and early postoperative mobilization and weight bearing can be performed [35]. On the other hand, the stress shielding effect could cre- ate a problem. Bone loss induced by stress shielding leads to a resorptive process characterized by porosis and loss of the endosteal bone, and as a result of this process, cortical thinning can make the bone fragile and more easily fractured [36]. 
In our study, there was no loss of fixation in patients with LCP, but three implant-related fractures occurred in nonambulatory patients with cerebral palsy (P=0.03). A recent study reported that the femur was 15.2 times more likely than other bones to have an implant-related frac- ture [32]. In particular, long and fragile lever arms in the hip joints increase fracture probability, and an additional factor is a long period of immobilization or rigid fixation [14]. Furthermore, after hardware removal, the cortical 
defect acts as a stress riser [37]. Osteopenia, defined as a bone mineral density Z-score less than −2.0, is found in the femurs of most nonambulatory children with cerebral palsy. The clinical and nutritional factor most directly correlated with low bone mineral density was severity of impairment as graded by GMFCS level [28,38]. Therefore, implant-related fractures are more prone to occur in severely osteoporotic nonambulatory patients with cerebral palsy (GMFCS IV, V) after femoral osteotomy. 
We found that age was correlated positively with the incidence of hardware-related mechanical complications after proximal femoral osteotomy. In the conventional BP system, the strength of proximal fixation becomes rela- tively weak as patients grow and mature, and BP fixation requires proper sizing for maximal stability; in the LCP system, the plate has just three designs of width and length and two or three distal fixation screws for varus 
Fig. 3 
An 16-year-old girl (Gross Motor Function Classification System level IV) showed a implant-related fracture 3 months after femoral varization derotational osteotomy. (a) Hip anterioposterior (b) hip translateral. 

Copyright r 2018 Wolters Kluwer Hea"""

print("\nPre Defined Text Length : \n",len(article_content))

def _create_dictionary_table(text_string) -> dict:
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text_string)
    stem = PorterStemmer()
    frequency_table = dict()
    for wd in words:
        wd = stem.stem(wd)
        if wd in stop_words:
            continue
        if wd in frequency_table:
            frequency_table[wd] += 1
        else:
            frequency_table[wd] = 1

    return frequency_table


def _calculate_sentence_scores(sentences, frequency_table) -> dict:   
    sentence_weight = dict()

    for sentence in sentences:
        sentence_wordcount = (len(word_tokenize(sentence)))
        sentence_wordcount_without_stop_words = 0
        for word_weight in frequency_table:
            if word_weight in sentence.lower():
                sentence_wordcount_without_stop_words += 1
                if sentence[:7] in sentence_weight:
                    sentence_weight[sentence[:7]] += frequency_table[word_weight]
                else:
                    sentence_weight[sentence[:7]] = frequency_table[word_weight]

        sentence_weight[sentence[:7]] = sentence_weight[sentence[:7]] / sentence_wordcount_without_stop_words

       

    return sentence_weight

def _calculate_average_score(sentence_weight) -> int:
   
    sum_values = 0
    for entry in sentence_weight:
        sum_values += sentence_weight[entry]

    average_score = (sum_values / len(sentence_weight))

    return average_score

def _get_article_summary(sentences, sentence_weight, threshold):
    sentence_counter = 0
    article_summary = ''

    for sentence in sentences:
        if sentence[:7] in sentence_weight and sentence_weight[sentence[:7]] >= (threshold):
            article_summary += " " + sentence
            sentence_counter += 1

    return article_summary

def _run_article_summary(article):
    frequency_table = _create_dictionary_table(article)
    sentences = sent_tokenize(article)
    sentence_scores = _calculate_sentence_scores(sentences, frequency_table)
    threshold = _calculate_average_score(sentence_scores)
    article_summary = _get_article_summary(sentences, sentence_scores, 1.145 * threshold)
    return article_summary

if __name__ == '__main__':
    summary_results = _run_article_summary(article_content)
    print(summary_results)
    print("\nPost Summarized Text Length : \n",len(summary_results))
