import sys

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def usage():
  return \
"""
Usage: python3 main.py <video_id>
"""

def write_to_file(video_id, transcript):
  file_path = "output.md"
  print(f"Writing transcript to file: {file_path}")

  body = f"### Video Transcript\n{transcript}"
  footer = f"### Metadata\nVideo ID: {video_id}\n"
  with open(file_path, 'w') as file:
    file.write(f"{body}\n\n{footer}")

def main():
  if len(sys.argv) != 2:
    print(usage())
    exit()

  video_id = sys.argv[1]

  print(f"Fetching video transcript for {video_id}")
  transcript = YouTubeTranscriptApi.get_transcript(video_id)

  print(f"Formatting video transcript as text")
  formatter = TextFormatter()
  formatted_transcript = formatter.format_transcript(transcript)

  write_to_file(video_id, formatted_transcript)

# Run the script.
main()
