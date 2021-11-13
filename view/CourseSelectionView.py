from view import Service


class CourseSelectionView:

    @staticmethod
    def would_you_like_to_change_course_exceptions():
        print("\nMöchtest du die Auswahl der zu herrunterladenenden Kurse anpassen?")
        Service.yes_no_promt()

    @staticmethod
    def search_ilias_for_courses_promt():
        print("\nIlias wird nach Kursen durchsucht...")

    @staticmethod
    def number_of_new_courses_promt(number_of_new_courses):
        if number_of_new_courses == 0:
            print("\nEs wurden keine neuen Kurse gefunden.")
        else:
            print("\nEs wurden %s neue Kurse gefunden. Bitte wähle im Folgenden, ob du sie herrunterladen willst \n"
                  "oder nicht." % number_of_new_courses)

    @staticmethod
    def thank_you_promt():
        print("\nVielen Dank. Deine Eingaben wurden gespeichert.")

    @staticmethod
    def first_time_only_promt():
        print("\nIn Zukunft wirst du benachrichtigt wenn ein neuer Kurs gefunden wurde. Du wirst außerdem jedes mal \n"
              "beim Ausführen des Programms gefragt, ob du deine Auswahl der Kurse anpassen möchtest.")

    @staticmethod
    def show_no_new_courses_promt():
        print("\nEs wurden keine neuen Kurse gefunden. Vielleicht wurden in den Kursen ja neue Dateien hinzugefügt...")
