import csv
from datetime import datetime


class StoreCsv:
	'''Write the results for the extracted links (i.e., the TESC KPI).'''

	def __init__(self, all_papers, path=''):
		"""Write all paper data to a .csv file.

		Args:
		    all_papers (list): A list of dictionaries (i.e., each dictionary holds the data for a paper).
		    path (str, optional): The path where to write the .csv file.
		"""
		self.date = datetime.today()
		self.data = [['#', 'Title', 'Pure Link', 'DOI', 'Abstract', 'TESC Authors', 'External Authors']]
		self.path = path
		self.append_content(all_papers)


	def append_content(self, all_papers):
		for i, paper in enumerate(all_papers):
			for key, value in paper.items():
				if key == 'tesc_authors' or key == 'external_authors':
					paper[key] = '#'.join(value)
			self.data.append(
						[str(i), paper['title'], paper['url'], paper['doi'], paper['abstract'], paper['tesc_authors'], paper['external_authors']]
					)


	def save(self, filename=None):
		"""Commit the changes and save the paper data to the file.

		Args:
		    filename (str, optional): The name of the .csv file to be written. Defaults to 'TESC_KPI_dd-mm-yyyy.csv'.
		"""
		if filename is None:
			filename='%s/TESC_KPI_%s-%s-%s.csv' % (self.path, self.date.year, self.date.month, self.date.day)

		self.errors = []

		# with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
		with open(filename, 'w', newline='', encoding='UTF-8') as file:
			csv_writer = csv.writer(file)
			for line in self.data:
				try:
					csv_writer.writerow(line)
				except:
					self.errors.append(line)

		if not self.errors:
			print('\nFile "%s" has been written successfully.' % filename)
		else:
			print('\nFile "%s" has been written, but %s lines raised errors. Handle them manually.' % (filename, len(self.errors)))
