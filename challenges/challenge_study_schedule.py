def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    # Verifica se target_time é None. Se for, significa que não há um tempo-alvo definido, e a função retorna None. Isso é útil para lidar com casos em que o tempo-alvo não está especificado.

    alunos = 0
    for periodo in permanence_period:
        if not isinstance(periodo[0], int) or not isinstance(periodo[1], int):
            return None
        if periodo[0] <= target_time <= periodo[1]:
            alunos += 1
    return alunos
