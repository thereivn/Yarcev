import numpy as np


def calculate_consistency(matrix):
    n = matrix.shape[0]
    eigenvalues, _ = np.linalg.eig(matrix)
    max_eigenvalue = max(eigenvalues).real
    CI = (max_eigenvalue - n) / (n - 1)
    RI = {1: 0, 2: 0, 3: 0.58, 4: 0.9, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
    CR = CI / RI[n]
    return CI, CR, max_eigenvalue

def print_matrix(matrix, title):
    print(f"\n{title}:")
    for row in matrix:
        print(" ".join([f"{x:.3f}" for x in row]))

def calculate_priority_vector(matrix, name):
    print(f"\n=== Обработка матрицы {name} ===")
    print_matrix(matrix, "Исходная матрица")

    # Вычисление среднего геометрического для каждой строки
    geo_mean = np.prod(matrix, axis=1) ** (1 / len(matrix))
    print("\nСреднее геометрическое строк:")
    print([f"{x:.3f}" for x in geo_mean])
    # Нормализация вектора
    normalized = geo_mean / np.sum(geo_mean)
    print("\nНормализованный вектор приоритетов:")
    print([f"{x:.3f}" for x in normalized])

    return normalized

# Матрицы попарных сравнений (примерные данные)
criteria_matrix = np.array([
    [1, 3, 5],  # Мощность > Уровень шума > Диаметр лопастей
    [1 / 3, 1, 2],  # Уровень шума > Мощность > Диаметр лопастей
    [1 / 5, 1 / 2, 1]  # Диаметр лопастей > Мощность > Уровень шума
])

power_matrix = np.array([
    [1, 2, 4],  # 50 Вт > 75 Вт > 100 Вт
    [1 / 2, 1, 3],  # 75 Вт > 50 Вт > 100 Вт
    [1 / 4, 1 / 3, 1]  # 100 Вт > 50 Вт > 75 Вт
])

noise_matrix = np.array([
    [1, 4, 2],  # 30 дБ > 40 дБ > 50 дБ
    [1 / 4, 1, 1 / 2],  # 40 дБ > 30 дБ > 50 дБ
    [1 / 2, 2, 1]  # 50 дБ > 30 дБ > 40 дБ
])

diameter_matrix = np.array([
    [1, 3, 5],  # 30 см > 40 см > 50 см
    [1 / 3, 1, 2],  # 40 см > 30 см > 50 см
    [1 / 5, 1 / 2, 1]  # 50 см > 30 см > 40 см
])

# Шаг 1: Вычисление весов критериев
criteria_weights = calculate_priority_vector(criteria_matrix, "Критериев")

# Шаг 2: Вычисление весов альтернатив по каждому критерию
power_weights = calculate_priority_vector(power_matrix, "Мощности")
noise_weights = calculate_priority_vector(noise_matrix, "Уровня шума")
diameter_weights = calculate_priority_vector(diameter_matrix, "Диаметра лопастей")

# Шаг 3: Проверка согласованности для каждой матрицы
print("\n=== Проверка согласованности матрицы критериев ===")
CI, CR, lambda_max = calculate_consistency(criteria_matrix)
print(f"Главное собственное значение: {lambda_max:.3f}")
print(f"ИС: {CI:.3f}, ОС: {CR:.3f} (допустимо < 0.1)")

# Линейная свертка
print("\n=== Линейная свертка приоритетов ===")
alternative_weights = np.vstack((power_weights, noise_weights, diameter_weights))
print_matrix(alternative_weights, "Матрица весов альтернатив")
final_weights = np.dot(alternative_weights.T, criteria_weights)
print("\nИтоговые веса вентиляторов:")
for i, w in enumerate(final_weights):
    print(f"Вентилятор {i + 1}: {w:.3f}")