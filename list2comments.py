import os
from pelican import signals


def get_content_path(pelican):
    return pelican.settings.get('PATH')


def list2comments(generator):
    comments_path = generator.settings.get('COMMENTS_PATH', 'comments')
    comments_path = os.path.join(get_content_path(generator), comments_path)

    for article in generator.articles:
        comments = {}

        if 'comments' in article.metadata.keys():
            comments_filename = article.metadata.get('comments')
            comments_file = os.path.join(comments_path, comments_filename)
            comments_file += '.txt'

            if os.path.isfile(comments_file):
                lines = [line.rstrip('\n') for line in open(comments_file)]

                for line in lines:
                    filename, comment = line.split(':', 1)
                    comments[filename] = comment.strip()

        article.comments = comments


def register():
    signals.article_generator_finalized.connect(list2comments)
