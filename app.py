from flask import Flask, render_template
from utils import Candidates


app = Flask(__name__)

candidate_list = Candidates()


@app.route('/')
def main_page():
    """Главная страница"""
    list_all = candidate_list.load_candidates_from_json()
    return render_template("list.html", list=list_all)


@app.route('/index.html')
def index_page():
    """Страница с заданием 1 по домашней работе"""
    return render_template('index.html')


@app.route('/candidates/<int:uid>')
def candidate_page(uid):
    """Страница кандидатов, найденных по id"""
    single_candidate = candidate_list.get_candidate(uid)
    if single_candidate:
        return render_template('single.html', single_candidate=single_candidate)
    return 'Нет такого кандидата'

@app.route('/search/<candidate_name>')
def search_page(candidate_name):
    """Страница кандидатов, найденных по имени"""
    search = candidate_list.get_candidates_by_name(candidate_name)
    count = len(search)
    return render_template('search.html', search=search, count=count)


@app.route('/skills/<skill>')
def skills_page(skill):
    """Страница кандидатов, найденных по навыку"""
    skills = candidate_list.get_candidates_by_skill(skill)
    count = len(skills)
    return render_template('skill.html', skills=skills, name=skill, count=count)


if __name__ == "__main__":
    app.run(debug=True)
