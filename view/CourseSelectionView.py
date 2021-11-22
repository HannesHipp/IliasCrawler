from PyInquirer import prompt


class CourseSelectionView:

    @staticmethod
    def select_between_all_or_only_new_courses():
        questions = [
            {
                'type': 'list',
                'name': 'choice',
                'message': 'Wähle bitte aus, bei welchen Kursen die Download-Einstellungen angepasst werden sollen:',
                'choices': ['Nur bei den neu gefundenen Kursen', 'Bei allen Kursen'],
            }
        ]
        user_input = prompt(questions)
        return user_input['choice']

    @staticmethod
    def user_wants_to_change_settings():
        questions = [
            {
                'type': 'confirm',
                'name': 'choice',
                'message': 'Möchtest du die bisherigen Einstellungen für die herunterzuladenden Kurse anpassen?',
            }
        ]
        user_input = prompt(questions)
        return user_input['choice']

    @staticmethod
    def get_courses_numbers_to_download_from_user(courses):
        choices = [{'name': course.name} for course in courses]
        questions = [
            {
                'type': 'checkbox',
                'qmark': '?',
                'message': 'Wähle die Kurse aus, die du herrunterladen möchtest:',
                'name': 'courses_to_download',
                'choices': choices
            }
        ]
        user_input = prompt(questions)
        result = [course.get_course_number() for course in courses if course.name in user_input['courses_to_download']]
        return result

    @ staticmethod
    def search_ilias_for_courses_promt():
        print("\nIlias wird nach Kursen durchsucht...")

    @ staticmethod
    def number_of_new_courses_promt(number_of_new_courses):
        if number_of_new_courses == 0:
            print("\nEs wurden keine neuen Kurse gefunden.")
        else:
            print("\nEs wurden %s neue Kurse gefunden." %
                  number_of_new_courses)

    @ staticmethod
    def thank_you_promt():
        print("\nVielen Dank. Deine Eingaben wurden gespeichert.")

    @ staticmethod
    def first_time_only_promt():
        print("\nIn Zukunft wirst du benachrichtigt wenn ein neuer Kurs gefunden wurde. Du wirst außerdem jedes mal \n"
              "beim Ausführen des Programms gefragt, ob du deine Auswahl der Kurse anpassen möchtest.")

    @ staticmethod
    def show_no_new_courses_promt():
        print("\nEs wurden keine neuen Kurse gefunden. Vielleicht wurden in den Kursen ja neue Dateien hinzugefügt...")
