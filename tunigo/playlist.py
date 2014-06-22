from __future__ import unicode_literals

import tunigo


class Playlist(object):

    def __init__(self,
                 created=0,
                 description='',
                 id='',
                 image='',
                 location='',
                 main_genre=None,
                 main_genre_template='',
                 num_subscribers=0,
                 sub_genre=None,
                 sub_genre_template='',
                 title='',
                 updated=0,
                 uri='',
                 version=0,
                 item_array=None):

        if item_array:
            self._created = int(item_array['created'])
            self._description = item_array['description']
            self._id = item_array['id']
            self._image = item_array['image']
            self._location = item_array['location']
            self._main_genre = tunigo.Genre(
                playlist=self,
                template_name=item_array['mainGenreTemplate'])
            self._num_subscribers = int(item_array['numSubscribers'])
            self._sub_genre = tunigo.SubGenre(
                key=item_array['subGenreTemplate'],
                main_genre=self._main_genre)
            self._title = item_array['title']
            self._updated = int(item_array['updated'])
            self._uri = item_array['uri']
            self._version = int(item_array['version'])

        else:
            self._created = int(created)
            self._description = description
            self._id = id
            self._image = image
            self._location = location

            if main_genre_template:
                self._main_genre = tunigo.Genre(
                    playlist=self,
                    template_name=main_genre_template)
            else:
                self._main_genre = main_genre

            self._num_subscribers = int(num_subscribers)

            if sub_genre_template:
                self._sub_genre = tunigo.SubGenre(key=sub_genre_template,
                                                  main_genre=self._main_genre)
            else:
                self._sub_genre = sub_genre

            self._title = title
            self._updated = int(updated)
            self._uri = uri
            self._version = int(version)

    @property
    def created(self):
        return self._created

    @property
    def description(self):
        return self._description

    @property
    def id(self):
        return self._id

    @property
    def image(self):
        return self._image

    @property
    def location(self):
        return self._location

    @property
    def main_genre(self):
        return self._main_genre

    @property
    def main_genre_template(self):
        return self._main_genre.template_name

    @property
    def num_subscribers(self):
        return self._num_subscribers

    @property
    def sub_genre(self):
        return self._sub_genre

    @property
    def sub_genre_template(self):
        return self._sub_genre.template_name

    @property
    def title(self):
        return self._title

    @property
    def updated(self):
        return self._updated

    @property
    def uri(self):
        return self._uri

    @property
    def version(self):
        return self._version