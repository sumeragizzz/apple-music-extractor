import sys
import traceback
import json
from datetime import datetime
from typing import Any
from appscript import app

def main(args: list) -> int:
    try:
        music = app("Music")

        if not music.isrunning():
            music.run()

        tracks: list[str] = []
        i = 0
        for track in music.library_playlists[1].tracks():
            if i >= 10:
                break
            track_info: dict = get_track_info(track)
            tracks.append(track_info)
            i += 1

        with open("output.json", "w", encoding="utf-8", newline="\n") as jsonfile:
            json.dump(tracks, jsonfile, ensure_ascii=False, indent=4, default=convert_type)
    except Exception as e:
        traceback.print_exc()
        return 1
    else:
        return 0

def get_track_info(track) -> dict:
    return {
        "name": track.name.get(),
        "artist": track.artist.get(),
        "album": track.album.get(),
        "duration": track.duration.get(),
        "track_number": track.track_number.get(),
        "disc_number": track.disc_number.get(),
        "genre": track.genre.get(),
        "year": track.year.get(),
        "rating": track.rating.get(),
        "played_count": track.played_count.get(),
        "played_date": track.played_date.get(),
        "date_added": track.date_added.get(),
        "bit_rate": track.bit_rate.get(),
        "sample_rate": track.sample_rate.get(),
        "size": track.size.get(),
        "location": track.location.get().path,
        "kind": track.kind.get(),
        "composer": track.composer.get(),
        "album_artist": track.album_artist.get(),
        "comment": track.comment.get(),
        "grouping": track.grouping.get(),
        "bpm": track.bpm.get(),
        "compilation": track.compilation.get(),
        "persistent_ID": track.persistent_ID.get(),
        "database_ID": track.database_ID.get()
    }

def convert_type(object: Any) -> Any:
    if isinstance(object, datetime):
        return object.isoformat()
    else:
        return object

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
