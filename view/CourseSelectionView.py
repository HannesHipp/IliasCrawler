class CourseSelectionView:

    @staticmethod
    def search_ilias_for_courses_promt():
        print("\nIlias wird nach Kursen durchsucht...")

    @staticmethod
    def number_of_new_courses_promt(number_of_new_courses):
        print("\nEs wurden %s neue Kurse gefunden." % number_of_new_courses)
        if number_of_new_courses != 0:
            print("Bitte wähle im Folgenden, ob du sie herrunterladen willst oder nicht.")

    @staticmethod
    def thank_you_promt():
        print("\nVielen Dank. Deine Eingaben wurden gespeichert.")

    @staticmethod
    def first_time_only_promt():
        print("\nIn Zukunft wirst du benachrichtigt wenn ein neuer Kurs gefunden wurde.")
        #Du wirst außerdem jedes mal beim Ausführen des Programms gefragt, ob du deine Auswahl der Kurse anpassen möchtest.

    @staticmethod
    def show_no_new_courses_promt():
        print("\nEs wurden keine neuen Kurse gefunden. Vielleicht wurden in den Kursen ja neue Dateien hinzugefügt. \n"
              "Schauen wir doch mal nach...")
