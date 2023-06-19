#iterator
class workoutIterator:
    def __init__(self):
        self.workout_parts = [" отжимания ", "приседания" ]
        self.additional_parts = []
        self.current_index = 0

    def include_squats(self, squats=False):
        if squats:
            self.additional_parts.append(" приседания ")

    def include_push_ups(self, push_ups=False):
        if push_ups:
            self.additional_parts.append(" отжимания ")

    def include_бег (self, running=False):
        if running:
            self.additional_parts.append(" бег")

    def print_workout(self):
        print(*self.workout_parts[:4], *self.additional_parts, self.workout_parts[-1])


workout = workoutIterator()
workout.print_workout()

workout.include_бег(True)
workout.print_workout()

#visitor
class cardio(workoutIterator):
    def __init__(self):
        super().__init__()

    def include_additional(self):
        self.additional_parts.insert(-1, " бег ")



# Пример использования
cardio = cardio()
cardio.include_additional()
cardio.print_workout()