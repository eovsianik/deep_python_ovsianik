class SomeModel:
    def predict(self, message: str) -> float:  # pragma: no cover
        return len(message) % 10 * 0.1


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    result = model.predict(message)
    if result > good_thresholds:
        return "отл"
    if result < bad_thresholds:
        return "неуд"
    return "норм"
