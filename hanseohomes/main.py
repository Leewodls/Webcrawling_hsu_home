from flask import Flask, render_template, request, redirect, send_file
from extractors.h_home import hanseo_home

from file import save_to_file

app = Flask("Hanseo Home")
# 데이터 베이스 생성 / 이전에 검색한 항목 빠르게 리턴
db = {}  # 서버가 켜진 동안만 유지


@app.route("/")
def h_home():
  return render_template("h_home.html")


@app.route("/h_search")
def h_search():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword == "":
    return redirect("/")

  if keyword in db:
    hanseos = db[keyword]
  else:
    hanseos = hanseo_home(keyword)
    db[keyword] = hanseos  # 키워드 값 db에 jobs와 저장

  return render_template("h_search.html", keyword=keyword, hanseos=hanseos)
  # 키워드를  template에 보냄


@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")

  if keyword not in db:
    return redirect(f"/search?keyword={keyword}")

  save_to_file(keyword, db[keyword])
  return send_file(f"{keyword}.csv", as_attachment=True)
  # as_attatchment=True : 다운로드가 실행되도록 해줌


app.run("0.0.0.0")
