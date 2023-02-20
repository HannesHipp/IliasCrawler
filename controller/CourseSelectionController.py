from service.Session import Session
from model.Folders import Root
from service.Database import Database
from view import Service
from view.CourseSelectionView import CourseSelectionView


class CourseSelectionController:

    @staticmethod
    def run():
        CourseSelectionView.search_ilias_for_courses_promt()

        # get old courses and course numbers
        old_courses = Database.get_instance("all_courses").get_all()
        old_course_numbers = []
        for course in old_courses:
            old_course_numbers.append(course[0])

        # get current courses and course numbers
        current_courses = CourseSelectionController.crawl_for_courses()
        current_course_numbers = []
        for course in current_courses:
            current_course_numbers.append(course.get_course_number())

        # delete deleted courses from database
        deleted_course_numbers = list(
            set(old_course_numbers) - set(current_course_numbers))
        for course_number in deleted_course_numbers:
            Database.get_instance("all_courses").delete_key(course_number)

        # get new course numbers, show number of new courses and add new courses to database
        new_course_numbers = list(
            set(current_course_numbers) - set(old_course_numbers))
        new_courses = []
        for course in current_courses:
            for new_course_number in new_course_numbers:
                if course.get_course_number() == new_course_number:
                    new_courses.append(course)
                    Database.get_instance("all_courses").add(
                        new_course_number, course.name)

        # user chooses to select course exceptions for all or only new courses
        courses_to_choose_from = new_courses
        CourseSelectionView.would_you_like_to_change_course_exceptions()
        if Service.user_chooses_yes(""):
            courses_to_choose_from = current_courses
        else:
            CourseSelectionView.number_of_new_courses_promt(len(new_courses))

        # Select course exceptions and save to database
        course_exception_numbers = CourseSelectionController.select_course_exceptions(
            courses_to_choose_from)
        for course_exception_number in course_exception_numbers:
            try:
                Database.get_instance("course_exceptions").add(
                    course_exception_number)
            except:
                pass
        if len(new_courses) != 0:
            CourseSelectionView.thank_you_promt()
        if len(old_courses) == 0:
            CourseSelectionView.first_time_only_promt()

        return current_courses

    @staticmethod
    def crawl_for_courses():
        root = Root('Ilias',
                    "https://ilias3.uni-stuttgart.de/ilias.php?baseClass=ilDashboardGUI&cmd=jumpToSelectedItems",
                    None)
        root.content = Session.get_content(root.url)
        return root.get_new_pages()

    @staticmethod
    def select_course_exceptions(new_courses):
        if len(new_courses) != 0:
            Service.yes_no_promt()
        result = []
        for course in new_courses:
            if not Service.user_chooses_yes(course.name + ": "):
                result.append(course.get_course_number())
        return result
