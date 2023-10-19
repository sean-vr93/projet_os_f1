import random

# 20 grands prix en tout
grands_prix = []
# 20 voitures
voitures = [1, 11, 16, 55, 63, 44, 31, 10, 4, 81, 77, 24, 14, 18, 20, 27, 22, 3, 23, 2]
# 23 circuits, ils font tous 5km, 3 secteurs
circuits = []


### PAR GRANDS PRIX ###

## CHOISIR ENTRE UN DES WEEKENDS

## WEEKEND CLASSIQUE 

# 1 heure
seance_libre_normaleP1 = []
# 1 heure
seance_libre_normaleP2 = []
# 1 heure
seance_libre_normaleP3 = []

# 18 minutes, élimine les 5 dernières voitures : 16 à 20 places
seance_qualif_normaleQ1 = []
# 15 minutes, élimine les 5 suivantes : 11 à 15 places
seance_qualif_normaleQ2 = []
# 12 minutes, classer les 10 dernières : 1 à 10 places
seance_qualif_normaleQ3 = []

# la course quoi
course_normale = []


## WEEKEND SPECIAL

# 1 heure 
course_specialeP1 = []

# 18 minutes, élimine les 5 dernières voitures : 16 à 20 places
seance_qualif_specialeQ1 = []
# 15 minutes, élimine les 5 suivantes : 11 à 15 places
seance_qualif_specialeQ2 = []
# 12 minutes, classer les 10 dernières : 1 à 10 places
seance_qualif_specialeQ3 = []

# Qalif pour le sprint 12 minutes
seance_qualif_sprintQ1 = []
# Qalif pour le sprint 10 minutes
seance_qualif_sprintQ2 = []
# Qalif pour le sprint 8 minutes
seance_qualif_sprintQ3 = []

# Course sprint 100km
course_sprint = []
# Course speciale
course_speciale = []