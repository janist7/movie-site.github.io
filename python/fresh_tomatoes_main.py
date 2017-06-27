import webbrowser
import os
import re
import templates.template_main as template_main
import templates.list_movies_template as list_movies_template

template = {}
template.update(template_main.get_template())
template.update(list_movies_template.get_template())

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += template["movie_tile_content"].format(
            movie_title=movie.title,
            movie_storyline = movie.storyline,
            movie_raiting = movie.rating,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_main_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('../index.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = template["main_page_content"].format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(template["main_page_head"] + template["main_page_navigation"] + rendered_content + template["main_page_footer"])
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    # url = os.path.abspath(output_file.name)
    # webbrowser.open('file://' + url, new=2)
