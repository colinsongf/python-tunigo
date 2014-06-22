from __future__ import unicode_literals

import tunigo


class Genre(object):

    def __init__(self,
                 created=0,
                 header_image_url='',
                 icon_image_url='',
                 icon_url='',
                 id='',
                 location='',
                 mood_image_url='',
                 name='',
                 number_playlists=0,
                 playlist=None,
                 playlist_uri='',
                 sub_genres=[],
                 template_name='',
                 type='',
                 updated=0,
                 version=0,
                 item_array=None):

        if item_array:
            self._created = int(item_array['created'])
            self._header_image_url = item_array['headerImageUrl']
            self._icon_image_url = item_array['iconImageUrl']
            self._icon_url = item_array['iconUrl']
            self._id = item_array['id']
            self._location = item_array['location']
            self._mood_image_url = item_array['moodImageUrl']
            self._name = item_array['name']
            self._number_playlists = int(item_array['numberPlaylists'])
            self._playlist = tunigo.Playlist(main_genre=self,
                                             uri=item_array['playlistUri'])
            self._sub_genres = []
            for sub_genre in item_array['subGenres']:
                self._sub_genres.append(SubGenre(key=sub_genre['key'],
                                                 main_genre=self,
                                                 name=sub_genre['name']))
            self._template_name = item_array['templateName']
            self._type = item_array['type']
            self._updated = int(item_array['updated'])
            self._version = int(item_array['version'])

        else:
            self._created = int(created)
            self._header_image_url = header_image_url
            self._icon_image_url = icon_image_url
            self._icon_url = icon_url
            self._id = id
            self._location = location
            self._mood_image_url = mood_image_url
            self._name = name
            self._number_playlists = int(number_playlists)

            if playlist_uri:
                self._playlist = tunigo.Playlist(main_genre=self,
                                                 uri=playlist_uri)
            else:
                self._playlist = playlist

            self._sub_genres = sub_genres
            self._template_name = template_name
            self._type = type
            self._updated = int(updated)
            self._version = int(version)

    @property
    def created(self):
        return self._created

    @property
    def header_image_url(self):
        return self._header_image_url

    @property
    def icon_image_url(self):
        return self._icon_image_url

    @property
    def icon_url(self):
        return self._icon_url

    @property
    def id(self):
        return self._id

    @property
    def key(self):
        return self._template_name

    @property
    def location(self):
        return self._location

    @property
    def mood_image_url(self):
        return self._mood_image_url

    @property
    def name(self):
        return self._name

    @property
    def number_playlists(self):
        return self._number_playlists

    @property
    def playlist(self):
        return self._playlist

    @property
    def playlist_uri(self):
        return self._playlist.uri

    @property
    def sub_genres(self):
        return self._sub_genres

    @property
    def template_name(self):
        return self._template_name

    @property
    def type(self):
        return self._type

    @property
    def updated(self):
        return self._updated

    @property
    def version(self):
        return self._version


class SubGenre(object):

    def __init__(self, key='', main_genre=None, name=''):
        self._key = key
        self._main_genre = main_genre
        self._name = name

    @property
    def key(self):
        return self._key

    @property
    def main_genre(self):
        return self._main_genre

    @property
    def name(self):
        return self._name