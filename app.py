from lib.TescPerf.tescworkers import LinkWorker, PaperDataWorker
from flask import Flask
from flask import request
from flask import render_template
import json

# app = Flask(__name__, template_folder='client')
app = Flask(__name__, template_folder='client', static_folder='client/dist')


@app.route('/tesc', methods=['POST'])
def tesc():
	start = request.form['start']
	end = request.form['end']
	search = request.form['search']

	papers = fetch_papers(start, end, search);
	return json.dumps(papers)


@app.route('/')
def index():
    return render_template('index.html')


# External logic.
def fetch_papers(start, end, search):
	'''Scraps the http://pure.uvt.nl database for TESC performance indicators.'''
	
	# Collect the links on all pages.
	LinkWorker.extract_all_links(start, end, search)
	# Collect the data for each paper link that is an article.
	PaperDataWorker.extract_all_paper_data(LinkWorker.all_links)
	# Temporary store the results. 
	papers = PaperDataWorker.all_papers

	# Resetting the links & papers, otherwise they will continue to add up.
	# The reason for such a reset has to do with the fact that flask is
	# an objects that runs as long as the server is up. On the other
	# hand, in PHP after a page is served everything is destroyed. 
	LinkWorker.all_links = []
	PaperDataWorker.all_papers = []

	return papers;
