from mycroft import MycroftSkill, intent_file_handler


class ThoughtsOnCourse(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('course.on.thoughts.intent')
    def handle_course_on_thoughts(self, message):
        self.speak_dialog('course.on.thoughts')


def create_skill():
    return ThoughtsOnCourse()

