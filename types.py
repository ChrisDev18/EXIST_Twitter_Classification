"""Add explicit typing to the data set that we read from"""

from typing import List, Literal, TypedDict


class Exist2024Training(TypedDict):
    id_EXIST: str
    lang: Literal["es", "en"]
    tweet: str
    number_annotators: int
    annotators: List[str]
    gender_annotators: List[Literal["F", "M"]]
    age_annotators: str
    ethnicities_annotators: List[str]
    study_levels_annotators: List[str]
    countries_annotators: List[str]
    labels_task1: List[Literal["YES", "NO"]]
    labels_task2: List[Literal["DIRECT", "REPORTED", "JUDGEMENTAL", "-"]]
    labels_task3: List[Literal["IDEOLOGICAL-INEQUALITY", "STEREOTYPING-DOMINANCE", "OBJECTIFICATION", "SEXUAL-VIOLENCE", "MISOGYNY-NON-SEXUAL-VIOLENCE"]]  # Nested lists to capture multiple label options
    split: str
