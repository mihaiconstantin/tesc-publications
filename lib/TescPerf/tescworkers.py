from threading import Thread
from queue import Queue
from time import time
# from teschelpers import UrlFetcher, UrlBuilder
from lib.TescPerf.teschelpers import UrlFetcher, UrlBuilder


# Links.
class LinkWorker(Thread):
	'''Extracts the links of a search query.'''

	all_links = []

	def __init__(self, queue):
		Thread.__init__(self)
		self.queue = queue


	def run(self):
		# While there are jobs in the queue.
		while True:
			# Get the work (i.e., the page URL) from the queue.
			page_url = self.queue.get()
			# Extract the links.
			LinkWorker.extract_page_links(UrlFetcher(page_url).soup)
			# Mark job as completed.
			self.queue.task_done()


	@classmethod
	def extract_page_links(cls, soup):
		"""Extracts the article links on a page.

		Args:
		    soup (BeautifulSoup): BeautifulSoup object from the request content.
		"""
		papers = soup.find_all('li', {'class': 'portal_list_item'})
		for paper in papers:
			cls.all_links.append(paper.find('h2', class_='title').find('a')['href'])
			print('\t- ' + paper.find('h2', class_='title').find('a')['href'][-43:])


	@staticmethod
	def extract_all_links(start, end, search):
		"""Extracts the article links on all pages for a URL query in a multi-threaded fashion.

		Args:
		    start (int): Year to start searching from.
		    end (int): Year to end searching at.
		    search (string): Search query.
		"""
		time_start = time()
		url = UrlBuilder(start, end, search, 0).url
		metadata = UrlFetcher(url).metadata
		queue = Queue()

		print('\nFrom year: %s' % str(start))
		print('To year: %s' % str(end))
		print('Searching for: %s' % str(search))

		print('\nQuery executed: %s' % url)

		print('\nIdentified %s candidate links distributed across %s page(s).' % (str(metadata[0]), str(metadata[1])))
		print('\nStarting the extraction...')

		for page in range(metadata[1]):
			worker = LinkWorker(queue)
			worker.daemon = True
			worker.start()

		for page in range(metadata[1]):
			queue.put(UrlBuilder(start, end, search, page).url)

		queue.join()

		print('Extraction completed...')
		print('\nFound: %s links.' % len(LinkWorker.all_links))
		print('\nTook: %s seconds.\n' % str(time() - time_start))


# Paper data.
class PaperDataWorker(Thread):
	'''Extracts the paper data.'''

	all_papers = []

	def __init__(self, queue):
		Thread.__init__(self)
		self.queue = queue


	def run(self):
		while True:
			# Get the work (i.e., the paper URL) from the queue.
			paper_url = self.queue.get()
			# Extract the paper data.
			PaperDataWorker.extract_paper_data(UrlFetcher(paper_url))
			# Mark job as completed.
			self.queue.task_done()


	@classmethod
	def extract_paper_data(cls, url_fetcher):
		"""Extracts data for a paper of type article.

		Args:
		    url_fetcher (UrlFetcher): UrlFetcher object.
		"""
		# Get the HTML soup.
		soup = url_fetcher.soup

		# Determine if the paper is a scientific article.
		article = cls.is_article(soup.find('div', class_='view_title').find('p', class_='type').find('span', class_='type_classification').text)

		if article:
			ctx_title = soup.find('div', class_='view_title')
			ctx_body = soup.find('div', class_='view_body')

			paper_data = {'tesc_authors': [], 'external_authors': []}

			# URL.
			paper_data['url'] = url_fetcher.url

			# Title.
			try:
				paper_data['title'] = ctx_title.find('h2', class_='title').text
			except:
				paper_data['title'] = 'Error: title.'

			# Abstract.
			try:
				paper_data['abstract'] = ctx_body.find('div', class_='abstract').text
			except:
				paper_data['abstract'] = 'Error: abstract.'

			# DOI.
			try:
				paper_data['doi'] = ctx_body.find('div', class_='rendering_contributiontojournal_versioneddocumentandlinkextensionanddoiportal').find('ul', class_='digital_object_identifiers').find('li', class_='available').find('a').text.strip()
			except:
				paper_data['doi'] = 'Error: DOI.'

			# Authors.
			try:
				authors = ctx_body.find('div', class_='rendering_associatesauthorsclassifiedlistportal').find('ul', class_='persons').find_all('li')
				for author in authors:
					if author.find('a') is not None:
						paper_data['tesc_authors'].append(author.find('a').text)
					else:
						paper_data['external_authors'].append(author.text)
			except:
				paper_data['tesc_authors'] = 'Error: TESC authors.'
				paper_data['external_authors'] = 'Error: external authors.'

			# Append the paper data if it was an article.
			cls.all_papers.append(paper_data)
			print('\t- For paper: %s' % str(paper_data['title']))


	@staticmethod
	def extract_all_paper_data(all_links):
		"""Extract the data for all papers in the list in a multi-threaded fashion.

		Args:
		    all_links (list): A list of URLs.
		"""
		time_start = time()

		queue = Queue()

		print('\nStarting extracting the paper data...')
		for thread in range(20):
			worker = PaperDataWorker(queue)
			worker.daemon = True
			worker.start()

		for paper_link in all_links:
			queue.put(paper_link)

		queue.join()

		print('Extraction completed...')
		print('\nFound: %s papers of type scientific article.' % len(PaperDataWorker.all_papers))
		print('\nTook: %s seconds.' % str(time() - time_start))
		print('\nDone with all.')


	@staticmethod
	def is_article(category):
		"""Checks if a paper is an article.

		Args:
		    category (string): The paper category.

		Returns:
		    bool: True if the paper is an article, false otherwise.
		"""
		if category == 'Article':
			return True
		return False

