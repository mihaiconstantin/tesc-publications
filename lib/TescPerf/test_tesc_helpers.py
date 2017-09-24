import unittest
from teschelpers import UrlBuilder, UrlFetcher
from bs4 import BeautifulSoup
from requests import Response


class TestTescHelpers(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		start = 2016
		end = 2016
		search = '^title:"experience sampling" OR abstract:"experience sampling"'

		cls.url_without_page = UrlBuilder(start, end, search).url
		cls.url_with_page = UrlBuilder(start, end, search, page=9).url
		cls.url_paper = 'https://pure.uvt.nl/portal/en/publications/loneliness-in-the-daily-lives-of-young-adults(65ec3c0a-a419-486d-b7e2-3da2a6f63c71).html'


	def test_url_builder(self):
		self.assertEqual(self.url_without_page, 'https://pure.uvt.nl/portal/en/publications/search.html?uri=&organisationName=TS Social and Behavioral Sciences&organisations=11391&type=/dk/atira/pure/researchoutput/researchoutputtypes/contributiontojournal/article&language=&publicationcategory=4590&peerreview=true&publicationYearsFrom=2016&publicationYearsTo=2016&search=^title:"experience sampling" OR abstract:"experience sampling"')
		self.assertEqual(self.url_with_page, 'https://pure.uvt.nl/portal/en/publications/search.html?uri=&organisationName=TS Social and Behavioral Sciences&organisations=11391&type=/dk/atira/pure/researchoutput/researchoutputtypes/contributiontojournal/article&language=&publicationcategory=4590&peerreview=true&publicationYearsFrom=2016&publicationYearsTo=2016&search=^title:"experience sampling" OR abstract:"experience sampling"&page=9')


	def test_url_fetcher(self):
		request = UrlFetcher(self.url_without_page).request
		soup = UrlFetcher(self.url_without_page).soup

		self.assertIsNotNone(request)
		self.assertIsNotNone(soup)

		self.assertIsInstance(request, Response)
		self.assertIsInstance(soup, BeautifulSoup)


	def test_url_metadata(self):
		metadata_url_without_page = UrlFetcher(self.url_without_page).metadata
		metadata_url_with_page = UrlFetcher(self.url_with_page).metadata

		self.assertSequenceEqual(metadata_url_without_page, (3, 1))
		self.assertSequenceEqual(metadata_url_with_page, (3, 1))

		with self.assertRaises(ValueError):
			fetcher_url_paper = UrlFetcher(self.url_paper)
			fetcher_url_paper.metadata


if __name__ == '__main__':
	unittest.main()
