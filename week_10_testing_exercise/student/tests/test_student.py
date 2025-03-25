from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.dummy_student_with_courses = Student('courses', {'Algebra': [], 'History': [], 'English': []})
        self.dummy_student_without_courses = Student('nocourses')

    def test_student_init_with_courses(self):
        self.assertEqual('courses', self.dummy_student_with_courses.name)
        self.assertDictEqual({'Algebra': [], 'History': [], 'English': []}, self.dummy_student_with_courses.courses)

    def test_student_init_without_courses(self):
        self.assertEqual('nocourses', self.dummy_student_without_courses.name)
        self.assertDictEqual({}, self.dummy_student_without_courses.courses)

    def test_enroll_course_add_notes_only(self):
        result = self.dummy_student_with_courses.enroll('Algebra', ['a', 'b', 'c'])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertTrue(all(x in self.dummy_student_with_courses.courses['Algebra'] for x in ['a', 'b', 'c']))

    def test_enroll_add_course_and_notes(self):
        result = self.dummy_student_with_courses.enroll('Programming', ['a', 'b', 'c'])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertIn("Programming", self.dummy_student_with_courses.courses)
        self.assertListEqual(['a', 'b', 'c'], self.dummy_student_with_courses.courses['Programming'])

        result = self.dummy_student_with_courses.enroll('Gardening', ['a', 'b', 'c'], 'Y')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertIn("Gardening", self.dummy_student_with_courses.courses)
        self.assertListEqual(['a', 'b', 'c'], self.dummy_student_with_courses.courses['Gardening'])


    def test_enroll_add_course_only(self):
        result = self.dummy_student_with_courses.enroll('Programming', ['a', 'b', 'c'], 'N')
        self.assertIn("Programming", self.dummy_student_with_courses.courses)
        self.assertEqual('Course has been added.', result)
        self.assertEqual([], self.dummy_student_with_courses.courses['Programming'])

    def test_add_notes_course_not_found_raises(self):
        with self.assertRaises(Exception) as e:
            self.dummy_student_with_courses.add_notes('Programming', 'abc')
        self.assertEqual("Cannot add notes. Course not found.", str(e.exception))

    def test_add_notes(self):
        result = self.dummy_student_with_courses.add_notes('Algebra', 'abc')
        self.assertEqual('abc', self.dummy_student_with_courses.courses['Algebra'][0])
        self.assertEqual("Notes have been updated", result)

    def test_leave_course_not_found_raises(self):
        with self.assertRaises(Exception) as e:
            self.dummy_student_with_courses.leave_course('Programming')
        self.assertEqual("Cannot remove course. Course not found.", str(e.exception))

    def test_leave_course(self):
        result = self.dummy_student_with_courses.leave_course('Algebra')
        self.assertNotIn('Algebra', self.dummy_student_with_courses.courses)
        self.assertEqual("Course has been removed", result)

if __name__ == "__main__":
    main()