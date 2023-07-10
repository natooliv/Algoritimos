def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    alunos = 0
    for periodo in permanence_period:
        if not isinstance(periodo[0], int) or not isinstance(periodo[1], int):
            return None
        if periodo[0] <= target_time <= periodo[1]:
            alunos += 1
    return alunos
