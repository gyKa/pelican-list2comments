# list2comments

Plugin reads static comments from the file and prepare them as a *key-value*
list for the article.

## Installation

Clone repository to your plugins directory:

`git https://github.com/gyKa/pelican-list2comments.git list2comments`

## Configuration

Add a setting `COMMENTS_PATH`, which should point to comments directory. By
default it is `comments` under `content` directory.

In order to enable plugin add `list2comments` to `PLUGINS` list.

Create a file in the comments directory. File name should be
`{title-related-to-the-article.txt}`. Every line in the file is a comment. E.g.:

```
0.jpg: This is my comment.
1.png: Second comment.
```

First part of the line until symbol ':' is a key, second part is a comment.

Now open an article. Add metatag `Comments` which should point to your comments
file without extension.

In the template you can access your comment via `article.comments` variable.
It is a simple pythonic dictionary.
