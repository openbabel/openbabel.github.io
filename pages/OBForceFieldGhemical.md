---
title: OBForceFieldGhemical
permalink: /OBForceFieldGhemical/
---

OBForceFieldGhemical class
--------------------------

This class is an implementation of the molecular mechanics force field used in the [Ghemical](http://www.uku.fi/~thassine/projects/ghemical/) program. It is an all-atom method similar to the Tripos-5.2 force field.

### Parameters

Parameters for the Gehmical force field can be found in data/ghemical.prm.

### Bonded Interactions

#### Bond Stretching

[Image:BondEGhemical.png](/Image:BondEGhemical.png "wikilink")

<tex>E_{bond}=k_{b}(r_{ab}-r_{ab}^0)^2</tex>

<tex>k_b</tex>: bond stretching force constant (ghemical.prm)

<tex>r_{ab}^0</tex>: ideal bond length (ghemical.prm)

<tex>r_{ab}</tex>: bond length between atoms a and b

#### Angle Bending

[Image:AngleEGhemical.png](/Image:AngleEGhemical.png "wikilink")

<tex>E_{angle}=k_a(\\theta_{abc}-\\theta_{abc}^0)^2</tex>

<tex>k_a</tex>: angle bending force constant (ghemical.prm)

<tex>\\theta_{abc}^0</tex>: ideal angle (ghemical.prm)

<tex>\\theta_{abc}</tex>: angle

#### Torsional

[Image:TorsionSingleEGhemical.png](/Image:TorsionSingleEGhemical.png "wikilink") [Image:TorsionDoubleEGhemical.png](/Image:TorsionDoubleEGhemical.png "wikilink")

<tex>E_{torsion}= V_1(1 + cos(\\omega_{abcd})) + V_2(1 - cos(2\\omega_{abcd})) + V_1(1 + cos(3\\omega_{abcd}))</tex>

<tex>V_t</tex>: rotational barrier (ghemical.prm)

<tex>s_t</tex>: +1 if staggered minimum, -1 if eclipsed minimum (ghemical.prm)

<tex>n_t</tex>: multiplicity (ghemical.prm)

<tex>\\omega_{abcd}</tex>: torsion angle

<tex>V_1</tex>, <tex>V_2</tex> and <tex>V_3</tex> can be derived from <tex>V_t</tex>, <tex>s_t</tex> and <tex>n_t</tex> using this table:

|                 |                        |                        |                        |                        |                        |                        |
|-----------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
|                 | <tex>s_tn_t=+3</tex> | <tex>s_tn_t=+2</tex> | <tex>s_tn_t=+1</tex> | <tex>s_tn_t=-1</tex> | <tex>s_tn_t=-2</tex> | <tex>s_tn_t=-3</tex> |
| <tex>V_1</tex> | 0                      | 0                      | <tex>V_t</tex>        | <tex>-V_t</tex>       | 0                      | 0                      |
| <tex>V_2</tex> | 0                      | <tex>-V_t</tex>       | 0                      | 0                      | <tex>V_t</tex>        | 0                      |
| <tex>V_3</tex> | <tex>V_t</tex>        | 0                      | 0                      | 0                      | 0                      | <tex>-V_t</tex>       |
||

### Non-Bonded Interactions

#### Van der Waals

[Image:VDWEGhemical.png](/Image:VDWEGhemical.png "wikilink")

<tex>E_{vdw}=k_{ab}\\left(\\frac{1}{\\sigma_{ab}^{12}} - \\frac{2}{\\sigma_{ab}^6}\\right)</tex>

<tex>k_{ab} = \\sqrt{k_a k_b}</tex>: force constant (ghemical.prm)

<tex>\\sigma_{ab} = \\frac{r_{ab}}{R_a + R_b}</tex>

<tex>R_a</tex>: vdw radius of atom a (ghemical.prm)

<tex>r_{ab}</tex>: separation (calulated in the same way as bondlengths)

#### Electrostatic

[Image:EleAttrEGhemical.png](/Image:EleAttrEGhemical.png "wikilink") [Image:EleRepEGhemical.png](/Image:EleRepEGhemical.png "wikilink")

<tex>E_{ele}=332.17 \\frac{Q_a Q_b}{r_{ab}}</tex>

<tex>Q_a</tex>: net atomic charge on atom a

<tex>Q_b</tex>: net atomic charge on atom b

<tex>r_{ab}</tex>: separation (calulated in the same way as bondlengths)

<tex>332.17</tex>: unit conversion factor

#### 1,4-Scaling

Non bonded interations between atoms in a 1,4 relationship are scaled with a factor 0.5.

### Validation

Done. The energies were compared to the energies produced by the ghemical package. Analytical gradients are also implemented and their values have been compared to numerical derivatives. (The MMFF94 test set was used for the validation.)

[Category:Force_Fields](/Category:Force_Fields "wikilink")[Category:Developer](/Category:Developer "wikilink")