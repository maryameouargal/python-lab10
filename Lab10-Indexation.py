import numpy as np
import numpy as np
# ETAPE 1

A = np.array([10, 28, 38, 40, 58])
N = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

print("Tableau 1D A :", A)
print("Tableau 2D N :\n", N)

# ETAPE 2

element_3 = A[2]      
element_fin = A[-1]   

print("A[2] =", element_3)
print("A[-1] =", element_fin)

valeur_12 = N[1, 2]      
valeur_dernier = N[-1, -1]  
print("N[1, 2] =", valeur_12)
print("N[-1, -1] =", valeur_dernier)

# ETAPE 3
# TASK 3.1
segment = A[1:4] 
print("A[1:4] =", segment)

#TASK 3.2
print("\nTask 3.2:")
print("A[:-1] =", A[:-1])  
print("A[-3:] =", A[-3:])

# ETAPE 4 
# Task 4.1 
sous_bloc = N[0:2, 1:]
print("\nTask 4.1:")
print("N[0:2, 1:] =\n", sous_bloc)

# Task 4.2 
ligne_2 = N[1, :]  
print("\nTask 4.2:")
print("Ligne 2 (row 2):", ligne_2)

# Task 4.3  
colonne_3 = N[:, 2]  
print("\nTask 4.3:")
print("Colonne 3 (column 3):", colonne_3)

#ETAPE 5 
# Task 5.1 
bloc_central = N[0:3, 1:3]
print("\nTask 5.1:")
print("Bloc central N[0:3, 1:3] :\n", bloc_central)

# Task 5.2 
colonnes_alternées = N[:, ::2]
print("\nTask 5.2:")
print("Colonnes 0 et 2 (columns 0 and 2) N[:, ::2] :\n", colonnes_alternées)

# ETAPE 6
# Task 6.1 
print("Task 6.1 ")
# Créez une vue 
vue = N[0:2, 1:3]
print("Vue initiale :\n", vue)

# Modifiez la vue
vue[0, 0] = 999
print("Vue modifiée :\n", vue)
print("M après modification via la vue :\n",N)


# Task 6.2 - Reset the matrix
print("Task 6.2 ")

N = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

print("N réinitialisé aux valeurs originales :\n", N)

# ETAPE 7
# Task 7.1
print("Task 7.1 ")
# 1. Créez une copie 
sous_copie = N[0:2, 1:3].copy()  
print("Copie avant modification :\n", sous_copie)

# 2. Modifiez la copie
sous_copie[0, 0] = 999
print("\nCopie modifiée :\n", sous_copie)
print("\nN restée intacte :\n", N)

# ETAPE 8
print("ÉTAPE 8 - Exercices d'application guidés")
# Exercise 8.1
print("\nExercise 8.1")
N[:, -1] *= 10
print("N après multiplication de la dernière colonne :\n", N)
N = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Exercise 8.2
print("\n Exercise 8.2 ")
bloc_vue = N[1:, :2]
bloc_vue[:] = -1
print("N après bloc -1 (via vue) :\n", N)
N = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Exercise 8.3
print("\nExercise 8.3 ")
bloc_copy = N[1:, :2].copy()
bloc_copy[:] = -1
print("Bloc copy modifié :\n", bloc_copy)
print("\nN (copie intacte) :\n", N)

# Exercise 8.4
print("\nExercise 8.4 ")
A_original = A.copy()
A[1:-1] = 0
print("A modifié (éléments intermédiaires = 0) :", A)
A = A_original
print("A restauré :", A)