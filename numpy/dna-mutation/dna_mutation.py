import numpy as np


def get_dna(n):
    return np.random.choice(np.array('AGCT', 'c'), n)


def print_dna(dna):
    return dna.tobytes().decode()


DNA_length = 10
original_dna = get_dna(DNA_length)
mutation_indices = np.unique(np.random.randint(0, DNA_length, size=DNA_length))
mutations = get_dna(len(mutation_indices))
new_dna = original_dna.copy()
new_dna[mutation_indices] = mutations

print(f'original dna: {print_dna(original_dna)}\n'
      f'mutations: {print_dna(mutations)}\n'
      f'mutation indices: {mutation_indices}\n'
      f'new dna: {print_dna(new_dna)}')