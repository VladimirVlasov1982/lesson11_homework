import json


class Candidates:
    def __init__(self, path='candidates.json'):
        self.path = path

    def load_candidates_from_json(self) -> list[dict]:
        """Возвращает список всех кандидатов"""
        with open(self.path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_candidate(self, candidate_id: int) -> dict | None:
        """Возвращает одного кандидата по его id"""
        list_candidate = self.load_candidates_from_json()
        if candidate_id > len(list_candidate):
            return None
        else:
            return [candidate for candidate in list_candidate if candidate_id == candidate['id']][0]

    def get_candidates_by_name(self, candidate_name: str) -> list[dict]:
        """Возвращает кандидатов по имени"""
        candidates = self.load_candidates_from_json()
        return [candidate for candidate in candidates if candidate_name.lower() in candidate['name'].lower()]

    def get_candidates_by_skill(self, skill_name) -> list[dict]:
        """Возвращает кандидатов по навыку"""
        lst_candidate = []
        for candidate in self.load_candidates_from_json():
            for skill in candidate['skills'].split(', '):
                if skill.lower() == skill_name.lower() and candidate not in lst_candidate:
                    lst_candidate.append(candidate)
        return lst_candidate
