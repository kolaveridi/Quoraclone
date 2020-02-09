from django.apps import AppConfig


class QuestionsConfig(AppConfig):
    name = 'questions'
    
    
    def redy(self):
        import questions.signals
