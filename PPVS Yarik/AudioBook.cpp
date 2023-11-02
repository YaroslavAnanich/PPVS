#include "AudioBook.h"

void AudioBook::set_text(string text)
{
	this->text = text;
}

void AudioBook::set_pages(int pages)
{
	this->pages = pages;
}

void AudioBook::set_chapters(int chapters)
{
	this->chapters = chapters;
}

string AudioBook::get_text()
{
	return text;
}

int AudioBook::get_pages()
{
	return pages;
}

int AudioBook::get_chapters()
{
	return chapters;
}

void AudioBook::set_author(string author)
{
	this->author = author;
}

string AudioBook::get_author()
{
	return author;
}
