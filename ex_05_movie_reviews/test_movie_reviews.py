import subprocess
from unittest import TestCase

from hamcrest import assert_that, equal_to


class TestMovieReviews(TestCase):
    def test_no_reviews_shown_if_no_reviews_exist(self):
        stdout = subprocess.check_output([
            'python',
            'movie_reviews.py',
            'display'
        ])
        assert_that(stdout.strip(), equal_to('No reviews'))

    def test_rating_stats_shown_after_adding_a_review(self):
        # TODO: will need to pass input to std in and use Popen I think
        cmd = [
            'python',
            'movie_reviews.py',
            'add'
        ]
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE
        )
        expected_outputs = ''.join((
            'Enter movie title:',
            'Enter rating (0-5):',
            'Enter your name:',
            'Enter review text:',
        ))
        inputs = '\n'.join((
            'The Abyss',
            'Jo Jones',
            '5',
            'The film was very good.'
        ))
        stdout, stderr = proc.communicate(inputs)
        proc.wait()
        assert_that(stdout.strip(), equal_to(expected_outputs))


        cmd = [
            'python',
            'movie_reviews.py',
        ]
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE
        )
        stdout, stderr = proc.communicate(inputs)
        proc.wait()

        expected_outputs = '''\
The Abyss
Rating  No. of Reviews
5       1
4       0
3       0
2       0
1       0'''
        assert_that(stdout.strip(), equal_to(expected_outputs))
