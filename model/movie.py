from dataclasses import dataclass

@dataclass
class Movie:
    id: int
    name: str
    sinopse: str
    image: str
    video: str
    likes: int = 0
