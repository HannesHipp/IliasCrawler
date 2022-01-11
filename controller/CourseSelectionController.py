from model.Ilias import Ilias
from service.Database import Database
from view.CourseSelectionView import CourseSelectionView


class CourseSelectionController:

    @staticmethod
    def run():
        CourseSelectionView.search_ilias_for_courses_promt()

        current_courses = CourseSelectionController.crawl_for_courses()
        current_course_numbers = [course.get_course_number()
                                  for course in current_courses]
        old_course_numbers = Database.get_instance("all_courses").get_all()
        new_course_numbers = list(
            set(current_course_numbers) - set(old_course_numbers))
        for new_course_number in new_course_numbers:
            Database.get_instance("all_courses").add(new_course_number)
        new_courses = [course for course in current_courses if course.get_course_number() in new_course_numbers]

        CourseSelectionView.number_of_new_courses_promt(len(new_courses))

        first_time_execution = len(old_course_numbers) == 0
        new_courses_present = len(new_courses) != 0
        user_wants_to_change_existing_download_settings = True
        courses_to_choose_from = current_courses
        if not first_time_execution:
            if new_courses_present:
                choice = CourseSelectionView.select_between_all_or_only_new_courses()
                if choice == "Nur bei den neu gefundenen Kursen":
                    courses_to_choose_from = new_courses
            else:
                if not CourseSelectionView.user_wants_to_change_settings():
                    user_wants_to_change_existing_download_settings = False
        if user_wants_to_change_existing_download_settings:
            courses_to_download = CourseSelectionView.get_courses_numbers_to_download_from_user(courses_to_choose_from)
            Database.get_instance("courses_to_download").overwrite(courses_to_download)
            CourseSelectionView.thank_you_promt()
        if first_time_execution:
            CourseSelectionView.first_time_only_promt()
        return current_courses

    @staticmethod
    def crawl_for_courses():
        return Ilias.create().get_new_pages()
    