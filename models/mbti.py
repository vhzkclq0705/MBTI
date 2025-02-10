# MBTI Data model
class Mbti:
    def __init__(self, country: str, mbti: str, percentage: float):
        self.country = country
        self.mbti = mbti
        self.percentage = percentage
